import unittest
from envelopanalysis import EnvelopAnalysis


class TestEnvelop(unittest.TestCase):

    def test_norm_enclosed_args(self):
        self.assertEqual(EnvelopAnalysis([5, 5.5], [2, 2.5]).check_data(),
                         'Envelope can be enclosed!\n')

    def test_norm_non_enclosed_args(self):
        self.assertEqual(EnvelopAnalysis([5, 5.5], [7.5, 2.5]).check_data(),
                         'Envelope can\'t be enclosed!\n')

    def test_non_normal_args(self):
        self.assertRaises(TypeError,
                          EnvelopAnalysis(['miyke', 5.5],
                                          [7.5, 2.5]).check_data())

    def test_args_less_equal_zero(self):
        self.assertRaises(ValueError,
                          EnvelopAnalysis([-1, 5.5],
                                          [7.5, 0]).check_data())


if __name__ == "__main__":
    unittest.main()
