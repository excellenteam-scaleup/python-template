
import time
from collections.abc import Callable
from typing import Any


def timer(f: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """Measure the execution time of a function in seconds."""
    start_time = time.perf_counter()

    f(*args, **kwargs)

    end_time = time.perf_counter()

    return end_time - start_time


if __name__ == "__main__":
    print("Test 1:")
    print(timer(print, "Hello"))

    print("Test 2:")
    print(timer(zip, [1, 2, 3], [4, 5, 6]))

    print("Test 3:")
    print(timer("Hi {name}".format, name="Bug"))
