from music_tag import load_file
import re


def collector(file_path) -> tuple[dict, str]:
    pattern = r"-?\s*\S+\.\S+"
    file = load_file(file_path)
    collectd = {}

    collectd["title"] = re.sub(
        pattern=pattern, repl="", string=file["tracktitle"].value
    ).strip()
    collectd["artist"] = re.sub(
        pattern=pattern, repl="", string=file["artist"].value
    ).strip()
    collectd["album"] = re.sub(
        pattern=pattern, repl="", string=file["album"].value
    ).strip()
    collectd["year"] = file["year"].value

    art = file["artwork"]

    if art.first is not None:

        art_data = art.first.thumbnail([1024, 1024])

        thumb_path = f"temp/{collectd['title']}.jpg"

        art_data.save(thumb_path)
    else:
        thumb_path = None

    return collectd, thumb_path
