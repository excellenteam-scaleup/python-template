import time

def timer(func, *args, **kwargs) -> float:
    """ this function calcs the time that it takes to take the function inside to run"""

    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    time_passed = end - start

    return time_passed


if __name__ == '__main__':
    print("Time for print:", timer(print, "Hello"))

    print("Time for zip:", timer(zip, [1, 2, 3], [4, 5, 6]))

    print("Time for format:", timer("Hi {name}".format, name="Bug"))
