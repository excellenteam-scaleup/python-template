"""Module for calculating the total price of recipe ingredients.
"""


def piece_of_cake(
    prices: dict[str, float],
    optionals: list[str] | None = None,
    **quantities: float,
) -> float:
    """Calculate total ingredient cost."""
    ignored = set(optionals) if optionals else set()
    total_price = 0.0

    for ingredient, price_per_100g in prices.items():
        if ingredient not in ignored:
            grams = quantities.get(ingredient, 0)
            total_price += (grams / 100) * price_per_100g

    return total_price


def main() -> None:
    """Read recipe ingredients, prices, optionals, and quantities."""
    prices: dict[str, float] = {}
    quantities: dict[str, float] = {}

    while True:
        ingredient = input("Enter ingredient name (empty to finish): ").strip()
        if not ingredient:
            break
        prices[ingredient] = float(input(f"Price per 100g for {ingredient}: "))
        quantities[ingredient] = float(input(f"Amount in grams for {ingredient}: "))

    optionals_input = input("Enter optional ingredients (or empty): ").strip()
    optionals = optionals_input.split() if optionals_input else None

    print(piece_of_cake(prices, optionals=optionals, **quantities))


if __name__ == "__main__":
    main()