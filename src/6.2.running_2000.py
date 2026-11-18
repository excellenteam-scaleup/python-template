"""Module for measuring the execution time of function calls.
"""

from collections.abc import Callable
import time


def running_2000(
    func: Callable[..., object],
    *args: object,
    **kwargs: object,
) -> float:
    """Measure the execution duration of func(*args, **kwargs)."""
    start_time = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start_time


def main() -> None:
    """Demonstrate function with sample function calls."""
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main()