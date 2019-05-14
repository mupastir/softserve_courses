def suffix_nadcyat_under_14(unit_string):
    return unit_string + "надцать"


def suffix_nadcyat_under(unit_string):
    return unit_string[:-1] + "надцать"


ELEMENTARY = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре",
              5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
              'exceptions': {0: "", 1: "одна", 2: "две", 10: "десять",
                             40: "сорок", 90: "девяносто", 100: "сто",
                             200: "двести", 300: "триста", 400: "четыреста"
                             }}

SUFFIX = dict((k, suffix_nadcyat_under_14) for k in range(11, 14))
SUFFIX.update(dict((k, suffix_nadcyat_under) for k in range(14, 20)))
SUFFIX.update(dict((k, "дцать") for k in range(20, 40, 10)))
SUFFIX.update(dict((k, "десят") for k in range(50, 100, 10)))
SUFFIX.update(dict((k, "сот") for k in range(500, 1000, 100)))

THOUSAND = {1: "тысяча"}
THOUSAND.update(dict((k, "тысячи") for k in range(2, 5)))
THOUSAND.update(dict((k, "тысяч") for k in range(5, 20)))


class NumberRecord:

    def __init__(self, number: int):
        self.number = number
        self.record = []
        self.transformation()

    def __repr__(self):
        return self.record

    def transformation(self):
        if self.number < 10:
            self.record.append(ELEMENTARY[self.number])
        else:
            self._transform_basic_third()
            while self.number % 1000 > 0:
                self._append_thousand_name()
                self._transform_basic_third()
        self.record = self._list_to_string(self.record)
        print(self.record)
        return self.record

    @staticmethod
    def _list_to_string(our_list):
        return " ".join(map(str, our_list))

    def _transform_basic_third(self):
        self._units(self.number % 10)
        self._hundreds()
        self.number //= 10
        if '' in self.record:
            self.record.remove('')

    def _append_thousand_name(self):
        if self.number % 100 in THOUSAND:
            self.record.insert(0, THOUSAND[self.number % 100])
        else:
            self.record.insert(0, THOUSAND[self.number % 10])

    def _units(self, unit: int):
        if len(self.record) > 2 and unit in ELEMENTARY['exceptions']:
            unit_list = [unit, ELEMENTARY['exceptions'][unit]]
        elif unit == 0:
            unit_list = [unit, ""]
        else:
            unit_list = [unit, ELEMENTARY[unit]]
        return self._tens(unit_list)

    def _tens(self, units: list):
        digit_to_check = self._get_digit()
        tens_number_to_check = int(str(digit_to_check) + str(units[0]))
        if digit_to_check == 0:
            self.record.insert(0, units[1])
        elif tens_number_to_check in ELEMENTARY['exceptions']:
            self.record.insert(0,
                               ELEMENTARY['exceptions'][tens_number_to_check])
        elif tens_number_to_check in SUFFIX:
            self.record.insert(0, SUFFIX[tens_number_to_check](units[1]))
        elif digit_to_check * 10 in ELEMENTARY['exceptions']:
            self.record.insert(0,
                               ELEMENTARY['exceptions'][digit_to_check * 10] +
                               ' ' + units[1])
        elif digit_to_check * 10 in SUFFIX:
            self.record.insert(0, ELEMENTARY[digit_to_check] +
                               SUFFIX[digit_to_check * 10] + ' ' + units[1])

    def _hundreds(self):
        digit_to_check = self._get_digit()
        hundred_to_check = digit_to_check * 100
        if hundred_to_check in ELEMENTARY['exceptions']:
            self.record.insert(0, ELEMENTARY['exceptions'][hundred_to_check])
        else:
            self.record.insert(0, ELEMENTARY[digit_to_check] +
                               SUFFIX[hundred_to_check])

    def _get_digit(self):
        self.number //= 10
        return self.number % 10


if __name__ == "__main__":
    NumberRecord(555666)
