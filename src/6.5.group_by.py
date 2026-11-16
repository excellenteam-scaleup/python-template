"""Module for grouping iterable elements by the result of a key function."""

from collections import defaultdict
from collections.abc import Callable, Iterable
from typing import Any


def group_by(
    target_function: Callable[[Any], Any], iterable: Iterable[Any]
) -> dict[Any, list[Any]]:
    """
    Group elements of an iterable based on a key function.

    :param target_function: Function applied to each element to generate group keys.
    :param iterable: Collection of elements to group.
    :return: Dictionary mapping group keys to lists of elements.
    """
    grouped_elements: defaultdict[Any, list[Any]] = defaultdict(list)

    for item in iterable:
        key = target_function(item)
        grouped_elements[key].append(item)

    return dict(grouped_elements)


def main() -> None:
    """Demonstrate group_by with sample string lengths."""
    sample_data = ["hi", "bye", "yo", "try"]
    result = group_by(len, sample_data)
    print("Grouped result:", result)


if __name__ == "__main__":
    main()
