import unittest
from ticketscheckhappy import *


class TestHappyTicket(unittest.TestCase):

    def setUp(self):
        self.peter = TicketsCheckHappy(['121358', '278561'], 'pIteR')
        self.moscow = TicketsCheckHappy(['253145', '111111'], 'MoskoW')

    def test_peter(self):
        self.assertEqual(str(self.peter.count_happy_tickets()),
                         'There are 1 happy piter tickets')

    def test_moscow(self):
        self.assertEqual(str(self.moscow.count_happy_tickets()),
                         'There are 2 happy moskow tickets')

    def test_non_existence_file(self):
        self.assertRaises(FileNotFoundError,
                          existence_file, 'smth_not_existence')

    def test_non_correct_mode(self):
        self.assertRaises(KeyError, TicketsCheckHappy, ['121358'], 'moscaw')

    def test_non_digits_ticket(self):
        self.assertRaises(ValueError, TicketsCheckHappy, ['1213dvdf'], 'pIteR')

    def test_non_six_digit_len(self):
        self.assertRaises(ValueError, TicketsCheckHappy, ['12'], 'pIteR')


if __name__ == "__main__":
    unittest.main()
