import time


def timer(func, *args, **kwargs):
    start = time.perf_counter()

    func(*args, **kwargs)

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    def calculate(n):
        return sum(range(n))

    print(timer(calculate, 1000000))