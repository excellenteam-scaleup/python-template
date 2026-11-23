"""Exercise 5.1: Generate a random date and check for Monday."""

import datetime
import random


def vinnigrete_no() -> None:
    """Generate a random date and print a message if it is Monday."""
    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")

    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

    timestamp1 = int(date1.timestamp())
    timestamp2 = int(date2.timestamp())

    random_time = random.randint(min(timestamp1, timestamp2),
                                 max(timestamp1, timestamp2))
    random_date = datetime.datetime.fromtimestamp(random_time)

    print("the chosen random date:", random_date.strftime("%Y-%m-%d"))
    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    vinnigrete_no()
