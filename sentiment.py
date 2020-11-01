import requests


def sentiment(text):
    url = "https://microsoft-text-analytics1.p.rapidapi.com/sentiment"
    payload = {
        "documents": [
            {
                "id": 1,
                "language": "en",
                "text": text,
            }
        ]
    }
    headers = {
        "x-rapidapi-host": "microsoft-text-analytics1.p.rapidapi.com",
        "x-rapidapi-key": "7237c4ebb0msh564d5594c0cdc53p1a98c9jsna9111a62800e",
        "content-type": "application/json",
        "accept": "application/json",
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text