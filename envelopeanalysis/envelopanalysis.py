INFO_MSG = "Enter size of every side of 2 envelops in order:\n" \
           "1 - a-size\n" \
           "1 - b-size\n" \
           "2 - c-size\n" \
           "2 - d-size\n\n"
ERR_MSG = "There were put not numbers or not existing envelops!\n" \
          "(Less or equal zero!)"


def _input_sides():
    print(INFO_MSG, end='')
    sides = ('A', 'B')
    envelops = 2
    return [[input(f'Enter size {s} of envelope No{e+1}: ')
             for s in sides]
            for e in range(envelops)]


class EnvelopAnalysis:

    def __init__(self, envelop_first, envelop_second):
        self.result_msg = 'Envelope can be enclosed!\n'
        self.first_envelop, self.second_envelop = envelop_first, envelop_second

    def main(self):
        if self.check_data() is None:
            self._restart()
        print(self.result_msg)
        self._ask_restart()

    def check_data(self):
        if self._are_normal_args(self.first_envelop, self.second_envelop):
            self.first_envelop, self.second_envelop = \
                [float(self.first_envelop[0]), float(self.first_envelop[1])], \
                [float(self.second_envelop[0]), float(self.second_envelop[1])]
            if not self._is_enclosed(self.first_envelop, self.second_envelop):
                self.result_msg = self.result_msg.replace('can', 'can\'t')
        else:
            return
        return self.result_msg

    def __repr__(self):
        return self.result_msg

    def _are_normal_args(self, first_envelop, second_envelop) -> bool:
        try:
            float(first_envelop[0]), float(first_envelop[1])
            float(second_envelop[0]), float(second_envelop[1])
            if float(first_envelop[0]) <= 0 or \
                    float(first_envelop[1]) <= 0 or \
                    float(second_envelop[0]) <= 0 or \
                    float(second_envelop[1]) <= 0:
                raise ValueError
        except (TypeError, ValueError):
            print(ERR_MSG)
            return False
        else:
            return True

    @staticmethod
    def _is_enclosed(first_envelop, second_envelop):
        enclosed = \
            (min(first_envelop) > min(second_envelop) and
             max(first_envelop) > max(second_envelop))\
            or \
            (min(second_envelop) > min(first_envelop) and
             max(second_envelop) > max(first_envelop))
        if enclosed:
            return True
        return False

    def _ask_restart(self):
        if input('If you want restart '
                 'calculation enter "y" or "yes": ').lower() == ('y' or 'yes'):
            self._restart()
        return

    @staticmethod
    def _restart():
        first_envelop, second_envelop = _input_sides()
        EnvelopAnalysis(first_envelop, second_envelop).main()


if __name__ == "__main__":
    first_envelop, second_envelop = _input_sides()
    EnvelopAnalysis(first_envelop, second_envelop).main()
