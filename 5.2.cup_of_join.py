#cup of join


def join(*lists: list, sep: str = "-") -> list | None:
    """Joins an unlimited number of lists with a separator element between them"""
    if not lists:
        return None

    result = []
    for i, current_list in enumerate(lists):
        result.extend(current_list)
        if i < len(lists) - 1:
            result.append(sep)

    return result


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())