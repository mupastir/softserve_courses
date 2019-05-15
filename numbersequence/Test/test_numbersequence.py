import unittest
from numbersequence import NumberSequence


class TestHappyTicket(unittest.TestCase):

    def test_norm_args(self):
        seq = NumberSequence(90.01)
        self.assertEqual(seq.build_sequence(),
                         '1, 2, 3, 4, 5, 6, 7, 8, 9')

    def test_non_number_args(self):
        seq = NumberSequence('str')
        self.assertRaises(FileNotFoundError,
                          is_existence_file('smth_not_existence'))

    def test_not_correct_mode(self):
        self.assertRaises(KeyError,
                          HappyTicket([], 'moscaw'))


if __name__ == "__main__":
    unittest.main()
