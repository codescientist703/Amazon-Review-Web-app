import requests


def summarization(text):
    url = "https://rapidapi.p.rapidapi.com/nlp/summarize"
    payload = {"text": text}
    headers = {
        "content-type": "application/json",
        "x-rapidapi-host": "text-monkey-summarizer.p.rapidapi.com",
        "x-rapidapi-key": "7237c4ebb0msh564d5594c0cdc53p1a98c9jsna9111a62800e",
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text