"""Decorator that runs the function it wraps twice."""

def twice(func):
    """Decorate a function so it is executed twice.

    :param func: The function to decorate
    :return: The wrapped function
    """
    def wrapper(*args, **kwargs):
        """Call the original function twice and return both results."""
        return (
            func(args, kwargs),
            func(args, kwargs)
        )
    return wrapper


def func():
    """Print a sample letter."""
    print("A")

if __name__ == "__main__":
    func()