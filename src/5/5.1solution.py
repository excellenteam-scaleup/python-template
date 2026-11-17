import datetime
import os
import random
import time


# ---------- 1.(This is the way) ----------
def files_starting_with_deep(path):
    """Return a list of all files in `path` whose names start with 'deep'."""
    return [
        name for name in os.listdir(path)
        if name.startswith('deep') and os.path.isfile(os.path.join(path, name))
    ]


# ---------- 2.(A strange card game) ----------
def create_deck():
    suits = ['Club', 'Diamond', 'Heart', 'Spade']
    return [(value, suit) for suit in suits for value in range(1, 14)]


def deal(deck, players=4):
    """Split the deck between the players (card i goes to player i % players)."""
    return [deck[i::players] for i in range(players)]


def strange_card_game():
    deck = create_deck()
    random.shuffle(deck)
    hands = deal(deck, 4)
    sums = [sum(value for value, suit in hand) for hand in hands]
    best = max(range(len(sums)), key=lambda i: sums[i])
    print(f"Sums of the hands: {sums}")
    print(f"Player {best + 1} has the highest sum: {sums[best]}")


# ---------- 3. It's the final? ----------
def days_until(date_string):
    """Get a future date in YYYY-MM-DD format and print/return the days left until it."""
    target = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    days_left = (target - datetime.date.today()).days
    print(days_left)
    return days_left


# ---------- 4. (I have no vinaigrette) ----------
def date_to_epoch(date_string):
    return time.mktime(time.strptime(date_string, '%Y-%m-%d'))


def random_date_between(first, second):
    start, end = sorted([date_to_epoch(first), date_to_epoch(second)])
    random_epoch = random.uniform(start, end)
    return datetime.date.fromtimestamp(random_epoch)


def vinaigrette():
    first = input("Enter the first date (YYYY-MM-DD): ")
    second = input("Enter the second date (YYYY-MM-DD): ")
    chosen = random_date_between(first, second)
    print(chosen.strftime('%Y-%m-%d'))
    if chosen.weekday() == 0:  # Monday == 0
        print("אין לי ויניגרט!")


if __name__ == '__main__':
    if os.path.isdir('images'):
        print(files_starting_with_deep('images'))
    strange_card_game()
    days_until('2026-12-31')
    vinaigrette()
