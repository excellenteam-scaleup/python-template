"""Module for generating a random date between two given dates."""

from datetime import datetime, timedelta
import random

DATE_FORMAT = "%Y-%m-%d"
MONDAY_WEEKDAY = 0
VINNIGRETE_MESSAGE = "אין לי ויניגרט!"


def no_vinnigrete(date_start_str: str, date_end_str: str) -> str:
    """
    Generate and print a random date between two given dates.

    The dates can be provided in any order. If the randomly selected date
    falls on a Monday, an additional message is printed.

    :param date_start_str: First date in YYYY-MM-DD format.
    :param date_end_str: Second date in YYYY-MM-DD format.
    :return: The generated date formatted as a string (YYYY-MM-DD).
    :raises ValueError: If either date format is invalid.
    """
    try:
        first_date = datetime.strptime(date_start_str, DATE_FORMAT).date()
        second_date = datetime.strptime(date_end_str, DATE_FORMAT).date()
    except ValueError as error:
        raise ValueError(
            f"Invalid date format. Expected '{DATE_FORMAT}'."
        ) from error

    start_date = min(first_date, second_date)
    end_date = max(first_date, second_date)

    total_days = (end_date - start_date).days
    random_days = random.randint(0, total_days)
    selected_date = start_date + timedelta(days=random_days)

    selected_date_str = selected_date.strftime(DATE_FORMAT)
    print(selected_date_str)

    if selected_date.weekday() == MONDAY_WEEKDAY:
        print(VINNIGRETE_MESSAGE)

    return selected_date_str


def main() -> None:
    """Demonstrate the no_vinnigrete function with sample dates."""
    first_date = "1912-06-23"
    second_date = "1954-06-07"
    no_vinnigrete(first_date, second_date)


if __name__ == "__main__":
    main()
