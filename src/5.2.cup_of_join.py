def join(*lists, sep="-"):
    if not lists:
        return None

    result = []

    for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)
        result.extend(lst)

    return result


if __name__ == "__main__":
    print(join([1, 2], [3, 4], [5, 6]))
    print(join([1, 2], [3, 4], sep="*"))
    print(join())