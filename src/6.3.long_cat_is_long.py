TEST_TEXT = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
"""

def long_cat_is_long(text):
    clean_text = ''.join(char if char.isalpha() else ' ' for char in text)

    words = clean_text.split()

    return {word: len(word) for word in words}

if __name__ == '__main__':
    print(long_cat_is_long("Hello-World"))
