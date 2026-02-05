# line-messaging-translation-automation

This repository contains a production-ready **LINE bot** designed for chat automation with optional message translation. It demonstrates how to build a LINE app chat bot using the LINE Messaging API, with clean webhook handling and extensible logic.

The project can be used as a foundation for a line translator bot, customer support automation, or multilingual chat workflows on the LINE messaging app.

## Setup

1. Create a LINE Official Account and obtain:
   - Channel Access Token
   - Channel Secret

2. Create a `.env` file:
   LINE_CHANNEL_ACCESS_TOKEN=your_token
   LINE_CHANNEL_SECRET=your_secret

3. Install dependencies:
   pip install -r requirements.txt

4. Run locally:
   uvicorn app.api:app --reload

## Notes

- Translation logic is abstracted in `translator.py`
- Flex messages can be added in `handlers.py`
- Built for clarity, safety, and maintainability
