# piece_of_cake




def get_recipe_price(prices: dict, optionals: list | None = None, **ingredients_amounts) -> float:
    """calcs the total cost of a recipe based on prices per 100g and required amounts"""
    if optionals is None:
        optionals = []

    total_price = 0
    for ingredient, price_per_100g in prices.items():
        #skiping optional
        if ingredient in optionals:
            continue

        amount_in_grams = ingredients_amounts.get(ingredient, 0)
        total_price += (amount_in_grams / 100) * price_per_100g

    return total_price



if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))