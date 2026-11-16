"""Module for calculating total recipe price based on ingredients."""

BASE_WEIGHT_GRAMS = 100


def piece_of_cake(
    prices: dict[str, int | float],
    optionals: list[str] | None = None,
    **ingredients: int | float,
) -> int | float:
    """
    Calculate the total price of a recipe based on ingredients weight.

    :param prices: Dictionary mapping ingredient names to price per 100 grams.
    :param optionals: Optional list of ingredient names to ignore.
    :param ingredients: Keyword arguments mapping ingredient names to amount in grams.
    :return: The total calculated price.
    """
    ignored_ingredients = set(optionals) if optionals is not None else set()
    total_cost: float = 0.0

    for ingredient_name, amount_in_grams in ingredients.items():
        if ingredient_name in ignored_ingredients:
            continue

        if ingredient_name in prices:
            unit_price = prices[ingredient_name]
            total_cost += (amount_in_grams / BASE_WEIGHT_GRAMS) * unit_price

    if int(total_cost) == total_cost:
        return int(total_cost)
    return total_cost


# Alias to support notebook naming convention
get_recipe_price = piece_of_cake


def main() -> None:
    """Demonstrate the piece_of_cake function with sample recipes."""
    sample_prices = {"chocolate": 18, "milk": 8}

    cost_1 = piece_of_cake(sample_prices, chocolate=200, milk=100)
    print(f"Cost 1 (expected 44): {cost_1}")

    cost_2 = piece_of_cake(sample_prices, optionals=["milk"], chocolate=300)
    print(f"Cost 2 (expected 54): {cost_2}")

    cost_3 = piece_of_cake({})
    print(f"Cost 3 (expected 0): {cost_3}")


if __name__ == "__main__":
    main()
