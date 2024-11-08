import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import sys
sys.path.append('D:/GenAI/Poetry_generation')
from prompt_generator import create_prompt

# Load pre-trained model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_poem(prompt: str, max_length: int = 50) -> str:
    # Encode the prompt and generate the poem
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    poem = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return poem

# Test the function
if __name__ == "__main__":
    theme = "sunset"
    form = "poem"
    prompt = create_prompt(theme, form)
    poem = generate_poem(prompt)
    print(poem)
