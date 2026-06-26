import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.topic_generator import generate_starters


def test_generate_starters():
    starters = generate_starters(
        "AI Conference",
        "Machine Learning"
    )

    assert len(starters) == 3
    assert "AI Conference" in starters[0]
    assert "Machine Learning" in starters[1]