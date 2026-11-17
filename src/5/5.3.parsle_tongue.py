def get_check_digit(id_without_check):
    id_string = str(id_without_check).zfill(8)
    total = 0
    for index, digit in enumerate(id_string):
        number = int(digit) * (index % 2 + 1)
        if number > 9:
            number = number - 9
        total = total + number
    return (10 - total % 10) % 10


def all_ids():
    for number in range(100000000):
        id_string = str(number).zfill(8)
        yield id_string + str(get_check_digit(id_string))


def print_all_ids():
    for id_number in all_ids():
        print(id_number)


def sum_of_divisors(number):
    total = 0
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            total = total + divisor
    return total


def perfect_portions():
    number = 2
    while True:
        if sum_of_divisors(number) == number:
            yield number
        number = number + 1


def print_perfect_portions():
    for portion in perfect_portions():
        print(portion)


def read_bytes(path, chunk_size=1024):
    with open(path, 'rb') as file:
        chunk = file.read(chunk_size)
        while chunk:
            for byte in chunk:
                yield byte
            chunk = file.read(chunk_size)


def find_secret_messages(path):
    current = ''
    for byte in read_bytes(path):
        letter = chr(byte)
        if 'a' <= letter <= 'z':
            current = current + letter
        elif letter == '!' and len(current) >= 5:
            yield current + '!'
            current = ''
        else:
            current = ''


print(get_check_digit('12345678'))

for portion in perfect_portions():
    print(portion)
    if portion > 1000:
        break

for message in find_secret_messages('resources/logo.jpg'):
    print(message)
