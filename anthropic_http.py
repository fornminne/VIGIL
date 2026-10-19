import json
import os
import urllib.request
import urllib.error

def send_message(prompt, model="claude-sonnet-4-5",
                 max_tokens=1024):
    api_key = os.environ["ANTHROPIC_API_KEY"]

    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(
            request, timeout=120
        ) as response:
            return json.load(response)

    except urllib.error.HTTPError as error:
        print("API error:", error.code)
        print(error.read().decode())
        raise
