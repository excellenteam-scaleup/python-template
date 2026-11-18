def group_by(key_func, items):
    key_dict = {}
    for item in items:
        if (key := key_func(item)) not in key_dict:
            key_dict[key] = [item]
        else:
            key_dict[key].append(item)

    return key_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
