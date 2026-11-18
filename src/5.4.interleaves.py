def generator_interleave(*iterables):
    for group in zip(*iterables):
        for item in group:
            yield item


def interleave(*iterables):
    return list(generator_interleave(*iterables))


if __name__ == "__main__":
    print(interleave("abc", [1, 2, 3], ("!", "@", "#")))
    print(list(generator_interleave("abc", [1, 2, 3], ("!", "@", "#"))))