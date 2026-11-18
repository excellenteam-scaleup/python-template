def get_recipe_price(prices, optionals=None, **ingredients):
    if optionals is None:
        optionals = []

    total = 0

    for ingredient, grams in ingredients.items():
        if ingredient not in optionals:
            total += prices[ingredient] * grams / 100

    return total


if __name__ == "__main__":
    prices = {
        "flour": 2,
        "sugar": 3,
        "butter": 8
    }

    print(get_recipe_price(
        prices,
        optionals=["butter"],
        flour=200,
        sugar=50,
        butter=100
    ))