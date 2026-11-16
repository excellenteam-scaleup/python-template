"""Module implementing a decorator that executes the wrapped function twice."""

from collections.abc import Callable
from typing import Any
from decorator import decorator


@decorator
def twice(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Execute the decorated function twice and return the second result.

    :param func: The function to execute twice.
    :param args: Positional arguments forwarded to func.
    :param kwargs: Keyword arguments forwarded to func.
    :return: The return value of the second function execution.
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)


@twice
def greet(name: str) -> str:
    """
    Print a greeting message and return it.

    :param name: Name of the person to greet.
    :return: Greeting message string.
    """
    message = f"Hello, {name}!"
    print(message)
    return message


def main() -> None:
    """Demonstrate the twice decorator."""
    result = greet("World")
    print("Returned value:", result)
    print("Function name preserved:", greet.__name__)


if __name__ == "__main__":
    main()
