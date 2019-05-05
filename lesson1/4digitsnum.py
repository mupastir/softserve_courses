class FourDigitsNum:

    def __init__(self, number: int):
        self.number = str(number)
        self.summary = 0
        self.sorted_number = ''

    def __call__(self):
        for digit in sorted(self.number):
            self.summary += int(digit)
            self.sorted_number += digit

        return self.__repr__()

    def __repr__(self):
        print('Summary of digits of the number = {}'.format(self.summary),
              end='\n\n')
        print('Our number in reverse order: {}'.format(self.number[::-1]),
              end='\n\n')
        print('Sorted digits in number: {}'.format(self.sorted_number))


if __name__ == "__main__":
    test = FourDigitsNum(54648)
    test()
