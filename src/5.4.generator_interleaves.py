"""Interleave the items of several iterables."""


def generator_interleaves(*data_containers):
    """Interleave items from several iterables, one item from each in turn.

    :param iterators: The iterables to interleave
    :return: List of the interleaved items
    """
    iterators_list = []
    for item in data_containers:
        iterators_list.append(iter(item))

    result = []

    while iterators_list:
        # Iterate over a copy so removing exhausted iterators is safe
        for iterator in iterators_list[:]:
            try:
                result.append(next(iterator))
            except StopIteration:
                iterators_list.remove(iterator)

    return result


if __name__ == '__main__':
    print(generator_interleaves([1, 2, 3], [1, 2], ['1', '2', '3', '4']))
