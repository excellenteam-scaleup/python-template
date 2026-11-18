"""Decorator factory that checks the type of a function's single argument."""

def type_check(type):
    """Create a decorator that checks the argument type of a one-argument function.

    :param type: The expected type of the argument
    :return: A decorator that performs the type check
    """
    def decorator(func):
        """Wrap the function with an argument type check.

        :param func: The function to decorate
        :return: The wrapped function
        """
        def wrapper(arg):
            """Check the argument type and call the original function.

            :param arg: The argument passed to the function
            :return: The result of the original function
            :raises TypeError: If the argument is not of the expected type
            """
            if not isinstance(arg, type):
                raise TypeError(f"The argument '{arg}' is not of type {type}")
            return func(arg)
        return wrapper
    return decorator


@type_check(int)
def print_int(num):
    """Print an integer.

    :param num: The integer to print
    """
    print(num)

@type_check(float)
def print_float(num):
    """Print a float.

    :param num: The float to print
    """
    print(num)

if __name__ == '__main__':
    try:
        print_int(1)
        print_int(2)
        print_int(3.2)
    except TypeError as e:
        print(e)

    try:
        print_float(3.2)
        print_float(3)
    except TypeError as e:
        print(e)