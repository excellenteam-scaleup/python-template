"""Module for counting word lengths from cleaned text."""


def long_cat_is_long(text: str) -> dict[str, int]:
    """
    Count the length of each unique word in a given text after cleaning.

    Punctuation is removed, characters are lowercased, and words are mapped
    to their respective lengths using comprehensions.

    :param text: The input string containing words and punctuation.
    :return: A dictionary mapping each lowercase word to its length.
    """
    cleaned_characters = (
        char.lower() if char.isalpha() or char.isspace() else " "
        for char in text
    )
    cleaned_text = "".join(cleaned_characters)
    words = cleaned_text.split()

    return {word: len(word) for word in words}


# Alias to support notebook naming convention
count_words = long_cat_is_long


def main() -> None:
    """Demonstrate the long_cat_is_long function with sample text."""
    sample_text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    result = long_cat_is_long(sample_text)
    print("Word lengths dictionary:")
    print(result)


if __name__ == "__main__":
    main()
