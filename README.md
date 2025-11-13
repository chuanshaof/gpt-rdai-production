# Llama-3.2-3B Instruct FastAPI Service (Quantized)

This project is a **Dockerized FastAPI API** serving the **RedHatAI/Llama-3.2-3B-Instruct-quantized.w8a8** model from Hugging Face.  

It allows you to send text prompts and receive model-generated completions. The model is quantized (INT8) for reduced memory usage and can run on CPU or GPU.

---

## **Setup & Running Locally**

1. **Clone the repository** (if using git):

```bash
git clone <your-repo-url>
cd llama-api
```

2. Set up Python environment:
```
python -m venv venv
source venv/bin/activate       # Linux / Mac
# venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

3. Set your Hugging Face token:
```
export HUGGINGFACE_TOKEN=hf_xxx   # Linux / Mac
# set HUGGINGFACE_TOKEN=hf_xxx    # Windows
```

4. Run FastAPI locally:
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Example request JSON:
```
{
  "text": "Hello, how are you?",
  "max_tokens": 50
}
```

Example response JSON:
```
{
  "response": "Hello! I'm fine, thank you. How can I help you today?"
}
```

Docker usage:
1. Build docker image
```
docker build -t gpt-rdai-production .
```

2. Run the container
```
docker run -p 8000:8000 -e HUGGINGFACE_TOKEN=$HUGGINGFACE_TOKEN gpt-rdai-production
```

The API will be accessible at http://localhost:8000/docs (Swagger UI).

You can send requests from your browser, curl, Postman, or any HTTP client.

### Optional: persist model cache:
```
docker run -p 8000:8000 \
  -e HUGGINGFACE_TOKEN=$HUGGINGFACE_TOKEN \
  -v /local/models:/root/.cache/huggingface/transformers \
  llama-api
```
