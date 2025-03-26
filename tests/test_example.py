import unittest
from src.example import Example


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_example(self):
        exmaple = Example()
        self.assertEqual(exmaple.x, 6)


if __name__ == '__main__':
    unittest.main()
