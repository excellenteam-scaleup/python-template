from typing import Iterable, Any

def interleave(*iterables: Iterable[Any]) -> list[Any]:
    """Interleaves elements from multiple iterables into a single list"""
    result = []
    for group in zip(*iterables):
        for item in group:
            result.append(item)
    return result


if __name__ == '__main__':
    regular_result = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    print("Regular function result:")
    print(regular_result)