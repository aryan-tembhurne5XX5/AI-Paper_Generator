import os
import json
import time
from glob import glob
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Define the data structure for extraction
class QuestionData(BaseModel):
    subject: str = Field(description="The subject of the question paper")
    topic: str = Field(description="The specific topic the question belongs to")
    marks: int = Field(description="The marks allocated for the question")
    question: str = Field(description="The exact text of the question")

class PaperData(BaseModel):
    questions: list[QuestionData] = Field(description="List of questions extracted from the paper")

def main():
    # Initialize the LLM (using Groq for fast, free generation)
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1, max_retries=3)
    parser = PydanticOutputParser(pydantic_object=PaperData)

    prompt = PromptTemplate(
        template="You are a data extraction expert. Extract all individual questions from the following college question paper text.\n\n"
                 "Identify the overall Subject of the paper. For each question, identify the Topic it belongs to, the Marks allocated, and the Question text itself.\n\n"
                 "Text: {text}\n\n{format_instructions}\n",
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chain = prompt | llm | parser

    input_dir = "parsed_markdown"
    output_file = "training_dataset.jsonl"
    
    # Get all markdown files
    md_files = glob(os.path.join(input_dir, "*.md"))
    
    if not md_files:
        print(f"No markdown files found in '{input_dir}'.")
        return

    print(f"Found {len(md_files)} markdown files. Starting extraction...")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for i, file_path in enumerate(md_files):
            print(f"Processing ({i+1}/{len(md_files)}): {os.path.basename(file_path)}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # If the content is too large, you might need to chunk it. 
                # For now, we assume the paper fits within the context window.
                result = chain.invoke({"text": content})
                
                for q in result.questions:
                    # Format strictly to the requested schema
                    jsonl_entry = {
                        "messages": [
                            {"role": "system", "content": f"You are an expert AI question paper generator for {q.subject}."},
                            {"role": "user", "content": f"Generate a {q.marks}-mark question on {q.topic}."},
                            {"role": "assistant", "content": q.question}
                        ]
                    }
                    out_f.write(json.dumps(jsonl_entry) + '\n')
                
                print(f"Successfully extracted {len(result.questions)} questions.")
                
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
            
            # Rate limiting / Sleep function to prevent API crashes
            print("Sleeping for 3 seconds to respect rate limits...")
            time.sleep(3)
            
    print(f"Dataset generated successfully at {output_file}")

if __name__ == "__main__":
    main()
