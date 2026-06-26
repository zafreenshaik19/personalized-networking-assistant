from fastapi import FastAPI
from services.topic_generator import generate_starters

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Personalized Networking Assistant"}

@app.get("/generate-conversation")
def generate(event: str, interests: str):
    starters = generate_starters(event, interests)
    return {"conversation_starters": starters}