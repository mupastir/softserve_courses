import io
import unittest.mock
from envelopanalysis import EnvelopAnalysis


class TestEnvelop(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, required_string,
                      side1a, side1b, side2a, side2b,
                      mock_stdout):
        test = EnvelopAnalysis()
        test.check_data((side1a, side1b), (side2a, side2b))
        self.assertEqual(mock_stdout.getvalue(), required_string)

    def test_norm_enclosed_args(self):
        self.assert_stdout('Envelope can be enclosed!\n',
                           5, 5.5, 2, 2.5)

    def test_norm_non_enclosed_args(self):
        self.assert_stdout('Envelope can\'t be enclosed!\n',
                           5, 5.5, 7.5, 2.5)

    def test_non_normal_args(self):
        self.assert_stdout("There were put not numbers!",
                           'miyke', 5.5, 7.5, 2.5)


if __name__ == "__main__":
    unittest.main()
