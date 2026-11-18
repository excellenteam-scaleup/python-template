"""Module for grouping items from an iterable by a key generating function.
"""

from collections.abc import Callable, Iterable
from typing import TypeVar

ItemT = TypeVar("ItemT")
KeyT = TypeVar("KeyT")


def group_by(
    key_func: Callable[[ItemT], KeyT], items: Iterable[ItemT]
) -> dict[KeyT, list[ItemT]]:
    """Group items into a dictionary with their keys as the return values."""
    grouped: dict[KeyT, list[ItemT]] = {}
    for item in items:
        key = key_func(item)
        grouped.setdefault(key, []).append(item)
    return grouped


def main() -> None:
    """Read user input and to test the len function as in the example."""
    words = input("Enter words: ").split()
    print(group_by(len, words))


if __name__ == "__main__":
    main()