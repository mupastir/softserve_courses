from this import s


class PythonZen:

    def __init__(self):
        self.string_zen = s
        self.zen_in_string = self.zen_to_string(self.get_decode_zen())
        self.find_occurrences()
        self.better, self.never, self.is_times = self.find_occurrences()
        self.zen_upper = self.zen_in_string.upper()
        self.print_result()

    def get_decode_zen(self):
        """
        Function decoded zen of Python by algorithm from module this
        :return:
        """
        dictionary_cipher = {}
        for c in (65, 97):
            for i in range(26):
                dictionary_cipher[chr(i + c)] = chr((i + 13) % 26 + c)
        return "".join([dictionary_cipher.get(c, c) for c in self.string_zen])

    def zen_to_string(self, zen: str) -> str:
        return zen.replace('\n', ' ')

    def find_occurrences(self):
        return self.zen_in_string.count('better'), self.zen_in_string.count('never'), self.zen_in_string.count('is')

    def print_result(self):
        print('\nZen in one string:\n{}'.format(self.zen_in_string),
              end='\n\n')
        print('"better" found {} times, "never" - {}, "is" - {}'.format(self.better,
                                                                        self.never,
                                                                        self.is_times),
              end='\n\n')
        print('Zen in UPPERCASE:\n{}'.format(self.zen_upper),
              end='\n\n')
        print('Zen replaced "i" with "&":\n{}'.format(self.zen_in_string.replace('i', '&')),
              end='\n\n')
