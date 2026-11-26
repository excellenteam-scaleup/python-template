
"""Create a dictionary of words and their lengths."""


def long_cat_is_long(text):
    """Return a dictionary containing word lengths."""
    clean_text = "".join(
        char for char in text.lower()
        if char.isalpha() or char.isspace()
    )

    return {word: len(word) for word in clean_text.split()}


if __name__ == "__main__":
    print(long_cat_is_long("Hello, Python is awesome!"))

    print(long_cat_is_long("You see, a very, very long cat."))

    print(long_cat_is_long(""))
