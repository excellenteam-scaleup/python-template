
"""Generate a random date between two dates."""

import random
from datetime import date, timedelta


def no_vinnigrete(start_date, end_date):
    """Return a random date between two given dates."""
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    days = (end - start).days
    random_days = random.randint(0, days)

    return start + timedelta(days=random_days)


if __name__ == "__main__":
    first = input("Enter first date (YYYY-MM-DD): ")
    second = input("Enter second date (YYYY-MM-DD): ")

    result = no_vinnigrete(first, second)
    print(result)

    if result.weekday() == 0:
        print("I don't have any vinaigrette!")
