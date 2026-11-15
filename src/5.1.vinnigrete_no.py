from datetime import datetime, timedelta


def vinnigrete_no(date1, date2):
    first_date = datetime.strptime(date1, "%Y-%m-%d")
    second_date = datetime.strptime(date2, "%Y-%m-%d")

    middle_date = first_date + (second_date - first_date) / 2

    print(middle_date.strftime("%Y-%m-%d"))

    if middle_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    vinnigrete_no("1912-06-23", "1954-06-07")
