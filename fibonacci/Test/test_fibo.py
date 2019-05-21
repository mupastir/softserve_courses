import unittest
from fibonacci import *


class TestFiboRange(unittest.TestCase):

    def setUp(self):
        self.positive = FibonacciRange(15)
        self.negative = FibonacciRange(start_range=-50, end_range=-5)
        self.mixed = FibonacciRange(start_range=-30, end_range=30)

    def test_positive_args(self):
        self.assertEqual(self.positive.build_sequence(),
                         [0, 1, 1, 2, 3, 5, 8, 13])

    def test_negative_args(self):
        self.assertEqual(self.negative.build_sequence(),
                         [34, -21, 13, -8, 5])

    def test_mixed_args(self):
        self.assertEqual(self.mixed.build_sequence(),
                         [-21, 13, -8, 5, -3, 2, -1, 1,
                          0, 1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == "__main__":
    unittest.main()
