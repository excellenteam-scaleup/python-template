from faker import Faker
from PIL import Image


# Animal: pandas, mammoth
# Number: six
# Mythological creature: python (the giant serpent from Greek mythology)
# six - helps write code that works on both Python 2 and Python 3.


def create_people(n):
    fake = Faker()
    people = []
    for _ in range(n):
        person = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'phone': fake.phone_number(),
        }
        people.append(person)
    return people


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


for person in create_people(3):
    print(person)

print(decode_message('resources/code.png'))
