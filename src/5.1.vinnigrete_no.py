import datetime as dt
import random as rnd
import calendar

DATE_FORMAT = "%Y-%m-%d"
MONDAY_MSG = "אין לי ויניגרט!"

def random_date_between_dates(date_a:str, date_b:str):
    date_a = dt.datetime.strptime(date_a, DATE_FORMAT)
    date_b = dt.datetime.strptime(date_b, DATE_FORMAT)

    days = (date_b - date_a).days

    return date_a + dt.timedelta(days=rnd.randint(0,days))

def vinnigrete_no(date_a:str, date_b:str):
    random_date = random_date_between_dates(date_a, date_b)
    print(random_date, end='')
    if random_date.weekday() == calendar.MONDAY:
        print('\t',MONDAY_MSG, end='')
    print()


if __name__ == '__main__':
    vinnigrete_no('2026-11-15','2026-11-21')