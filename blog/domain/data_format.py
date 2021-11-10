from datetime import datetime


def date_format(data):
    for entry in data:
        entry["date"] = datetime.strftime(entry["date"], "%Y-%m-%d")
    return data
