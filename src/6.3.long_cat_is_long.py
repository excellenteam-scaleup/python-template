def count_words(text):
    cleaned = "".join(
        char.lower() if char.isalpha() else " "
        for char in text
    )

    return {word: len(word) for word in cleaned.split()}


if __name__ == "__main__":
    text = "Hello, World! Python123 is AMAZING!"

    print(count_words(text))