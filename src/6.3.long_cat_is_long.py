
def count_words(text: str) -> dict[str, int]:
    """Return a dictionary mapping each word to its length."""
    cleaned_text = "".join(
        char.lower() if char.isalpha() else " "
        for char in text
    )

    return {
        word: len(word)
        for word in cleaned_text.split()
    }


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here,
    they receive them there.
    The only difference is that there is no cat.
    """

    result = count_words(text)

    print(result)
    print("Total unique words:", len(result))
