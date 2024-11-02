import telegram
import os
import time
import random
import argparse
import sys


from dotenv import load_dotenv

load_dotenv()
TG_API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = telegram.Bot(token=TG_API_KEY)
tg_chat_id = "@starsspacesuper"
directory = 'images'
filesindir = os.listdir(directory)
parser = argparse.ArgumentParser(
                    description='Отправляет фото с телеграм канал. Укажите время задержки отправки фото. Значение по умолчанию 4 часа',
                    )
parser.add_argument("time", nargs="?", help='Время задержки отправки фото.', default=14400, type=int)
waiting_time = parser.parse_args(sys.argv[1:]).time

if __name__ == "__main__":
    for filesindirs in filesindir:
        path = os.path.join(filesindirs)
        file = os.path.join(str(directory), path)
        bot.send_document(chat_id=tg_chat_id, document=open(file, 'rb'))
        time.sleep(waiting_time)
    while True:
        random.shuffle(filesindir)
        for filesindirs in filesindir:
            path = os.path.join(filesindirs)
            file = os.path.join(str(directory), path)
            bot.send_document(chat_id=tg_chat_id, document=open(file, 'rb'))
            time.sleep(waiting_time)



