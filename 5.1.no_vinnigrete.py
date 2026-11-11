# no vinigrete


import datetime as dt
import random


def get_date() -> dt.date | None:
    user_input = input("insert date in format YYYY-MM-DD: ")
    try:
        valid_date = dt.date.fromisoformat(user_input)
        print("valid date:", valid_date)
        return valid_date
    except ValueError:
        print("Format not allowed or date does not exist.")
        return None


def no_vinnigrete(date_one : dt.date, date_two : dt.date) -> dt.date:
    dt_one = dt.datetime.combine(date_one, dt.time.min)
    dt_two = dt.datetime.combine(date_two, dt.time.min)

    st_epoch = int(dt_one.timestamp())
    end_epoch = int(dt_two.timestamp())

    if st_epoch > end_epoch:
        st_epoch, end_epoch = end_epoch, st_epoch

    random_epoch = random.randint(st_epoch, end_epoch)

    return dt.datetime.fromtimestamp(random_epoch)


if __name__ == '__main__':
    date_one = get_date()
    date_two = get_date()

    if date_one is not None and date_two is not None:
        rnd_date = no_vinnigrete(date_one, date_two)
        print("Random date:", rnd_date)

        if rnd_date.weekday() == 0:
            print("אין לי ויניגרט!")
    else:
        print("cannot generate random date because one of the inputs was invalid.")