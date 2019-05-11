class EnvelopAnalysis:

    def __init__(self):
        self.INFO_MSG = "Enter size of every side of 2 envelops in order:\n" \
                        "1 - a-size\n" \
                        "1 - b-size\n" \
                        "2 - c-size\n" \
                        "2 - d-size\n\n"
        self.ERR_MSG = "There were put not numbers!"
        self.result_msg = 'Envelope can be enclosed!\n'
        print(self.INFO_MSG, end='')
        self.first_envelop, self.second_envelop = self.input_sides()
        if self.are_normal_args():
            if self.is_enclosed():
                print(self.result_msg)
            else:
                print(self.result_msg.replace('can', 'can\'t'))
        else:
            print(self.ERR_MSG)
        self.ask_restart()

    def input_sides(self):
        sides = ('A', 'B')
        envelops = 2
        return [[input(f'Enter size {s} of envelope No{e+1}: ')
                 for s in sides]
                for e in range(envelops)]

    def are_normal_args(self) -> bool:
        try:
            float(self.first_envelop[0]), float(self.first_envelop[1])
            float(self.second_envelop[0]), float(self.second_envelop[1])
        except (ValueError, TypeError):
            return False
        else:
            return True

    def is_enclosed(self):
        vertical_enclosed = \
            min(self.first_envelop) > max(self.second_envelop) or \
            min(self.second_envelop) > max(self.first_envelop)
        horizontal_enclosed = \
            min(self.first_envelop) > min(self.second_envelop) and \
            max(self.first_envelop) > max(self.second_envelop) or \
            min(self.second_envelop) > min(self.first_envelop) and \
            max(self.second_envelop) > max(self.first_envelop)
        if vertical_enclosed or horizontal_enclosed:
            return True
        return False

    def ask_restart(self):
        if input('If you want restart '
                 'calculation enter "y" or "yes": ').lower() == ('y' or 'yes'):
            EnvelopAnalysis()
        return
