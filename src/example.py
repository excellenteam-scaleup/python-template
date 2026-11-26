
"""Example module for testing."""


def not_a_pep8_fn():
    """Print an example message."""
    print("Linter should error!")


class Example:
    """Example class for unit testing."""

    def __init__(self):
        """Initialize the example value."""
        self.x = 6

    def wrong_func(self):
        """Print an example message."""
        print("Linter should error!")

    def get_value(self):
        """Return the example value."""
        return self.x
