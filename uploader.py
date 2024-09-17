import requests, json
from requests import Response

url = "http://localhost:5000/api/track"


def uploader(data: dict, thumb_path: str, audio_path: str) -> Response:
    files = {
        "trackFile": open(audio_path, "rb"),
        "thumbnail": open(thumb_path, "rb") if thumb_path is not None else None,
    }

    return requests.request("POST", url=url, data=data, files=files, timeout=30)
