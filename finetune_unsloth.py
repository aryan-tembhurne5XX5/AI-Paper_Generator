"""
Google Colab-ready Python script using the unsloth library to fine-tune Llama-3-8B-Instruct.

In Google Colab, you will first need to run the following pip install commands in a notebook cell:

# Install Unsloth, Xformers, and TRL
!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
!pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes
"""

import os
from unsloth import FastLanguageModel
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments

def main():
    # 1. Load the unsloth/llama-3-8b-Instruct-bnb-4bit model
    max_seq_length = 2048 # Can be increased, but 2048 is good for this use case
    dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
    load_in_4bit = True # Use 4bit quantization to reduce memory usage

    print("Loading model and tokenizer...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "unsloth/llama-3-8b-Instruct-bnb-4bit",
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )

    # 2. Apply standard LoRA parameters
    print("Applying LoRA adapters...")
    model = FastLanguageModel.get_peft_model(
        model,
        r = 16, # Suggested 8, 16, 32, 64, 128
        target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                          "gate_proj", "up_proj", "down_proj",],
        lora_alpha = 16,
        lora_dropout = 0, # Supports any, but = 0 is optimized
        bias = "none",    # Supports any, but = "none" is optimized
        use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
        random_state = 3407,
        use_rslora = False,  # We support rank stabilized LoRA
        loftq_config = None, # And LoftQ
    )

    # 3. Write the dataset mapping function to format JSONL into the prompt format
    def format_chat_template(examples):
        texts = []
        for messages in examples["messages"]:
            # Uses the model's specific chat template (Llama-3 format)
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False
            )
            texts.append(text)
        return {"text": texts}

    print("Loading and mapping dataset...")
    # Load the JSONL dataset
    dataset = load_dataset("json", data_files={"train": "training_dataset.jsonl"}, split="train")

    # Map the dataset to format the text
    dataset = dataset.map(format_chat_template, batched=True)

    # 4. Set up the SFTTrainer with reasonable hyperparameters
    trainer = SFTTrainer(
        model = model,
        tokenizer = tokenizer,
        train_dataset = dataset,
        dataset_text_field = "text",
        max_seq_length = max_seq_length,
        dataset_num_proc = 2,
        packing = False, # Can make training 5x faster for short sequences
        args = TrainingArguments(
            per_device_train_batch_size = 2,
            gradient_accumulation_steps = 4,
            warmup_steps = 5,
            num_train_epochs = 3, # Training for 1 to 3 epochs
            learning_rate = 2e-4,
            fp16 = not FastLanguageModel.is_bfloat16_supported(),
            bf16 = FastLanguageModel.is_bfloat16_supported(),
            logging_steps = 1,
            optim = "adamw_8bit",
            weight_decay = 0.01,
            lr_scheduler_type = "linear",
            seed = 3407,
            output_dir = "outputs",
            report_to = "none", # Use "wandb" to log to weights & biases
        ),
    )

    # Train the model
    print("Starting training...")
    trainer_stats = trainer.train()

    # 5. Save the fine-tuned LoRA adapters locally
    save_directory = "llama3-paper-generator-lora"
    print(f"Saving model adapters to {save_directory}...")
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)

    # 6. Example of how to run inference to generate a new question
    print("\n--- Running Inference Example ---")
    FastLanguageModel.for_inference(model) # Enable native 2x faster inference

    messages = [
        {"role": "system", "content": "You are an expert AI question paper generator for Data Structures and Algorithms."},
        {"role": "user", "content": "Generate a 10-mark question on Graph Traversal."}
    ]

    # Format the input using the chat template
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True, # Tells the model to start generating the assistant's response
        return_tensors="pt"
    ).to("cuda")

    # Generate the output
    outputs = model.generate(input_ids=inputs, max_new_tokens=256, use_cache=True)
    
    # Decode and print the response
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    
    print("Generated Output:")
    print(response)

if __name__ == "__main__":
    main()
