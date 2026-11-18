"""Module for mapping words in text to their lengths.
"""


def long_cat_is_long(text: str) -> dict[str, int]:
    """Return a dictionary mapping each word to its length."""
    cleaned_text = "".join(
        char.lower() if char.isalpha() else " " for char in text
    )
    return {word: len(word) for word in cleaned_text.split()}


def main() -> None:
    """Read text from user input and print the word-length dictionary."""
    user_text = input("Enter text: ")
    print(long_cat_is_long(user_text))


if __name__ == "__main__":
    main()