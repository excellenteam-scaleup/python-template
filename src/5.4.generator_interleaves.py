
from typing import Iterator


def generator_interleaves(*iterables) -> Iterator:
    """Yield interleaved elements from multiple iterables."""
    iterators = [iter(iterable) for iterable in iterables]

    while iterators:
        remaining = []

        for iterator in iterators:
            try:
                value = next(iterator)
            except StopIteration:
                continue

            yield value
            remaining.append(iterator)

        iterators = remaining


if __name__ == "__main__":
    print(list(generator_interleaves(
        "abc", [1, 2, 3], ("!", "@", "#")
    )))

    print(list(generator_interleaves(
        "ab", [1, 2, 3, 4]
    )))

    print(list(generator_interleaves()))
