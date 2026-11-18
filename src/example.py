"""Example module from the template, used to demonstrate linter errors."""

def not_a_pep8_fn():
    """Print a message saying the linter should report an error."""
    print("Linter should error!")


class Example:
    """Example class used to demonstrate linter errors."""
    def __init__(self):
        """Initialize the example with a sample attribute x."""
        self.x = 6

    def wrong_func(self):
        """Print a message saying the linter should report an error."""
        print("Linter should error!")
