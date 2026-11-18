from datetime import datetime


def vinnigrete_no(date1: str, date2: str) -> str:
    """Return the middle date between two dates."""
    first_date = datetime.strptime(date1, "%Y-%m-%d")
    second_date = datetime.strptime(date2, "%Y-%m-%d")

    middle_date = first_date + (second_date - first_date) / 2

    if middle_date.weekday() == 0:
        print("אין לי ויניגרט!")

    return middle_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(vinnigrete_no("1912-06-23", "1954-06-07"))
