import os.path

ERR_MSG = {"ticket": "Size one of the "
                     "ticket not equal 6 or there were put not digits!",
           "mode": 'It was put not correct mode! There are only "Moskow" '
                   'and "Piter"',
           "file": 'File does not exist'}


def main():
    try:
        tickets = get_tickets_from_file()
        mode = input("Enter mode: ")
        tickets = TicketsCheckHappy(tickets, mode)
        number_of_happy_tickets = tickets.count_happy_tickets()
        print(number_of_happy_tickets)
    except Exception as e:
        print(str(e))
        main()


def get_tickets_from_file() -> list:
    filepath = input('Enter filename: ')
    tickets_list = []
    existence_file(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        for string in f:
            tickets_list.append(string.strip())
    return tickets_list


def existence_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(ERR_MSG["file"])


class TicketsCheckHappy:

    def __init__(self, tickets: list, mode: str):
        self.MODES = {"moskow": self.is_happy_by_moscow_mode,
                      "piter": self.is_happy_by_peter_mode}
        self._valid_mode(mode.lower())
        self._valid_tickets(tickets)
        self._mode = mode.lower()
        self._tickets = tickets
        self._happy_tickets = 0
        self._result = ''
        self._check_by_mode = self.MODES[self._mode]

    def count_happy_tickets(self) -> str:
        for ticket in self._tickets:
            if self._check_by_mode(ticket):
                self._happy_tickets += 1
        self._result = f'There are {self._happy_tickets} ' \
                       f'happy {self._mode.lower()} tickets'
        return self._result

    @staticmethod
    def is_happy_by_moscow_mode(ticket: str) -> bool:
        first_part = [int(d) for d in ticket[:3]]
        second_part = [int(d) for d in ticket[3:]]
        if sum(first_part) == sum(second_part):
            return True
        return False

    @staticmethod
    def is_happy_by_peter_mode(ticket: str) -> bool:
        even_digits = sum([int(d) for d in ticket if int(d) % 2 == 0])
        odd_digits = sum([int(d) for d in ticket if int(d) % 2 == 1])
        if even_digits == odd_digits:
            return True
        return False

    def _valid_mode(self, mode):
        if mode not in self.MODES:
            raise KeyError(ERR_MSG['mode'])

    @staticmethod
    def _valid_tickets(tickets):
        for ticket in tickets:
            if len(ticket) != 6 or not ticket.isnumeric():
                raise ValueError(f'{ticket} {ERR_MSG["ticket"]}')

    def __repr__(self) -> str:
        return self._result


if __name__ == "__main__":
    main()
