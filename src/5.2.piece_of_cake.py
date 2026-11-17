
def get_recipe_price(
    prices: dict[str, float],
    optionals: list[str] | None = None,
    **ingredients: float
) -> float:
    """Calculate the total price of recipe ingredients."""
    if optionals is None:
        optionals = []

    total_price = 0.0

    for ingredient, price_per_100g in prices.items():
        if ingredient in optionals:
            continue

        quantity = ingredients[ingredient]
        total_price += price_per_100g * quantity / 100

    return total_price


if __name__ == "__main__":
    print(get_recipe_price(
        {"chocolate": 18, "milk": 8},
        chocolate=200,
        milk=100
    ))

    print(get_recipe_price(
        {"chocolate": 18, "milk": 8},
        optionals=["milk"],
        chocolate=300
    ))

    print(get_recipe_price({}))
