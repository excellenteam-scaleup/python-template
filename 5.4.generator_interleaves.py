# generator_interleaves


from typing import Iterable, Generator, Any

def interleave_gen(*iterables: Iterable[Any]) -> Generator[Any, None, None]:
    """Generator version that yields interleaved elements one by one"""
    for group in zip(*iterables):
        for item in group:
            yield item

if __name__ == '__main__':
    regular_result = interleave_gen('abc', [1, 2, 3], ('!', '@', '#'))
    print("Regular function result:")
    print(regular_result)