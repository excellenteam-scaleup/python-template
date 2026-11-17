import datetime
import html
import os
import random
import re


def create_deck():
    suits = ['Club', 'Diamond', 'Heart', 'Spade']
    return [(value, suit) for suit in suits for value in range(1, 14)]


def play_war(max_rounds=10000):
    deck = create_deck()
    random.shuffle(deck)
    player1 = deck[::2]
    player2 = deck[1::2]
    rounds = 0
    while player1 and player2 and rounds < max_rounds:
        rounds = rounds + 1
        table = []
        while True:
            if not player1 or not player2:
                break
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            table.extend([card1, card2])
            if card1[0] > card2[0]:
                random.shuffle(table)
                player1.extend(table)
                break
            if card2[0] > card1[0]:
                random.shuffle(table)
                player2.extend(table)
                break
            for _ in range(3):
                if len(player1) > 1 and len(player2) > 1:
                    table.append(player1.pop(0))
                    table.append(player2.pop(0))
    print(f"Game ended after {rounds} rounds")
    if len(player1) > len(player2):
        print(f"Player 1 wins with {len(player1)} cards")
    elif len(player2) > len(player1):
        print(f"Player 2 wins with {len(player2)} cards")
    else:
        print("It's a tie")


def interleave(*iterables):
    result = []
    for group in zip(*iterables):
        result.extend(group)
    return result


def interleave_generator(*iterables):
    for group in zip(*iterables):
        for item in group:
            yield item


def add_inventory(inventory, **delivery):
    for product, amount in delivery.items():
        inventory[product] = inventory.get(product, 0) + amount
    return inventory


def clean_file_name(name):
    for bad_char in '\\/:*?"<>|':
        name = name.replace(bad_char, '')
    return ' '.join(name.split()).strip('. ')


def find_chapter(path):
    with open(path, encoding='utf-8', errors='ignore') as file:
        content = html.unescape(file.read())
    match = re.search(r'Chapter\s+(\d+)\s*[:\-]\s*([^<\n]+)', content)
    if match is None:
        return None
    return int(match.group(1)), clean_file_name(match.group(2))


def rename_chapters(folder):
    used_names = set()
    for file_name in sorted(os.listdir(folder)):
        old_path = os.path.join(folder, file_name)
        if not os.path.isfile(old_path):
            continue
        chapter = find_chapter(old_path)
        if chapter is None:
            print(f"Could not find a chapter in {file_name}")
            continue
        number, title = chapter
        extension = os.path.splitext(file_name)[1]
        new_name = f"{number:03} {title}{extension}"
        if new_name in used_names:
            print(f"Duplicate chapter {number}, skipping {file_name}")
            continue
        used_names.add(new_name)
        os.rename(old_path, os.path.join(folder, new_name))
        print(f"{file_name} -> {new_name}")


def all_birthdays():
    birthdays = []
    day = datetime.date(2020, 1, 1)
    while day < datetime.date(2024, 1, 1):
        birthdays.append((day.month, day.day))
        day = day + datetime.timedelta(days=1)
    return birthdays


BIRTHDAYS = all_birthdays()


def class_has_shared_birthday(students):
    seen = set()
    for _ in range(students):
        birthday = random.choice(BIRTHDAYS)
        if birthday in seen:
            return True
        seen.add(birthday)
    return False


def shared_birthday_percent(students, classes=10000):
    count = 0
    for _ in range(classes):
        if class_has_shared_birthday(students):
            count = count + 1
    return count / classes * 100


play_war()

print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
print(list(interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))))

print(add_inventory({'cheese': 2, 'milk': 1}, cheese=3, chocolate=5))
print(add_inventory({'refrigerator': 7, 'goat': 1}, honey=2))

if os.path.isdir('resources/hpmor'):
    rename_chapters('resources/hpmor')

print(f"23 students: {shared_birthday_percent(23):.2f}%")
for students in range(1, 367):
    print(f"{students} students: {shared_birthday_percent(students):.2f}%")
