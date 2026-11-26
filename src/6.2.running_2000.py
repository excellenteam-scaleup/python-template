
"""Measure the execution time of a function."""

from time import perf_counter


def running_2000(func, *args, **kwargs):
    """Return the time needed to execute a function."""
    start_time = perf_counter()

    func(*args, **kwargs)

    end_time = perf_counter()

    return end_time - start_time


if __name__ == "__main__":
    print("Test 1:")
    print(running_2000(print, "Hello"))

    print("Test 2:")
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))

    print("Test 3:")
    print(running_2000(lambda name: f"Hi {name}", name="Bug"))
