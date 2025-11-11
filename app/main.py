# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_loader import tokenizer, model, device
import torch

app = FastAPI(title="Llama-3.2-3B Instruct API")

# Request schema
class Prompt(BaseModel):
    text: str
    max_tokens: int = 50  # default max tokens

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Llama-3.2-3B Instruct API!"}

# Prediction endpoint
@app.post("/predict")
def predict(prompt: Prompt):
    try:
        # Tokenize input and send to device
        inputs = tokenizer(prompt.text, return_tensors="pt").to(device)

        # Generate output
        outputs = model.generate(
            **inputs,
            max_new_tokens=prompt.max_tokens,
            do_sample=True,
            top_p=0.95,
            temperature=0.7
        )

        # Decode output
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
