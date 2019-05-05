import io
import unittest
import unittest.mock
from chessdesk import ChessDesk


class TestChessdesk(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, required_string,
                      mock_stdout, height=None, weight=None):
        ChessDesk(height, weight)
        self.assertEqual(mock_stdout.getvalue(), required_string)

    def test_no_argues_given(self):
        self.assert_stdout("There didn't put numbers, please enter to " 
                           "create square desk HEIGHT.\n" 
                           "To create rectangular desk " 
                           "enter first HEIGHT and second WEIGHT. ")

    def test_height_only_given(self):
        self.assert_stdout("* * * \n * * *\n* * * "
                           "\n * * *\n* * * \n * *"
                           " *\n", height=6)

    def test_size_given_less_than_two(self):
        self.assert_stdout("Size too short!, [1, 1]", height=1)

    def test_given_args_not_nums(self):
        self.assert_stdout("There didn't put numbers, please enter to " 
                           "create square desk HEIGHT.\n" 
                           "To create rectangular desk " 
                           "enter first HEIGHT and second WEIGHT. ",
                           height='str', weight='str')

    def test_given_even_size(self):
        self.assert_stdout("* * * \n * * *\n* * * \n * * *\n",
                           height=4, weight=6)

    def test_given_odd_size(self):
        self.assert_stdout("* * * *\n * * * \n* * * *\n * * * \n* * * *\n",
                           height=5, weight=7)


if __name__ == "__main__":
    unittest.main()
