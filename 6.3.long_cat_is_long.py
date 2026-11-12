import string


def count_words(text : str) -> dict:
    """ this function is getting a text and breaking it to words and their length using list comprehension"""

    text_list = text.lower().split()

    cleaned_words = ["".join(char for char in word if char.isalpha()) for word in text_list]

    return {word: len(word) for word in cleaned_words if word}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
