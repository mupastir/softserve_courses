from typing import List


class ChessDesk:
            
    print_symbols: List[str]

    def __init__(self, height=None, weight=None):
        self.height, self.weight = height, weight
        self.print_symbols = ['*', ' ']
        self.INFO_STRING = "There didn't put numbers or values are too small" \
                           ', please enter to ' \
                           "create square desk HEIGHT.\n" \
                           "To create rectangular desk " \
                           "enter first HEIGHT and second WEIGHT. "
        if self.are_normal_args():
            self.desk = self.built_desk()
        else:
            self.desk = self.INFO_STRING
        self.__repr__()

    def __repr__(self):
        print(self.desk, end='')

    def are_normal_args(self) -> bool:
        if self.weight is None:
            self.weight = self.height
        try:
            self.height, self.weight = int(round(self.height)), \
                                       int(round(self.weight))
            if self.weight < 2 or self.height < 2:
                raise ValueError
        except (ValueError, TypeError):
            return False
        else:
            return True

    def built_desk(self):
        row_to_print = ''
        for i in range(self.height):
            for j in range(self.weight):
                row_to_print += (self.print_symbols[(i + j) % 2])
            row_to_print += '\n'
        return row_to_print
