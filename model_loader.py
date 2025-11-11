# model_loader.py
import os
from dotenv import load_dotenv
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

load_dotenv()

# Get Hugging Face token from environment
HF_TOKEN = os.environ.get("HUGGINGFACE_TOKEN")
if HF_TOKEN is None:
    raise ValueError("Please set your Hugging Face token in HUGGINGFACE_TOKEN environment variable.")

# Model name
MODEL_NAME = "RedHatAI/Llama-3.2-3B-Instruct-quantized.w8a8"

# Load tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)

# Load model
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)

# Choose device
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print(f"Model loaded on {device}")
