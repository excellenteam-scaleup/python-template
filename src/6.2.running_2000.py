"""Measure how long a function call takes to run."""

from time import perf_counter


def running_2000(func, *args, **kwargs):
    """Run a function once and measure its execution time.

    :param func: The function to run
    :param args: Positional arguments passed to func
    :param kwargs: Keyword arguments passed to func
    :return: Elapsed time of the call in seconds (float)
    """
    start = perf_counter()
    func(*args, **kwargs)
    return perf_counter() - start


if __name__ == '__main__':
    for j in range(9):
        print(running_2000(lambda x: [i ** 5 for i in range(x)], 10 ** j))
