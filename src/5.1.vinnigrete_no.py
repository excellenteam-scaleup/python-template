
import datetime
import random


def vinnigrete_no():
    first_date = input("Enter first date (YYYY-MM-DD): ")
    second_date = input("Enter second date (YYYY-MM-DD): ")

    first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d").date()
    second_date = datetime.datetime.strptime(second_date, "%Y-%m-%d").date()

    start_day = min(first_date.toordinal(), second_date.toordinal())
    end_day = max(first_date.toordinal(), second_date.toordinal())

    random_day = random.randint(start_day, end_day)
    random_date = datetime.date.fromordinal(random_day)

    print("Random date:", random_date)

    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    vinnigrete_no()
