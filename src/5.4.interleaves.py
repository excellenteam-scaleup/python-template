"""Interleave the items of several iterables."""


def interleaves(*iterators):
    """Interleave items from several iterables, one item from each in turn.

    :param iterators: The iterables to interleave
    :return: List of the interleaved items
    """
    iterators_list = []
    for iterator in iterators:
        iterators_list.append(iter(iterator))

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
    print(interleaves([1, 2, 3], [1, 2], ['1', '2', '3', '4']))
