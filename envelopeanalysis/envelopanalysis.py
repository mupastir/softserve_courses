class EnvelopAnalysis:

    def __init__(self):
        self.info_msg = "Enter size of every side of 2 envelops in oreder:\n" \
                        "1 - a-size\n" \
                        "1 - b-size\n" \
                        "2 - c-size\n" \
                        "2 - d-size\n\n"
        self.err_msg = "There were put not numbers!"
        print(self.info_msg, end='')
        f_env_side_a, f_env_side_b, \
            s_env_side_a, s_env_side_b = [input('Enter size of envelope: ')
                                          for i in range(4)]
        self.first_envelop = [f_env_side_a, f_env_side_b]
        self.second_envelop = [s_env_side_a, s_env_side_b]

        if self.are_normal_args():
            print(f_env_side_a, f_env_side_b, s_env_side_a, s_env_side_b)
            if self.is_enclosed():
                print('Envelope can be enclosed!\n')
            else:
                print("Envelope can't be enclosed!\n")
            self.ask_restart()
        else:
            print(self.err_msg)
            self.ask_restart()

    def are_normal_args(self) -> bool:
        try:
            float(self.first_envelop[0]), float(self.first_envelop[1])
            float(self.second_envelop[0]), float(self.second_envelop[1])
        except (ValueError, TypeError):
            return False
        else:
            return True

    def ask_restart(self):
        if input('If you want restart '
                 'calculation enter "y" or "yes": ').lower() == ('y' or 'yes'):
            EnvelopAnalysis()
        return

    def is_enclosed(self):
        if min(self.first_envelop) > max(self.second_envelop) or \
                min(self.second_envelop) > max(self.first_envelop):
            return True
        else:
            return False
