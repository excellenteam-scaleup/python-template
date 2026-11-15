def interleave(*iterables):
    result = []

    for items in zip(*iterables):
        for item in items:
            result.append(item)

    return result


def generator_interleave(*iterables):
    for items in zip(*iterables):
        for item in items:
            yield item


if __name__ == "__main__":
    print(interleave("abc", [1, 2, 3], ("!", "@", "#")))

    print(list(generator_interleave(
        "abc", [1, 2, 3], ("!", "@", "#")
    )))
    