class FourDigitsNum:

    def __init__(self, number: int):
        self.number = str(number)
        self.summary = self.sum_of_digits()
        self.sorted_number = self.sorted_digits()
        self.reversed_number = self.get_reversed_number()
        self.print_results()

    def sum_of_digits(self):
        summary = 0
        for digit in self.number:
            summary += int(digit)
        return summary

    def get_reversed_number(self):
        return self.number[::-1]

    def sorted_digits(self):
        sorted_number = ''
        for digit in sorted(self.number):
            sorted_number += digit
        return sorted_number

    def print_results(self):
        print('Summary of digits of the number = {}'.format(self.summary),
              end='\n\n')
        print('Our number in reverse order: {}'.format(self.number[::-1]),
              end='\n\n')
        print('Sorted digits in number: {}'.format(self.sorted_number))
