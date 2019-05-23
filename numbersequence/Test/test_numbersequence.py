import unittest
from numbersequence import NumberSequence


class TestNumberSequence(unittest.TestCase):

    def test_norm_args(self):
        self.assertEqual(str(NumberSequence(90.01).build_sequence()),
                         '1, 2, 3, 4, 5, 6, 7, 8, 9')

    def test_less_one(self):
        self.assertRaises(ValueError, NumberSequence, -0.9)

    def test_non_numbers(self):
        self.assertRaises(TypeError, NumberSequence, 'str')


if __name__ == "__main__":
    unittest.main()
