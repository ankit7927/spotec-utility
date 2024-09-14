import os, sys
from pathlib import Path
from collector import collector
from uploader import uploader
from threading import Thread

import logging

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

song_dir_path = input("enter songs dir path : ")
if song_dir_path == "":
    logging.critical("dir not provided")
    sys.exit(1)
files = os.listdir(song_dir_path)


def do_main_stuff():
    while len(files) != 0:
        file = files.pop()

        if Path(file).suffix != ".mp3":
            logging.info("other file extension")
            continue

        try:
            song_path = f"{song_dir_path}/{file}"
            collected = collector(song_path)

            response = uploader(
                data=collected[0], thumb_path=collected[1], audio_path=song_path
            )

            if response.status_code == 201:
                print("success")
            else:
                print(response.status_code)
                logging.warning(f"failed to upload {file} - {response.status_code}")

        except Exception as e:
            logging.warning(e)

for _ in range(40):
    Thread(target=do_main_stuff).start()
