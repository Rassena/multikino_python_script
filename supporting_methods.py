import random
import string
from datetime import date, timedelta, time


def random_string_generator(length) -> str:
    rand_signs = string.ascii_letters + string.digits
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_lowercase(length) -> str:
    rand_signs = string.ascii_lowercase
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_date_generator() -> date:
    start_date = date(2021, 1, 1)
    end_date = date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return random_date


def random_time_generator() -> time:
    pass


class ObjectWithCounter:
    counter = 0

    @classmethod
    def next(cls):
        counter_val = cls.counter
        cls.counter += 1
        return counter_val


class AddableToDatabase:
    @property
    def sql_addable(self):
        """
        example: "INSERT INTO ClassName (Atr_1, Atr_2) VALUES (%(Atr_1)s, %(Atr_2)s)"
        """
        keys = ', '.join(self.__dict__.keys())
        keys_insertable = ', '.join([f'%({key})s' for key in self.__dict__.keys()])
        return f'INSERT INTO {self.__class__.__name__} ({keys}) VALUES ({keys_insertable})'

    def __str__(self):
        keys, values = '', ''
        if len(self.__dict__) > 0:
            keys = ', '.join(self.__dict__.keys())
            values = ', '.join([str(value) for value in self.__dict__.values()])
        return f'{self.__class__.__name__} ({keys}) : ({values})'
