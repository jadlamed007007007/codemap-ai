import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def explain_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = f"Explain this Python file clearly:\n\n{content}"

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
