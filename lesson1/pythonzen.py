class PythonZen:

    def __repr__(self):
        print('\nZen in one string:\n{}'.format(self.zen_in_string),
              end='\n\n')
        print('"better" found {} times, "never" - {}, "is" - {}'.format(self.better,
                                                                        self.never,
                                                                        self.is_times),
              end='\n\n')
        print('Zen in UPPERCASE:\n{}'.format(self.zen_in_string.upper()),
              end='\n\n')
        print('Zen replaced "i" with "&":\n{}'.format(self.zen_in_string.replace('i', '&')),
              end='\n\n')

    def __call__(self):
        self.zen_in_string = self.zen_to_string(self.write_to_file(self.get_zen()))
        self.find_occurrences()
        return self.__repr__()

    def write_to_file(self, zen: str):
        with open('zen.txt', 'w') as f:
            f.write(zen)
        return 'zen.txt'

    def get_zen(self):
        from this import s
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i + c)] = chr((i + 13) % 26 + c)
        return "".join([d.get(c, c) for c in s])

    def zen_to_string(self, filename: str) -> str:
        zen_in_one_string = ''
        with open(filename, 'r') as file:
            for s in file.readlines():
                zen_in_one_string += s.replace('\n', ' ')
        return zen_in_one_string

    def find_occurrences(self):
        self.better = self.zen_in_string.count('better')
        self.never = self.zen_in_string.count('never')
        self.is_times = self.zen_in_string.count('is')
