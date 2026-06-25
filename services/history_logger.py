import json

def save_history(event, interests):

    with open("data/history.json", "r") as file:
        history = json.load(file)

    history.append({
        "event": event,
        "interests": interests
    })

    with open("data/history.json", "w") as file:
        json.dump(history, file, indent=4)