import telegram
import asyncio

from dotenv import load_dotenv
import os
load_dotenv()


token = os.environ.get('TOKEN')
chat_id = os.environ.get('CHAT_ID')
async def send_test_message(message):
    try:
        telegram_notify = telegram.Bot(token)    
        await telegram_notify.send_message(chat_id=chat_id, text=message,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)
