def get_recipe_price(prices, optionals=None, **ingredients):
    if optionals is None:
        optionals = []

    total = 0

    for ingredient, grams in ingredients.items():
        if ingredient in prices:
            total += prices[ingredient] * grams / 100
        elif ingredient not in optionals:
            raise ValueError(f"Missing price for {ingredient}")

    return total


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
