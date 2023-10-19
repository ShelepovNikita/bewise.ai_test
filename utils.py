"""Utils for Flask app."""
import datetime
import json
import requests

from constants import URL_WITH_QUESTIONS


def get_questions_json(num: int):
    """Function sends a request to the site with questions
    and return response with json formatting."""
    response = requests.get(f'{URL_WITH_QUESTIONS}?count={num}')
    return json.loads(response.text)


def to_python_datetime(db_datetime: str):
    """Сonversion to format python datetime."""
    datetime_str = db_datetime.split('T')
    date = datetime_str[0].split('-')
    time = datetime_str[1].split(':')
    return datetime.datetime(int(date[0]), int(date[1]), int(date[2]),
                             int(time[0]), int(time[1]),
                             int(time[2].split('.')[0]))
