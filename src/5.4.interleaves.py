
"""Interleave elements from multiple iterables."""


def generator_interleaves(*iterables):
    """Yield elements from the iterables alternately."""
    iterators = [iter(items) for items in iterables]

    while iterators:
        active = []

        for iterator in iterators:
            try:
                yield next(iterator)
                active.append(iterator)
            except StopIteration:
                continue

        iterators = active


def interleaves(*iterables):
    """Return a list of interleaved elements."""
    return list(generator_interleaves(*iterables))


if __name__ == "__main__":
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))

    print(list(generator_interleaves(
        "abc", [1, 2, 3], ("!", "@", "#")
    )))
