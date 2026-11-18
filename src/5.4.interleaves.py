"""Module for interleaving one or more iterables into a list or generator.
the interleaves function can just use the generator, but the task said
to make a version of interleaves as a generator, and that's why I'm
keeping the double code.
"""

from collections.abc import Generator, Iterable


def interleaves(*iterables: Iterable[object]) -> list[object]:
    """
    Return a list with elements from all iterables interleaved.

    :param iterables: One or more iterable objects to interleave
    :return: A single list containing elements interleaved in order
    """
    result: list[object] = []
    iterators = [iter(item) for item in iterables]

    while iterators:
        active_iterators = []
        for iterator in iterators:
            try:
                result.append(next(iterator))
                active_iterators.append(iterator)
            except StopIteration:
                pass
        iterators = active_iterators

    return result


def generator_interleaves(
    *iterables: Iterable[object],
) -> Generator[object, None, None]:
    """Yield elements from all iterables interleaved one by one."""
    iterators = [iter(item) for item in iterables]

    while iterators:
        active_iterators = []
        for iterator in iterators:
            try:
                yield next(iterator)
                active_iterators.append(iterator)
            except StopIteration:
                pass
        iterators = active_iterators


def main() -> None:
    """Read sequences from user input and print interleaved results."""
    user_lists: list[list[str]] = []

    while line := input(
        "Enter items of list (empty to finish): "
    ).strip():
        user_lists.append(line.split())

    print(interleaves(*user_lists))
    print(list(generator_interleaves(*user_lists)))


if __name__ == "__main__":
    main()