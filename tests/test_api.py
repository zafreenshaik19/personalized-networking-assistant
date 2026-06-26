import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Personalized Networking Assistant"


def test_generate():
    response = client.get(
        "/generate-conversation",
        params={
            "event": "AI Conference",
            "interests": "Machine Learning"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "conversation_starters" in data
    assert len(data["conversation_starters"]) == 3