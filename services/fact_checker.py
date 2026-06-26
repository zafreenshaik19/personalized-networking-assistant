import requests

def fact_check(topic):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

        headers = {
            "User-Agent": "PersonalizedNetworkingAssistant/1.0 (student project)"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary available.")

        elif response.status_code == 404:
            return "No Wikipedia page found."

        else:
            return f"Wikipedia API Error: {response.status_code}"

    except Exception as e:
        return str(e)