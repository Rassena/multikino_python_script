import random
import string
from datetime import date, timedelta, time, datetime

from initializing_database.f2_0_constants import *


def random_string_generator(length) -> str:
    rand_signs = string.ascii_letters + string.digits
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_lowercase(length) -> str:
    rand_signs = string.ascii_lowercase
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_date_generator(year_start: int = DEFAULT_YEAR_START, year_end: int = DEFAULT_YEAR_END) -> date:
    start_date = date(year_start, 1, 1)
    end_date = date(year_end, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return random_date


def random_time_generator(hour_start: int = DEFAULT_HOUR_START, hour_end: int = DEFAULT_HOUR_END,
                          min_start: int = DEFAULT_MINUTE_START, min_end: int = DEFAULT_MINUTE_END) -> time:
    h = random.randrange(hour_start, hour_end)
    m = random.randrange(min_start, min_end, step=10)
    to_str = str(h) + ":" + str(m)
    t = datetime.strptime(to_str, "%H:%M")
    return t.time()
