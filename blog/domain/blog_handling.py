from datetime import datetime
from babel.dates import format_date


def date_format(data):
    for entry in data:
        formated_date = format_date(entry["date"], locale="en_US")
        year = formated_date[-4:]
        month = formated_date[:3].upper()
        day = formated_date.split(",")[0].split()[1]
        entry["date"] = f"{year} {month} {day}"
    return data
