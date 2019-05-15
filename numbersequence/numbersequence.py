ERR_MSG = {'value': 'There aren\'t numbers less then square of 1',
           'type': 'There was put not number!'}


class NumberSequence:

    def __init__(self, end_number):
        self._end_number = end_number
        self._result_sequence = []
        self.build_sequence()

    def build_sequence(self):
        if self._is_number_valid():
            self._result_sequence = self.sequence_append(self._end_number)
            self._result_sequence = ', '.join(map(str, self._result_sequence))
            return self._result_sequence

    @staticmethod
    def sequence_append(end_square_number):
        member_of_sequence = 1
        while member_of_sequence**2 < end_square_number:
            yield member_of_sequence
            member_of_sequence += 1

    def _is_number_valid(self):
        try:
            float(self._end_number)
            if float(self._end_number) <= 1:
                raise ValueError
        except ValueError:
            print(ERR_MSG['value'])
            return False
        except TypeError:
            print(ERR_MSG['type'])
            return False
        else:
            return True


if __name__ == "__main__":
    A = NumberSequence('str').build_sequence()
    # print(A)
