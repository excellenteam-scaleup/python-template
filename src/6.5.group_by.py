
"""Group elements according to a given function."""


def group_by(func, iterable):
    """Return a dictionary of grouped elements."""
    result = {}

    for item in iterable:
        key = func(item)

        if key not in result:
            result[key] = []

        result[key].append(item)

    return result


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
    print(group_by(lambda x: x % 2, [1, 2, 3, 4, 5, 6]))
    print(group_by(len, []))
