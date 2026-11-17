import itertools
import random
from operator import add

from PIL import Image


def group_by(function, iterable):
    groups = {}
    for item in iterable:
        key = function(item)
        groups.setdefault(key, []).append(item)
    return groups


def zip_with(function, *iterables):
    return [function(*items) for items in zip(*iterables)]


def encode_message(message, path):
    image = Image.new('RGB', (len(message), 256), 'white')
    for x, char in enumerate(message):
        image.putpixel((x, ord(char)), (0, 0, 0))
    image.save(path)


def decode_message(path):
    image = Image.open(path).convert('RGB')
    width, height = image.size
    message = ''
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) == (0, 0, 0):
                message = message + chr(y)
                break
    return message


NUMBERS = [1, 2, 3]
COLORS = ['red', 'green', 'purple']
SHAPES = ['diamond', 'squiggle', 'oval']
SHADINGS = ['solid', 'striped', 'open']


def create_set_deck():
    return list(itertools.product(NUMBERS, COLORS, SHAPES, SHADINGS))


def is_set(card1, card2, card3):
    for feature in zip(card1, card2, card3):
        if len(set(feature)) == 2:
            return False
    return True


def find_sets(cards):
    return [combo for combo in itertools.combinations(cards, 3) if is_set(*combo)]


def deal_cards(count=12):
    deck = create_set_deck()
    random.shuffle(deck)
    return deck[:count]


def percent_without_set(tries=10000):
    no_set = 0
    for _ in range(tries):
        if not find_sets(deal_cards()):
            no_set = no_set + 1
    return no_set / tries * 100


print(group_by(len, ["hi", "bye", "yo", "try"]))

print(zip_with(add, [1, 2, 3], [4, 5, 6]))
print(zip_with(max, (5, 4), (2, 5), (6, -6)))

encode_message("Remember remember the fifth of November", "secret.png")
print(decode_message("secret.png"))

table = deal_cards()
print(f"Deck size: {len(create_set_deck())}")
for card in table:
    print(card)
print("Sets on the table:")
for found_set in find_sets(table):
    print(found_set)
print(f"No set in {percent_without_set():.2f}% of the deals")
