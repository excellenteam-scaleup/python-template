"""Module for interleaving elements from multiple iterables."""

from collections.abc import Iterable, Iterator
from typing import Any


def generator_interleaves(*iterables: Iterable[Any]) -> Iterator[Any]:
    """
    Yield elements from multiple iterables in an interleaved sequence.

    :param iterables: One or more iterables to interleave.
    :return: Generator yielding interleaved elements.
    """
    for group in zip(*iterables):
        yield from group


def interleaves(*iterables: Iterable[Any]) -> list[Any]:
    """
    Interleave elements from multiple iterables into a single list.

    :param iterables: One or more iterables to interleave.
    :return: A list of interleaved elements.
    """
    return list(generator_interleaves(*iterables))


# Aliases to support variations in naming
interleave = interleaves
interleave_gen = generator_interleaves


def main() -> None:
    """Demonstrate interleaves and generator_interleaves with sample inputs."""
    sample_result = interleaves("abc", [1, 2, 3], ("!", "@", "#"))
    print(f"List result: {sample_result}")

    gen_result = list(generator_interleaves("abc", [1, 2, 3], ("!", "@", "#")))
    print(f"Generator result: {gen_result}")


if __name__ == "__main__":
    main()
