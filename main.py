from fastapi import FastAPI
from services.topic_generator import generate_starters
from services.event_analyzer import analyze_event

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Personalized Networking Assistant"
    }


@app.get("/generate-conversation")
def generate(event: str, interests: str):

    starters = generate_starters(event, interests)

    return {
        "conversation_starters": starters
    }


@app.get("/analyze-event")
def analyze(event: str):

    themes = analyze_event(event)

    return {
        "themes": themes
    }