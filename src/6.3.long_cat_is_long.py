import string


def count_words(text):
    words = [
        "".join(char for char in word if char not in string.punctuation).lower()
        for word in text.split()
    ]

    result = {
        word: len(word)
        for word in words
        if word
    }

    return result


if __name__ == "__main__":
    print(count_words("Hello, Python!"))
    print(count_words("You see, wire telegraph is a kind of a very, very long cat."))