from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from .translator import translate_text
from config.settings import settings

def handle_event(event, line_bot_api):
    if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        user_text = event.message.text

        # Optional translation flow
        response_text = user_text
        if settings.TRANSLATION_ENABLED:
            response_text = translate_text(
                user_text,
                target_language=settings.TARGET_LANGUAGE
            )

        # Simple logic: echo or translated reply
        message = TextSendMessage(text=response_text)
        line_bot_api.reply_message(event.reply_token, message)
