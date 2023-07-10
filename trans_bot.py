import telegram
import random
import asyncio
TOKEN = "6385470739:AAHKGqX0h8Bd6VCgaYzpsNXIPMTX1bB3ncg"
CHAT_ID = "-961467793"
async def send_test_message(message):
    try:
        telegram_notify = telegram.Bot(TOKEN)    
        await telegram_notify.send_message(chat_id=CHAT_ID, text=message,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)
