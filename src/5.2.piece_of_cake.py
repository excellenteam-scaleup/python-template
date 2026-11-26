"""Calculate the total price of a recipe."""


def piece_of_cake(prices, optionals=None, **quantities):
    """Return the total cost of the required ingredients."""
    if optionals is None:
        optionals = []

    total = 0

    for ingredient, price in prices.items():
        if ingredient not in optionals:
            total += price * quantities[ingredient] / 100

    return total


if __name__ == "__main__":
    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        chocolate=200,
        milk=100
    ))

    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        optionals=["milk"],
        chocolate=300
    ))

    print(piece_of_cake({}))
