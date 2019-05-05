from this import s

class PythonZen:

    def __init__(self):
        self.s = s
        self.zen_in_string = self.zen_to_string(self.get_zen())
        self.find_occurrences()
        self.better, self.never, self.is_times = self.find_occurrences()
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

    def get_zen(self):
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i + c)] = chr((i + 13) % 26 + c)
        return "".join([d.get(c, c) for c in self.s])

    def zen_to_string(self, zen: str) -> str:
        return zen.replace('\n', ' ')

    def find_occurrences(self):
        return self.zen_in_string.count('better'), self.zen_in_string.count('never'), self.zen_in_string.count('is')
