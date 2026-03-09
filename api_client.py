"""
OpenRouter API Client
Handles all API communication - by Sanjay G
"""

import os
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set.")
    return key


def call_openrouter(prompt, model="openai/gpt-3.5-turbo"):
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a Python debugging assistant. Analyze the given code, find bugs, explain them, and provide the corrected code.",
            },
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]
