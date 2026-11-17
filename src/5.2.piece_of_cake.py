PRICE_RATIO = 1/100

def piece_of_cake(prices, optionals:list = None, **ingredients):
    if not optionals:
        optionals = []
    price = 0

    for ingredient in ingredients:
        if ingredient in optionals:
            continue
        price += prices[ingredient] * (ingredients[ingredient] * PRICE_RATIO)

    return price

if __name__ == '__main__':
    print (piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print (piece_of_cake({'chocolate': 18, 'milk': 8}, ['milk'], chocolate=300))
    print (piece_of_cake({}))