from typing import Iterable, Callable, Any



def group_by(f: Callable, iterable: Iterable) -> dict:
    """ this function gets a function and an iterable, creating a dict of the function output and iterable objects"""
    output_dict ={}
    for item in iterable:
        key = f(item)
        output_dict.setdefault(key, []).append(item)
    return output_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))