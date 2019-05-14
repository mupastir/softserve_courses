from typing import List

PRINT_SYMBOLS = ('*', ' ')
INFO_STRING = "There didn't put numbers or values are too small" \
              ', please enter to ' \
              "create square desk HEIGHT.\n" \
              "To create rectangular desk " \
              "enter first HEIGHT and second WEIGHT. "


class ChessDesk:

    def __init__(self, height=None, weight=None):
        self.height, self.weight = height, weight
        if self.weight is None:
            self.weight = self.height
        if self._are_normal_args():
            self.height, self.weight = int(round(self.height)), \
                                       int(round(self.weight))
            self.desk = self.built_desk()

    def __repr__(self):
        return self.desk

    def _are_normal_args(self) -> bool:
        try:
            int(round(self.height)), int(round(self.weight))
            if self.weight < 2 or self.height < 2:
                raise ValueError
        except (ValueError, TypeError):
            print(INFO_STRING)
        else:
            return True

    def built_desk(self):
        row_to_print = ''
        for i in range(self.height):
            for j in range(self.weight):
                row_to_print += (PRINT_SYMBOLS[(i + j) % 2])
            row_to_print += '\n'
        return row_to_print
