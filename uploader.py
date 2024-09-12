import requests, json
from requests import Response

url = "http://localhost:5000/song/song"


def uploader(data: dict, thumb_path: str, audio_path: str) -> Response:
    files = {
        "songFile": open(audio_path, "rb"),
    }

    if thumb_path is not None:
        files["thumbnailFile"] = open(thumb_path, "rb")

    return requests.post(url=url, data=data, files=files, stream=True)
