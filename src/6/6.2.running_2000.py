import time


def my_filter(function, iterable):
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def get_positive_numbers():
    user_input = input("Enter numbers separated by commas: ")
    numbers = map(int, user_input.split(','))
    return list(my_filter(lambda number: number > 0, numbers))


def timer(f, *args, **kwargs):
    start = time.perf_counter()
    f(*args, **kwargs)
    end = time.perf_counter()
    return end - start


print(list(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
print(list(my_filter(None, [0, 1, '', 'hi', None, [], [1]])))
print(list(filter(None, [0, 1, '', 'hi', None, [], [1]])))

print(get_positive_numbers())

print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))
