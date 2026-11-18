"""Module for picking a random date between 2 user given dates.
"""

from datetime import datetime, timedelta
import random


def no_vinnigrete(date1: str, date2: str) -> None:
    """Pick a date between date1 and date2."""
    first_date = datetime.strptime(date1, "%Y-%m-%d")
    second_date = datetime.strptime(date2, "%Y-%m-%d")

    start_date = min(first_date, second_date)
    end_date = max(first_date, second_date)
    delta_days = (end_date - start_date).days

    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)

    print(f"Picked date: {random_date.strftime('%Y-%m-%d')}")

    if random_date.weekday() == 0:
        print("no vinnigrete")


def main() -> None:
    """Asking user for two dates and run no_vinnigrete."""
    first_input = input("Enter first date (YYYY-MM-DD): ").strip()
    second_input = input("Enter second date (YYYY-MM-DD): ").strip()

    no_vinnigrete(first_input, second_input)


if __name__ == "__main__":
    main()