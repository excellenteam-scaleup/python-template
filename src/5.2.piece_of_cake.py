"""Calculate the total price of ingredients for a recipe."""


def get_recipe_price(
    prices: dict[str, float],
    optionals: list[str] | None = None,
    **kwargs: float
) -> float:
    """Calculate recipe cost, excluding optional ingredients."""
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient in prices:
        if ingredient not in optionals:
            price = prices[ingredient]
            amount = kwargs[ingredient]
            total_price += price * amount / 100

    return total_price


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8},
                           chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8},
                           optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
