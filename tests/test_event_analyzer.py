import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.event_analyzer import analyze_event


def test_analyze_event():

    result = analyze_event("AI for Sustainable Cities")

    assert "Artificial Intelligence" in result
    assert "Sustainability" in result