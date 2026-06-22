# AI Paper Generator Pipeline

This project contains two primary phases for automating the generation of an AI question paper generator using Llama 3.

## Phase 1: Dataset Generation (`generate_dataset.py`)

This script extracts questions from your college question papers (`parsed_markdown/`) and formats them into a structured JSONL dataset (`training_dataset.jsonl`) ready for supervised fine-tuning (SFT).

### Setup for Free Extraction (Using Groq)

To keep this completely free, we've configured the script to use **Groq's Llama 3 API**, which offers high-speed LLM inference at zero cost (with generous rate limits).

1. **Get your FREE API Key**:
   - Go to [GroqCloud Console](https://console.groq.com/keys).
   - Create an account (it's completely free).
   - Generate a new API key.
2. **Add it to your `.env` file**:
   - Open the `.env` file in this directory.
   - Replace `"your_api_key_here"` with your actual key.
3. **Install Dependencies**:
   ```bash
   pip install langchain langchain-groq pydantic python-dotenv
   ```
4. **Run the Script**:
   ```bash
   python generate_dataset.py
   ```

## Phase 2: Fine-Tuning the Model (`finetune_unsloth.py`)

This script uses the `unsloth` library to perform highly memory-efficient fine-tuning on a Llama-3-8B-Instruct model using your generated dataset. It is designed to be run in a GPU environment like Google Colab.

### Running in Google Colab (Free Tier)

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook and ensure you are using a GPU:
   - `Runtime` > `Change runtime type` > Select `T4 GPU`.
3. Upload your `training_dataset.jsonl` file to the Colab environment.
4. Copy the entire contents of `finetune_unsloth.py` into a notebook cell.
5. Uncomment the first two `!pip install` lines at the top of the script and run the cell.
6. The script will train the model and save the adapters to a folder named `llama3-paper-generator-lora`.

Once you've generated the dataset and fine-tuned your model, let me know, and we can proceed to build the UI!
# AI-Paper_Generator
