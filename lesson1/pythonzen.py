class PythonZen:

    def __repr__(self):
        print('Zen in one string:\n{}'.format(self.zen_in_string),
              end='\n\n')
        print('"better" found {} times, "never" - {}, "is" - {}'.format(self.better,
                                                                        self.never,
                                                                        self.is_times),
              end='\n\n')
        print('Zen in UPPERCASE:\n{}'.format(self.zen_in_string.upper()),
              end='\n\n')
        print('Zen in UPPERCASE:\n{}'.format(self.zen_in_string.replace('i', '&')),
              end='\n\n')

    def __call__(self):
        self.zen_in_string = self.zen_to_string('zen.txt')
        self.find_occurrences()
        return self.__repr__()

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
