"""Module implementing a decorator that replaces function execution with a surprise."""

from collections.abc import Callable
import functools
from typing import Any

SURPRISE_MESSAGE = "surprise!"


def surprise(func: Callable[..., Any]) -> Callable[..., None]:
    """
    Decorate a function so it prints 'surprise!' instead of its original behavior.

    :param func: The original function to be wrapped.
    :return: A wrapper function that prints the surprise message.
    """
    @functools.wraps(func)
    def wrapper(*_args: Any, **_kwargs: Any) -> None:
        print(SURPRISE_MESSAGE)

    return wrapper


@surprise
def add_numbers(first: int, second: int) -> int:
    """
    Add two numbers (functionality replaced by decorator).

    :param first: First integer.
    :param second: Second integer.
    :return: Sum of the two integers.
    """
    return first + second


def main() -> None:
    """Demonstrate the surprise decorator."""
    add_numbers(5, 10)
    print("Function name preserved:", add_numbers.__name__)


if __name__ == "__main__":
    main()
