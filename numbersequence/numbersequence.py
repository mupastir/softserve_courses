ERR_MSG = {'value': 'There aren\'t numbers less then square of 1',
           'type': 'There was put not number!'}


def main():
    try:
        number_to_build = input('Enter number to which '
                                'square build sequence: ')
        if number_to_build.replace('.', '').isnumeric():
            number_to_build = float(number_to_build)
        example_sequence = NumberSequence(number_to_build).build_sequence()
        print(example_sequence)
    except Exception as e:
        print(str(e))
        main()


class NumberSequence:

    def __init__(self, end_number):
        self._end_number = end_number
        self._number_valid()
        self._result_sequence = ''

    def __repr__(self):
        return self._result_sequence

    def build_sequence(self):
        self._result_sequence = self.sequence_append(self._end_number)
        self._result_sequence = ', '.join(map(str, self._result_sequence))
        return self._result_sequence

    @staticmethod
    def sequence_append(end_square_number):
        member_of_sequence = 1
        while member_of_sequence ** 2 < end_square_number:
            yield member_of_sequence
            member_of_sequence += 1

    def _number_valid(self):
        if isinstance(self._end_number, float) or \
                isinstance(self._end_number, int):
            if self._end_number <= 1:
                raise ValueError(ERR_MSG['value'])
        else:
            raise TypeError(ERR_MSG['type'])


if __name__ == "__main__":
    main()
