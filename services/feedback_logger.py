import json

def save_feedback(feedback):

    with open("data/feedback.json", "r") as file:
        data = json.load(file)

    data.append({
        "feedback": feedback
    })

    with open("data/feedback.json", "w") as file:
        json.dump(data, file, indent=4)