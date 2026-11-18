"""Decorator that replaces a function's behavior with printing "surprise!"."""

def surprise(func):
    """Decorate a function so it prints a surprise message instead of running.

    :param func: The function to decorate
    :return: The wrapped function
    """
    def wrapper(*args, **kwargs):
        """Print the surprise message and ignore the original function."""
        print("surprise !")
    return wrapper


def func1():
    """Print a message (not decorated)."""
    print("func 1!")

@surprise
def func2():
    """Print a message (decorated, so it prints the surprise instead)."""
    print("func 2!")

def func3():
    """Print a message (not decorated)."""
    print("func 3!")

if __name__ == "__main__":
    func1()
    func2()
    func3()