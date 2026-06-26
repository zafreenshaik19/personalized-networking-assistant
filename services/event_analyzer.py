def analyze_event(event):

    keywords = []

    event = event.lower()

    if "ai" in event:
        keywords.append("Artificial Intelligence")

    if "cloud" in event:
        keywords.append("Cloud Computing")

    if "blockchain" in event:
        keywords.append("Blockchain")

    if "health" in event:
        keywords.append("Healthcare")

    if "sustain" in event:
        keywords.append("Sustainability")

    if len(keywords) == 0:
        keywords.append("General Networking")

    return keywords