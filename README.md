# Cafe Aroma FAQ Bot

A customer-support chatbot for a (fictional) cafe, built as a portfolio piece.
It answers opening hours, location, menu, wifi, bookings and pricing questions,
and falls back to a "talk to our team" reply for anything else.

## Two answer modes

- **Rules mode** (default): keyword matching, no API key needed. Runs anywhere.
- **Smart mode**: set `OPENAI_API_KEY` and the bot grounds an LLM in the FAQ sheet.

## Run it

```bash
pip install requests openai
export TELEGRAM_BOT_TOKEN="your-bot-token"   # from @BotFather
python bot.py
```

## What it shows

- Long-polling Telegram bot with zero framework lock-in
- Graceful fallback from LLM to rules when the API is down
- Business FAQ model that is trivial to swap for any real client's data
