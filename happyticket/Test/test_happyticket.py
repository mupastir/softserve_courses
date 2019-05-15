import unittest
from happyticket import HappyTicket
from happyticket import is_existence_file


class TestHappyTicket(unittest.TestCase):

    def test_peter(self):
        peter = HappyTicket(['121358', '278561'], 'pIteR')
        self.assertEqual(peter.main(),
                         'There are 1 happy piter tickets')

    def test_moscow(self):
        moscow = HappyTicket(['253145', '111111'], 'MoskoW')
        self.assertEqual(moscow.main(),
                         'There are 2 happy moskow tickets')

    def test_not_existence_file(self):
        self.assertRaises(FileNotFoundError,
                          is_existence_file('smth_not_existence'))

    def test_not_correct_mode(self):
        self.assertRaises(KeyError,
                          HappyTicket([], 'moscaw'))

    def test_non_digits_ticket(self):
        non_digits_ticket = HappyTicket(['1213dvdf'], 'pIteR')
        self.assertRaises(TypeError, non_digits_ticket.main())

    def test_not_six_digit_len(self):
        not_six_digit_len = HappyTicket(['1213'], 'pIteR')
        self.assertRaises(ValueError, not_six_digit_len.main())


if __name__ == "__main__":
    unittest.main()
