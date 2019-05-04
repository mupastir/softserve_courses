import unittest
from chessdesk import ChessDesk


class TestChessdesk(unittest.TestCase):

    def test_no_argues_given(self):
        required_string = ''''''
        test = ChessDesk()
        self.assertEqual(test(), required_string)

    def test_height_only_given(self):
        required_string = '''* * * \n * * *\n* * * \n * * *\n* * * \n * * *'''
        test = ChessDesk(6)
        self.assertEqual(test(), required_string)

    def test_size_given_less_than_two(self):
        required_string = {"'Size too short!' [1, 1]"}
        test = ChessDesk(1)
        self.assertEqual(test(), required_string)

    def test_given_args_not_nums(self):
        required_string = {"There didn't put numbers, please enter to create square desk HEIGHT.\n"
                           "To create rectangular desk enter first HEIGHT and second WEIGHT."}
        test = ChessDesk('str', 'str')
        self.assertEqual(test(), required_string)

    def test_given_even_size(self):
        required_string = '''* * * \n * * *\n* * * \n * * *'''
        test = ChessDesk(4, 6)
        self.assertEqual(test(), required_string)

    def test_given_odd_size(self):
        required_string = '''* * * *\n * * * \n* * * *\n * * * \n* * * *'''
        test = ChessDesk(5, 7)
        self.assertEqual(test(), required_string)


if __name__ == "__main__":
    unittest.main()
