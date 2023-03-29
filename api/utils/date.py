from datetime import datetime
import re


def get_datetime(date = None, format_: str = None) -> datetime:
    if date is None:
        return datetime.now()
    elif isinstance(date, str):
        format_ = format_ or "%d/%m/%Y"
        return datetime.strptime(date, format_)
    return date

def get_isoformat(date = None, format_: str = None):
    date: datetime = get_datetime(date, format_)
    return datetime.isoformat(date)

def format_all_datetime_to_iso(data: dict) -> dict:
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = get_isoformat(value)
        elif isinstance(value, dict):
            data[key] = format_all_datetime_to_iso(value)
    return data

def format_all_iso_to_datetime(data: dict) -> dict:
    for key, value in data.items():
        if isinstance(value, str):
            if re.match("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", value):
                data[key] = datetime.fromisoformat(value)
        elif isinstance(value, dict):
            data[key] = format_all_iso_to_datetime(value)
    return data
