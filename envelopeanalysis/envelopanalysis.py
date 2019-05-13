class EnvelopAnalysis:

    def __init__(self):
        self.INFO_MSG = "Enter size of every side of 2 envelops in order:\n" \
                        "1 - a-size\n" \
                        "1 - b-size\n" \
                        "2 - c-size\n" \
                        "2 - d-size\n\n"
        self.ERR_MSG = "There were put not numbers!"
        self.result_msg = 'Envelope can be enclosed!\n'
        self.first_envelop, self.second_envelop = [(), ()]

    def main(self):
        print(self.INFO_MSG, end='')
        self.first_envelop, self.second_envelop = self.input_sides()
        self.check_data(self.first_envelop, self.second_envelop)
        self.ask_restart()

    def check_data(self, first_envelop, second_envelop):
        if self.are_normal_args(first_envelop, second_envelop):
            if self.is_enclosed(first_envelop, second_envelop):
                print(self.result_msg, end='')
            else:
                print(self.result_msg.replace('can', 'can\'t'), end='')
        else:
            print(self.ERR_MSG, end='')

    def input_sides(self):
        sides = ('A', 'B')
        envelops = 2
        return [[input(f'Enter size {s} of envelope No{e+1}: ')
                 for s in sides]
                for e in range(envelops)]

    def are_normal_args(self, first_envelop, second_envelop) -> bool:
        try:
            float(first_envelop[0]), float(first_envelop[1])
            float(second_envelop[0]), float(second_envelop[1])
        except (ValueError, TypeError):
            return False
        else:
            return True

    def is_enclosed(self, first_envelop, second_envelop):
        enclosed = \
            min(first_envelop) > min(second_envelop) and \
            max(first_envelop) > max(second_envelop) \
            or \
            min(second_envelop) > min(first_envelop) and \
            max(second_envelop) > max(first_envelop)
        if enclosed:
            return True
        return False

    def ask_restart(self):
        if input('If you want restart '
                 'calculation enter "y" or "yes": ').lower() == ('y' or 'yes'):
            EnvelopAnalysis()
        return
