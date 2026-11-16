"""Module implementing a type-checking decorator factory."""

from collections.abc import Callable
import functools
from typing import Any


class InvalidTypeError(TypeError):
    """Raised when an argument passed to a decorated function has the wrong type."""


def type_check(
    expected_type: type,
) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
    """
    Create a decorator that validates the type of a single-argument function.

    :param expected_type: The expected Python type for the function argument.
    :return: A decorator function that enforces the type check.
    """
    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @functools.wraps(func)
        def wrapper(arg: Any) -> Any:
            if not isinstance(arg, expected_type):
                raise InvalidTypeError(
                    f"Expected argument of type {expected_type.__name__}, "
                    f"got {type(arg).__name__} instead."
                )
            return func(arg)

        return wrapper

    return decorator


@type_check(int)
def times_two(num: int) -> int:
    """
    Multiply an integer by two.

    :param num: An integer value.
    :return: The value multiplied by two.
    """
    return num * 2


def main() -> None:
    """Demonstrate the type_check decorator factory."""
    print("Valid call (times_two(2)):", times_two(2))
    print("Function name preserved:", times_two.__name__)

    try:
        times_two("not an int")  # type: ignore[arg-type]
    except InvalidTypeError as error:
        print(f"Caught expected error: {error}")


if __name__ == "__main__":
    main()
