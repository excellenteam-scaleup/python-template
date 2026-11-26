
"""Unit tests for the example module."""

import unittest
from src.example import Example


class MyTestCase(unittest.TestCase):
    """Test the example class."""

    def test_something(self):
        """Check the value returned by the getter."""
        example = Example()
        self.assertEqual(example.get_value(), 6)

    def test_example(self):
        """Check the initial example value."""
        example = Example()
        self.assertEqual(example.x, 6)


if __name__ == "__main__":
    unittest.main()
