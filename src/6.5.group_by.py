"""Group items by the result of a key function."""

def group_by(key_func, items):
    """Group items into a dict by the value key_func returns for them.

    :param key_func: Function applied to each item to get its group key
    :param items: Iterable of items to group
    :return: Dict mapping each key to the list of items that share it
    """
    key_dict = {}
    for item in items:
        if (key := key_func(item)) not in key_dict:
            key_dict[key] = [item]
        else:
            key_dict[key].append(item)

    return key_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
