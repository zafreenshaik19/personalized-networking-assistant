import wikipedia

def fact_check(topic):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(topic, sentences=2)
        return summary

    except Exception as e:
        return str(e)