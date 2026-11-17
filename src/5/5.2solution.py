def avg(*numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def join(*lists, sep='-'):
    if len(lists) == 0:
        return None
    result = list(lists[0])
    for current_list in lists[1:]:
        result.append(sep)
        result.extend(current_list)
    return result


def get_recipe_price(prices, optionals=None, **amounts):
    if optionals is None:
        optionals = []
    total = 0
    for ingredient, price in prices.items():
        if ingredient in optionals:
            continue
        grams = amounts.get(ingredient, 0)
        total = total + price * grams / 100
    return total


print(avg(5, 6))
print(avg(10, 5, 3))
print(avg(2))
print(avg())

print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())

print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
