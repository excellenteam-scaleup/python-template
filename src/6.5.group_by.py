
from collections.abc import Callable, Iterable
from typing import Any


def group_by(
    function: Callable[[Any], Any],
    iterable: Iterable[Any]
) -> dict[Any, list[Any]]:
    """Group items by the result of applying function to each item."""
    groups = {}

    for item in iterable:
        key = function(item)

        if key not in groups:
            groups[key] = []

        groups[key].append(item)

    return groups


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))

    print(group_by(
        lambda number: number % 2,
        [1, 2, 3, 4, 5, 6]
    ))

    print(group_by(str.lower, ["Apple", "APPLE", "Banana", "BANANA"]))

    print(group_by(len, []))
