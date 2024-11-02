import telegram
import os
import time
import random
import argparse
import sys


from dotenv import load_dotenv


def main():
    load_dotenv()
    TG_API_KEY = os.getenv("TELEGRAM_API_KEY")
    bot = telegram.Bot(token=TG_API_KEY)
    tg_chat_id = os.getenv("TG_CHAT_ID")
    directory = 'images'
    filesindir = os.listdir(directory)
    parser = argparse.ArgumentParser(
                        description='Отправляет фото с телеграм канал. Укажите время задержки отправки фото. Значение по умолчанию 4 часа',
                        )
    parser.add_argument("time", nargs="?", help='Время задержки отправки фото.', default=14400, type=int)
    waiting_time = parser.parse_args(sys.argv[1:]).time


    first_pass = True

    while True:
        if first_pass:
            file_list= filesindir
            first_pass = False
        else:
            file_list = filesindir[:]
            random.shuffle(file_list)

        for file in file_list:
            file_path = os.path.join(str(directory), file)
            with open(file_path,"rb") as file:
                bot.send_document(chat_id=tg_chat_id, document=file)
            time.sleep(waiting_time)


if __name__ == "__main__":
    main()



