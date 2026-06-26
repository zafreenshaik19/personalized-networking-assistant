from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

LABELS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Cloud Computing",
    "Blockchain",
    "Healthcare",
    "Sustainability",
    "Cybersecurity",
    "Data Science",
    "Networking"
]

def analyze_event(event):
    result = classifier(event, LABELS)
    return result["labels"][:3]