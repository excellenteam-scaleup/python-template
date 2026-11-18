"""Pick a random date in a range and announce when it falls on a Monday."""

import calendar
import datetime as dt
import random as rnd

DATE_FORMAT = "%Y-%m-%d"
MONDAY_MSG = "אין לי ויניגרט!"


def random_date_between_dates(date_a_text: str, date_b_text: str):
    """Return a random date between two dates (inclusive).

    :param date_a_text: Start date in YYYY-MM-DD format
    :param date_b_text: End date in YYYY-MM-DD format
    :return: A random datetime between date_a and date_b
    """
    date_a = dt.datetime.strptime(date_a_text, DATE_FORMAT)
    date_b = dt.datetime.strptime(date_b_text, DATE_FORMAT)

    days = (date_b - date_a).days

    return date_a + dt.timedelta(days=rnd.randint(0, days))


def no_vinnigrete(date_a: str, date_b: str):
    """Print a random date between two dates, with a special message on Mondays.

    :param date_a: Start date in YYYY-MM-DD format
    :param date_b: End date in YYYY-MM-DD format
    """
    random_date = random_date_between_dates(date_a, date_b)
    print(random_date, end='')
    if random_date.weekday() == calendar.MONDAY:
        print('\t', MONDAY_MSG, end='')
    print()


if __name__ == '__main__':
    no_vinnigrete('2026-11-15', '2026-11-21')
