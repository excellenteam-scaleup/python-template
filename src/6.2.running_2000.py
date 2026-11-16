"""Module for measuring the execution time of a given function."""

from collections.abc import Callable
import time
from typing import Any


def running_2000(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Measure and return the execution duration of a function with given arguments.

    :param func: The callable function to execute and measure.
    :param args: Positional arguments to forward to func.
    :param kwargs: Keyword arguments to forward to func.
    :return: Total execution time in seconds as a float.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


# Alias to support notebook naming convention
timer = running_2000


def main() -> None:
    """Demonstrate measuring execution duration for various functions."""
    duration_print = running_2000(print, "Hello")
    print(f"print execution time: {duration_print:.6f} seconds")

    duration_zip = running_2000(zip, [1, 2, 3], [4, 5, 6])
    print(f"zip execution time: {duration_zip:.6f} seconds")

    duration_format = running_2000(
        "Hi {name}".format, name="Bug"  # pylint: disable=consider-using-f-string
    )
    print(f"format execution time: {duration_format:.6f} seconds")


if __name__ == "__main__":
    main()
