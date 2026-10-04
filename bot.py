"""Cafe Aroma FAQ bot for Telegram.

Runs in two modes:
  smart   - answers with an LLM (set OPENAI_API_KEY)
  rules   - keyword matching, no API key needed (default fallback)

Usage:
  export TELEGRAM_BOT_TOKEN=123:abc
  python bot.py
"""

import os

import requests

from faq_data import FAQS, KEYWORDS, DEFAULT_REPLY

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
USE_LLM = bool(os.environ.get("OPENAI_API_KEY"))


def llm_answer(question: str) -> str:
    """Answer with the LLM, grounded in the FAQ sheet."""
    knowledge = "\n".join(f"{k}: {v}" for k, v in FAQS.items())
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system",
                 "content": f"You answer for Cafe Aroma using only this info.\n{knowledge}"},
                {"role": "user", "content": question},
            ],
            "max_tokens": 120,
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def rule_answer(question: str) -> str:
    """Keyword match against the FAQ sheet."""
    q = question.lower()
    for topic, words in KEYWORDS.items():
        if any(w in q for w in words):
            return FAQS[topic]
    return DEFAULT_REPLY


def answer(question: str) -> str:
    if USE_LLM:
        try:
            return llm_answer(question)
        except Exception:
            return rule_answer(question)
    return rule_answer(question)


def poll() -> None:
    offset = 0
    print("Bot running. Ctrl+C to stop.")
    while True:
        updates = requests.get(f"{API}/getUpdates", params={"offset": offset, "timeout": 30}, timeout=35).json()
        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message")
            if not msg or "text" not in msg:
                continue
            reply = answer(msg["text"])
            requests.post(f"{API}/sendMessage",
                          json={"chat_id": msg["chat"]["id"], "text": reply}, timeout=15)


if __name__ == "__main__":
    poll()
