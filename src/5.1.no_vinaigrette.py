import random
from datetime import datetime, timedelta


def no_vinaigrette():
    date1 = datetime.strptime(input("First date: "), "%Y-%m-%d")
    date2 = datetime.strptime(input("Second date: "), "%Y-%m-%d")

    if date1 > date2:
        date1, date2 = date2, date1

    days = (date2 - date1).days
    random_date = date1 + timedelta(days=random.randint(0, days))

    print(random_date.strftime("%Y-%m-%d"))

    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    no_vinaigrette()