import unittest
from happyticket import HappyTicket
from happyticket import is_existence_file


class TestHappyTicket(unittest.TestCase):

    def setUp(self):
        self.peter = HappyTicket(['121358', '278561'], 'pIteR')
        self.moscow = HappyTicket(['253145', '111111'], 'MoskoW')
        self.non_digit_ticket = HappyTicket(['1213dvdf'], 'pIteR')
        self.not_six_digit_len = HappyTicket(['1213'], 'pIteR')

    def test_peter(self):
        self.assertEqual(str(self.peter),
                         'There are 1 happy piter tickets')

    def test_moscow(self):
        self.assertEqual(str(self.moscow),
                         'There are 2 happy moskow tickets')

    def test_not_existence_file(self):
        self.assertRaises(FileNotFoundError,
                          is_existence_file('smth_not_existence'))

    def test_not_correct_mode(self):
        self.assertRaises(KeyError,
                          HappyTicket([], 'moscaw').main())

    def test_non_digits_ticket(self):
        self.assertRaises(TypeError, self.non_digit_ticket.main())

    def test_not_six_digit_len(self):
        self.assertRaises(ValueError, self.not_six_digit_len.main())


if __name__ == "__main__":
    unittest.main()
