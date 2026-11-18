from functools import wraps


class WrongTypeError(TypeError):
    pass


def type_check(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(value):
            if not isinstance(value, expected_type):
                raise WrongTypeError("Wrong argument type")
            return func(value)

        return wrapper

    return decorator


if __name__ == "__main__":
    @type_check(int)
    def double(number):
        return number * 2

    print(double(5))