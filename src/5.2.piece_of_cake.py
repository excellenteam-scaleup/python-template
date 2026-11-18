"""Calculate the price of a cake from its ingredients."""

PRICE_RATIO = 1 / 100


def piece_of_cake(prices, optionals: list = None, **ingredients):
    """Calculate the total price of a cake.

    Prices are given per 100 grams; optional ingredients are not charged.

    :param prices: Dict mapping ingredient name to its price per 100 grams
    :param optionals: List of ingredient names that should not be charged
    :param ingredients: Ingredient names mapped to their amount in grams
    :return: The total price of the cake
    """
    if not optionals:
        optionals = []
    price = 0

    for ingredient, count in ingredients.items():
        if ingredient in optionals:
            continue
        price += prices[ingredient] * (count * PRICE_RATIO)

    return price


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, ['milk'], chocolate=300))
    print(piece_of_cake({}))
