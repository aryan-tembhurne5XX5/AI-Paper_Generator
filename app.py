"""
AI Question Paper Generator - Flask Backend
Uses Groq API + training dataset to generate structured question papers.
"""

import os
import json
import random
import re
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ──────────────────────────────────────────────
# Load training dataset into memory
# ──────────────────────────────────────────────
DATASET_PATH = os.path.join(os.path.dirname(__file__), "training_dataset.jsonl")


def load_dataset():
    """Load the JSONL training dataset and index by subject."""
    questions = []
    subjects = set()
    subject_topics = {}

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                msgs = entry.get("messages", [])
                if len(msgs) < 3:
                    continue

                system_msg = msgs[0]["content"]
                user_msg = msgs[1]["content"]
                assistant_msg = msgs[2]["content"]

                # Extract subject from system message
                subject_match = re.search(
                    r"question paper generator for (.+?)\.$", system_msg
                )
                subject = subject_match.group(1) if subject_match else "Unknown"

                # Extract marks and topic from user message
                marks_match = re.search(r"(\d+)-mark", user_msg)
                marks = int(marks_match.group(1)) if marks_match else 0

                topic_match = re.search(r"question on (.+?)\.$", user_msg)
                topic = topic_match.group(1) if topic_match else "General"

                q = {
                    "subject": subject,
                    "topic": topic,
                    "marks": marks,
                    "question": assistant_msg,
                }

                questions.append(q)
                subjects.add(subject)

                if subject not in subject_topics:
                    subject_topics[subject] = set()
                subject_topics[subject].add(topic)

            except (json.JSONDecodeError, IndexError, KeyError):
                continue

    # Convert sets to sorted lists
    subject_topics = {k: sorted(list(v)) for k, v in subject_topics.items()}
    return questions, sorted(list(subjects)), subject_topics


QUESTIONS, SUBJECTS, SUBJECT_TOPICS = load_dataset()


# ──────────────────────────────────────────────
# Helper: select questions from dataset
# ──────────────────────────────────────────────
def select_questions_from_dataset(subject, total_marks, topics=None):
    """Select a set of questions from the dataset matching the criteria."""
    pool = [q for q in QUESTIONS if q["subject"] == subject and q["marks"] > 0]

    if topics:
        topic_list = [t.strip() for t in topics if t.strip()]
        if topic_list:
            filtered = [q for q in pool if q["topic"] in topic_list]
            if filtered:
                pool = filtered

    if not pool:
        return []

    random.shuffle(pool)

    selected = []
    current_marks = 0

    for q in pool:
        if current_marks + q["marks"] <= total_marks:
            selected.append(q)
            current_marks += q["marks"]
        if current_marks >= total_marks:
            break

    # If we haven't reached total marks, allow some more
    if current_marks < total_marks:
        remaining = [q for q in pool if q not in selected]
        for q in remaining:
            if current_marks + q["marks"] <= total_marks + 5:
                selected.append(q)
                current_marks += q["marks"]
            if current_marks >= total_marks:
                break

    return selected


# ──────────────────────────────────────────────
# Helper: generate with Groq LLM
# ──────────────────────────────────────────────
def generate_with_groq(subject, total_marks, topics, difficulty_pct, bloom_dist, exam_name, semester, year, duration):
    """Use Groq LLM to generate a full question paper."""
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key:
        return None, "GROQ_API_KEY not set in .env"

    client = Groq(api_key=api_key)

    # Get sample questions for context
    samples = select_questions_from_dataset(subject, total_marks, topics)
    sample_text = ""
    for i, s in enumerate(samples[:10], 1):
        sample_text += f"{i}. [{s['marks']} marks] ({s['topic']}) {s['question']}\n"

    difficulty_str = ", ".join([f"{k}: {v}%" for k, v in difficulty_pct.items()]) if difficulty_pct else "Easy: 30%, Medium: 50%, Hard: 20%"
    bloom_str = ", ".join([f"{k}: {v}%" for k, v in bloom_dist.items()]) if bloom_dist else "Remember: 20%, Understand: 20%, Apply: 20%, Analyze: 15%, Evaluate: 15%, Create: 10%"
    topics_str = ", ".join(topics) if topics else "All topics"

    prompt = f"""You are an expert university question paper generator for the subject: {subject}.

Generate a COMPLETE, structured question paper with the following specifications:
- Subject: {subject}
- Exam: {exam_name or 'End Semester Examination'}
- Semester: {semester or 'I'}
- Year: {year or '2024'}
- Duration: {duration or '3 Hours'}
- Total Marks: {total_marks}
- Topics to cover: {topics_str}
- Difficulty Distribution: {difficulty_str}
- Bloom's Taxonomy Distribution: {bloom_str}

Here are reference questions from past papers for this subject:
{sample_text}

IMPORTANT FORMATTING RULES:
1. Structure the paper with numbered questions (Q1, Q2, etc.)
2. Each main question should have sub-parts (a), (b) with internal choice (OR)
3. Clearly mention marks for each sub-question in brackets like [5 Marks]
4. Include a mix of question types: explain, derive, compare, design, numerical
5. Total marks of all questions must add up to {total_marks}
6. Make questions academically rigorous and similar in style to the reference questions
7. DO NOT include answers, only questions

Generate the question paper now in a clean, structured format."""

    # Try multiple models in order of preference (fallback for rate limits)
    models = [
        "llama-3.1-8b-instant",      # Higher rate limit on free tier
        "gemma2-9b-it",               # Alternative fallback
        "llama-3.3-70b-versatile",    # Best quality but lowest rate limit
    ]

    messages = [
        {"role": "system", "content": f"You are an expert AI question paper generator for {subject}. Generate university-level exam papers with proper structure."},
        {"role": "user", "content": prompt}
    ]

    last_error = None
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=3000,
            )
            paper_text = response.choices[0].message.content
            return paper_text, None
        except Exception as e:
            last_error = str(e)
            if "rate_limit" in last_error.lower():
                continue  # Try next model
            else:
                return None, last_error

    return None, f"All models rate-limited. Use 'Dataset Only' mode or try again later. Last error: {last_error}"


# ──────────────────────────────────────────────
# Helper: generate LaTeX from paper text
# ──────────────────────────────────────────────
def generate_latex(paper_text, subject, exam_name, semester, year, duration, total_marks):
    """Convert the generated paper to LaTeX format matching university style."""
    # Escape LaTeX special characters in the paper text
    escaped = paper_text
    for char in ['&', '%', '$', '#', '_', '{', '}']:
        escaped = escaped.replace(char, f'\\{char}')
    escaped = escaped.replace('~', '\\textasciitilde{}')
    escaped = escaped.replace('^', '\\textasciicircum{}')

    latex = r"""\documentclass[12pt,a4paper]{article}
\usepackage[margin=2cm]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{array}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{tikz}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.3pt}
\fancyfoot[C]{\thepage}

\begin{document}

% ─── Header Section ───
\begin{center}
    {\Large \textbf{SAVITRIBAI PHULE PUNE UNIVERSITY}} \\[4pt]
    {\large """ + (exam_name or 'End Semester Examination') + r"""} \\[4pt]
    {\large \textbf{""" + subject + r"""}} \\[6pt]
    \rule{\textwidth}{0.4pt}
\end{center}

\vspace{4pt}

\noindent
\begin{tabularx}{\textwidth}{@{}X r@{}}
    \textbf{Semester:} """ + (semester or 'I') + r""" & \textbf{Year:} """ + (year or '2024') + r""" \\
    \textbf{Duration:} """ + (duration or '3 Hours') + r""" & \textbf{Total Marks:} """ + str(total_marks) + r""" \\
\end{tabularx}

\vspace{2pt}
\rule{\textwidth}{0.4pt}

\vspace{6pt}
\noindent \textbf{Instructions:}
\begin{enumerate}[leftmargin=*, nosep]
    \item Answer all questions.
    \item Figures to the right indicate full marks.
    \item Assume suitable data, if necessary.
    \item Neat diagrams must be drawn wherever necessary.
\end{enumerate}

\vspace{4pt}
\rule{\textwidth}{0.4pt}
\vspace{8pt}

% ─── Questions ───
\begin{flushleft}
""" + escaped + r"""
\end{flushleft}

\vspace{12pt}
\begin{center}
    \rule{3cm}{0.4pt} \\[4pt]
    \textit{End of Question Paper}
\end{center}

\end{document}
"""
    return latex


# ──────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/subjects", methods=["GET"])
def get_subjects():
    """Return all unique subjects from the dataset."""
    return jsonify({"subjects": SUBJECTS, "subject_topics": SUBJECT_TOPICS})


@app.route("/api/generate", methods=["POST"])
def generate_paper():
    """Generate a question paper based on user input."""
    data = request.json

    subject = data.get("subject", "")
    total_marks = int(data.get("total_marks", 80))
    topics = data.get("topics", [])
    difficulty_pct = data.get("difficulty", {})
    bloom_dist = data.get("bloom_distribution", {})
    exam_name = data.get("exam_name", "End Semester Examination")
    semester = data.get("semester", "I")
    year = data.get("year", "2024")
    duration = data.get("duration", "3 Hours")
    use_ai = data.get("use_ai", True)

    if not subject:
        return jsonify({"error": "Subject is required"}), 400

    if use_ai:
        paper_text, error = generate_with_groq(
            subject, total_marks, topics, difficulty_pct, bloom_dist,
            exam_name, semester, year, duration
        )
        if error:
            return jsonify({"error": error}), 500
    else:
        # Fallback: use dataset-only mode
        selected = select_questions_from_dataset(subject, total_marks, topics)
        if not selected:
            return jsonify({"error": f"No questions found for subject '{subject}'"}), 404

        paper_text = ""
        q_num = 1
        for i in range(0, len(selected), 2):
            paper_text += f"\nQ{q_num})\n"
            paper_text += f"  a) {selected[i]['question']} [{selected[i]['marks']} Marks]\n"
            if i + 1 < len(selected):
                paper_text += f"                              OR\n"
                paper_text += f"  b) {selected[i+1]['question']} [{selected[i+1]['marks']} Marks]\n"
            q_num += 1

    # Generate LaTeX
    latex = generate_latex(paper_text, subject, exam_name, semester, year, duration, total_marks)

    return jsonify({
        "paper_text": paper_text,
        "latex": latex,
        "subject": subject,
        "total_marks": total_marks,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5050)
