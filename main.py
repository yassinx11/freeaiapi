from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    model: str
    message: str

@app.post("/api/chat")
def chat(req: ChatRequest):
    if req.model == "gpt-4o":
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer YOUR_OPENROUTER_API_KEY",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o",
                "messages": [{"role": "user", "content": req.message}]
            }
        )
        return response.json()
    return {"error": "Unknown model"}
