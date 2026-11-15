import time


def timer(func, *args, **kwargs):
    start = time.perf_counter()

    func(*args, **kwargs)

    end = time.perf_counter()

    return end - start


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
    