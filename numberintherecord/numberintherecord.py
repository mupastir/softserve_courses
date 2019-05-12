class NumberRecord:

    def __init__(self, number):
        self.number = int(number)
        self.ELEMENTARY = {0: "ноль",
                           1: "один",
                           2: "два",
                           3: "три",
                           4: "четыре",
                           5: "пять",
                           6: "шесть",
                           7: "семь",
                           8: "восемь",
                           9: "девять"}
        self.UNITS = {10: "десять",
                      12: "двенадцать",
                      13: "тринадцать",
                      40: "сорок",
                      90: "девяносто",
                      'suffix under 20': "надцать",
                      'suffix under 40': "дцать",
                      'suffix more 40': "десят"}
        self.HUNDREDS = {100: "сто",
                         200: "двести",
                         300: "триста",
                         400: "четыреста",
                         'suffix till 900': "сот"}
        self.THOUSAND = ["тысяча", "тысячи", "тысяч"]
        self.record = []
        self.transformation()
        self.__repr__()

    def __repr__(self):
        for e in self.record:
            print(e, end=' ')

    def transformation(self):
        if self.number == 0:
            self.record.append(self.ELEMENTARY[0])
        else:
            self.transform_basic_third()
            while self.number % 1000 > 0:
                self.append_thousand_name()
                self.transform_basic_third()

    def transform_basic_third(self):
        self.units(self.number % 10)
        self.hundreds()
        self.number //= 10
        if '' in self.record:
            self.record.remove('')

    def append_thousand_name(self):
        if self.number % 100 == 11:
            self.record.insert(0, self.THOUSAND[2])
        elif self.number % 10 == 1:
            self.record.insert(0, self.THOUSAND[0])
        elif 1 < self.number % 10 < 5:
            self.record.insert(0, self.THOUSAND[1])
        else:
            self.record.insert(0, self.THOUSAND[2])

    def units(self, unit: int):
        if len(self.record) > 2 and unit == 1:
            unit_list = [unit, "одна"]
        elif len(self.record) > 2 and unit == 2:
            unit_list = [unit, "две"]
        elif unit == 0:
            unit_list = [unit, ""]
        else:
            unit_list = [unit, self.ELEMENTARY[unit]]
        return self.tens(unit_list)

    def tens(self, units: list):
        digit_to_check = self.get_digit()
        if digit_to_check == 0:
            self.record.insert(0, units[1])
        elif digit_to_check == 1 and units[0] == 0:
            self.record.insert(0, self.UNITS[10])
        elif digit_to_check == 1 and units[0] == 2:
            self.record.insert(0, self.UNITS[12])
        elif digit_to_check == 1 and units[0] == 3:
            self.record.insert(0, self.UNITS[13])
        elif digit_to_check == 1:
            self.record.insert(0, units[1][:-1] +
                               self.UNITS['suffix under 20'])
        elif digit_to_check < 4:
            self.record.insert(0, self.ELEMENTARY[digit_to_check] +
                               self.UNITS['suffix under 40'])
            self.record.insert(1, units[1])
        elif digit_to_check == 4:
            self.record.insert(0, self.UNITS[40])
            self.record.insert(1, units[1])
        elif digit_to_check == 9:
            self.record.insert(0, self.UNITS[90])
            self.record.insert(1, units[1])
        elif digit_to_check > 4:
            self.record.insert(0, self.ELEMENTARY[digit_to_check] +
                               self.UNITS['suffix more 40'])
            self.record.insert(1, units[1])

    def hundreds(self):
        hundred = 100
        digit_to_check = self.get_digit()
        if 0 < digit_to_check < 5:
            self.record.insert(0, self.HUNDREDS[digit_to_check*hundred])
        elif digit_to_check > 4:
            self.record.insert(0, self.ELEMENTARY[digit_to_check] +
                               self.HUNDREDS['suffix till 900'])

    def get_digit(self):
        self.number //= 10
        return self.number % 10
