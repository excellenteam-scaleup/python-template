
"""Join multiple lists with a separator."""


def cup_of_join(*lists, sep="-"):
    """Return a combined list with separators."""
    if not lists:
        return None

    result = []

    for index, items in enumerate(lists):
        if index > 0:
            result.append(sep)

        result.extend(items)

    return result


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
