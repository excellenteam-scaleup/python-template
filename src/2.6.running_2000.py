from time import perf_counter

def running_2000(f, *args, **kwargs):
    start = perf_counter()
    f(*args, **kwargs)
    return perf_counter()-start

if __name__ == '__main__':
    for j in range(10):
        print(running_2000(lambda x: [i ** 12 for i in range(x)], 10**j))

