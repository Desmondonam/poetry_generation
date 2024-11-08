from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model and tokenizer from Hugging Face
model_name = "gpt2"  # Use "gpt-2" for free or smaller resources; "gpt-3" requires API
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

print("Model and tokenizer loaded successfully!")