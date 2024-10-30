import telegram
import os
from dotenv import load_dotenv

load_dotenv()
TG_API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = telegram.Bot(token=TG_API_KEY)

bot.send_message(chat_id="@starsspacesuper", text="Привет! Это сообщение из Python.")
