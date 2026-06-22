// ═══════════════════════════════════════════════
// AI Question Paper Generator – Frontend Logic
// ═══════════════════════════════════════════════

let subjects = [];
let subjectTopics = {};
let selectedTopics = [];
let useAI = true;
let generatedLatex = '';

// ─── Init ───
document.addEventListener('DOMContentLoaded', async () => {
    await loadSubjects();
    setupEventListeners();
});

// ─── Load Subjects ───
async function loadSubjects() {
    try {
        const res = await fetch('/api/subjects');
        const data = await res.json();
        subjects = data.subjects || [];
        subjectTopics = data.subject_topics || {};
        populateSubjectDropdown();
    } catch (e) {
        showToast('Failed to load subjects', 'error');
    }
}

function populateSubjectDropdown() {
    const sel = document.getElementById('subject');
    sel.innerHTML = '<option value="">Select a subject...</option>';
    subjects.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s;
        opt.textContent = s;
        sel.appendChild(opt);
    });
}

// ─── Event Listeners ───
function setupEventListeners() {
    // Subject change → update topics
    document.getElementById('subject').addEventListener('change', e => {
        selectedTopics = [];
        renderTopics(e.target.value);
    });

    // Marks slider
    const marksSlider = document.getElementById('total_marks');
    marksSlider.addEventListener('input', () => {
        document.getElementById('marks-display').textContent = marksSlider.value;
    });

    // Difficulty sliders
    ['easy', 'medium', 'hard'].forEach(id => {
        document.getElementById(`diff-${id}`).addEventListener('input', updateDifficultyTotal);
    });

    // Bloom inputs
    document.querySelectorAll('.bloom-input').forEach(input => {
        input.addEventListener('input', () => {
            const item = input.closest('.bloom-item');
            const fill = item.querySelector('.bloom-fill');
            fill.style.width = input.value + '%';
        });
    });

    // Mode toggle
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            useAI = btn.dataset.mode === 'ai';
        });
    });

    // Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    // Form submit
    document.getElementById('paper-form').addEventListener('submit', handleGenerate);

    // Copy & Download
    document.getElementById('copy-latex').addEventListener('click', () => {
        navigator.clipboard.writeText(generatedLatex).then(() => showToast('LaTeX copied to clipboard!', 'success'));
    });
    document.getElementById('download-latex').addEventListener('click', downloadLatex);
}

// ─── Topics ───
function renderTopics(subject) {
    const container = document.getElementById('topics-container');
    const topics = subjectTopics[subject] || [];
    if (!topics.length) {
        container.innerHTML = '<p class="topics-placeholder">No topics found for this subject</p>';
        return;
    }
    container.innerHTML = '';
    topics.forEach(t => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'topic-chip';
        chip.textContent = t;
        chip.addEventListener('click', () => {
            chip.classList.toggle('selected');
            if (chip.classList.contains('selected')) {
                selectedTopics.push(t);
            } else {
                selectedTopics = selectedTopics.filter(x => x !== t);
            }
        });
        container.appendChild(chip);
    });
}

// ─── Difficulty ───
function updateDifficultyTotal() {
    const e = parseInt(document.getElementById('diff-easy').value);
    const m = parseInt(document.getElementById('diff-medium').value);
    const h = parseInt(document.getElementById('diff-hard').value);
    document.getElementById('easy-val').textContent = e + '%';
    document.getElementById('medium-val').textContent = m + '%';
    document.getElementById('hard-val').textContent = h + '%';
    const total = e + m + h;
    const el = document.getElementById('diff-total-val');
    el.textContent = total + '%';
    el.className = total === 100 ? 'diff-total-num' : 'diff-total-num invalid';
}

// ─── Tabs ───
function switchTab(tab) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelector(`[data-tab="${tab}"]`).classList.add('active');
    document.getElementById('preview-paper').style.display = tab === 'paper' ? 'block' : 'none';
    document.getElementById('preview-latex').style.display = tab === 'latex' ? 'block' : 'none';
}

// ─── Generate ───
async function handleGenerate(e) {
    e.preventDefault();
    const btn = document.getElementById('generate-btn');
    const btnText = btn.querySelector('.btn-text');
    const btnLoader = btn.querySelector('.btn-loader');

    const subject = document.getElementById('subject').value;
    if (!subject) { showToast('Please select a subject', 'error'); return; }

    btn.disabled = true;
    btnText.style.display = 'none';
    btnLoader.style.display = 'flex';

    const payload = {
        subject,
        total_marks: parseInt(document.getElementById('total_marks').value),
        topics: selectedTopics,
        difficulty: {
            Easy: parseInt(document.getElementById('diff-easy').value),
            Medium: parseInt(document.getElementById('diff-medium').value),
            Hard: parseInt(document.getElementById('diff-hard').value)
        },
        bloom_distribution: {
            Remember: parseInt(document.getElementById('bloom-remember').value),
            Understand: parseInt(document.getElementById('bloom-understand').value),
            Apply: parseInt(document.getElementById('bloom-apply').value),
            Analyze: parseInt(document.getElementById('bloom-analyze').value),
            Evaluate: parseInt(document.getElementById('bloom-evaluate').value),
            Create: parseInt(document.getElementById('bloom-create').value)
        },
        exam_name: document.getElementById('exam_name').value,
        semester: document.getElementById('semester').value,
        year: document.getElementById('year').value,
        duration: document.getElementById('duration').value,
        use_ai: useAI
    };

    try {
        const res = await fetch('/api/generate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
        const data = await res.json();
        if (data.error) { showToast(data.error, 'error'); return; }
        renderPaper(data, payload);
        generatedLatex = data.latex || '';
        document.getElementById('latex-code').textContent = generatedLatex;
        showToast('Question paper generated successfully!', 'success');
    } catch (err) {
        showToast('Generation failed: ' + err.message, 'error');
    } finally {
        btn.disabled = false;
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
    }
}

// ─── Render Paper Preview ───
function renderPaper(data, payload) {
    document.getElementById('preview-empty').style.display = 'none';
    document.getElementById('preview-paper').style.display = 'block';

    const sheet = document.getElementById('paper-sheet');
    sheet.innerHTML = `
        <div class="paper-header">
            <h1>Savitribai Phule Pune University</h1>
            <h2>${payload.exam_name || 'End Semester Examination'}</h2>
            <h3>${data.subject}</h3>
        </div>
        <div class="paper-meta">
            <span><strong>Semester:</strong> ${payload.semester || 'I'}</span>
            <span><strong>Duration:</strong> ${payload.duration || '3 Hours'}</span>
            <span><strong>Total Marks:</strong> ${data.total_marks}</span>
            <span><strong>Year:</strong> ${payload.year || '2024'}</span>
        </div>
        <div class="paper-instructions">
            <strong>Instructions:</strong>
            <ol>
                <li>Answer all questions.</li>
                <li>Figures to the right indicate full marks.</li>
                <li>Assume suitable data, if necessary.</li>
                <li>Neat diagrams must be drawn wherever necessary.</li>
            </ol>
        </div>
        <hr style="border:1px solid #333; margin: 12px 0;">
        <div class="paper-body">${escapeHtml(data.paper_text)}</div>
        <hr style="border:1px solid #999; margin: 20px 0 8px;">
        <p style="text-align:center; font-style:italic; font-size:12px;">— End of Question Paper —</p>
    `;

    switchTab('paper');
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// ─── Download LaTeX ───
function downloadLatex() {
    if (!generatedLatex) { showToast('Generate a paper first', 'error'); return; }
    const blob = new Blob([generatedLatex], { type: 'text/x-tex' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'question_paper.tex';
    a.click();
    URL.revokeObjectURL(url);
    showToast('LaTeX file downloaded!', 'success');
}

// ─── Toast ───
function showToast(msg, type = 'info') {
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
}
