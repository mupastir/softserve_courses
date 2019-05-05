from typing import List


class ChessDesk:
    print_symbols: List[str]

    def __init__(self, height=None, weight=None):
        self.height, self.weight = height, weight
        self.print_symbols = ['*', ' ']
        self.info_string = "There didn't put numbers, please enter to " \
                           "create square desk HEIGHT.\n" \
                           "To create rectangular desk " \
                           "enter first HEIGHT and second WEIGHT. "
        if self.are_normal_args():
            self.desk = self.built_desk()
            print(self.desk, end='')
        else:
            print(self.info_string, end='')

    def are_normal_args(self) -> bool:
        if self.weight is None:
            self.weight = self.height
        try:
            int(self.height), int(self.weight)
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
        if self.height < 2 or self.weight < 2:
            return f'Size too short!, [{self.height}, {self.weight}]'
        return row_to_print
