
def interleave(*iterables) -> list:
    """Interleave elements from multiple iterables into a list."""
    result = []
    iterators = [iter(iterable) for iterable in iterables]

    while iterators:
        remaining = []

        for iterator in iterators:
            try:
                result.append(next(iterator))
                remaining.append(iterator)
            except StopIteration:
                pass

        iterators = remaining

    return result


if __name__ == "__main__":
    print(interleave("abc", [1, 2, 3], ("!", "@", "#")))
    print(interleave("ab", [1, 2, 3, 4]))
    print(interleave())
