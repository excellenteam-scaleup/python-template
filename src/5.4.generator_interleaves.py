def generator_interleaves(*iterators):
    iterators_list = []
    for iterator in iterators:
        iterators_list.append(iter(iterator))

    result = []
    active_iterators = len(iterators_list)
    while active_iterators > 0:
        for iterator in iterators_list:
            try:
                result.append(next(iterator))
            except StopIteration:
                active_iterators -= 1

    return result


if __name__ == '__main__':
    print(generator_interleaves([1, 2, 3], [1, 2], ['1', '2', '3', '4']))
