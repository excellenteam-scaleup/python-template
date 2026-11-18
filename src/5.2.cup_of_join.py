"""Join several lists into one list with a separator between them."""


def cup_of_join(*lists, sep: str = '-'):
    """Join any number of lists into a single list, separated by sep.

    :param lists: The lists to join
    :param sep: Separator inserted between the lists (default '-')
    :return: The joined list, or None if no lists were given
    :raises TypeError: If one of the arguments is not a list
    """
    if len(lists) == 0:
        return None

    if any(not isinstance((unexpected := arg), list) for arg in lists):
        raise TypeError(f'expected a list, got: {type(unexpected)}')

    res = []
    for current_list in lists:
        res += [sep] + current_list
    res.pop(0)
    return res


if __name__ == '__main__':
    print(cup_of_join([1, 2, 3], [4, 5, 6]))
    print(cup_of_join([1, 2, 3], [4, 5, 6], sep='@'))
    print(cup_of_join())
