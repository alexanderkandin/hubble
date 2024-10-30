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
chat_id = "@starsspacesuper"
directory = 'images'
filesindir = os.listdir(directory)
parser = argparse.ArgumentParser()
parser.add_argument("time", nargs="?", default=60, type=int)
waiting_time = parser.parse_args(sys.argv[1:]).time

if __name__ == "__main__":
    for filesindirs in filesindir:
        path = os.path.join(filesindirs)
        file = os.path.join(str(directory), path)
        bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
        time.sleep(waiting_time)
    while True:
        random.shuffle(filesindir)
        for filesindirs in filesindir:
            path = os.path.join(filesindirs)
            file = os.path.join(str(directory), path)
            bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
            time.sleep(waiting_time)



