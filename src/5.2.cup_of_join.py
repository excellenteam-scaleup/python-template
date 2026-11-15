def join(*lists, sep="-"):
    if not lists:
        return None

    result = []

    for i, current_list in enumerate(lists):
        if i > 0:
            result.append(sep)
        result.extend(current_list)

    return result


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep="@"))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
