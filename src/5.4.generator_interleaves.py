def generator_interleaves(*iterators):
    iterators_list = []
    for iterator in iterators:
        iterators_list.append(iter(iterator))

    result = []

    while iterators_list:
        for iterator in iterators_list:
            try:
                result.append(next(iterator))
            except StopIteration:
                iterators_list.remove(iterator)

    return result


if __name__ == '__main__':
    print(generator_interleaves([1, 2, 3], [1, 2], ['1', '2', '3', '4']))
