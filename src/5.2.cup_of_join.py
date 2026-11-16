"""Module for joining multiple lists with a separator element."""

from typing import Any

DEFAULT_SEP = "-"


def cup_of_join(*lists: list[Any], sep: Any = DEFAULT_SEP) -> list[Any] | None:
    """
    Join multiple lists into a single flat list with a separator between them.

    :param lists: Variable number of lists to concatenate.
    :param sep: Separator element placed between adjacent lists (default: '-').
    :return: A single flattened list with separators, or None if no lists were passed.
    """
    if not lists:
        return None

    result: list[Any] = []
    for index, current_list in enumerate(lists):
        result.extend(current_list)
        if index < len(lists) - 1:
            result.append(sep)

    return result


# Alias to support notebook naming convention
join = cup_of_join


def main() -> None:
    """Demonstrate the cup_of_join function with various inputs."""
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())


if __name__ == "__main__":
    main()
