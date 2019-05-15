ERR_MSG = {"ticket": "Size ticket not equal 6 or there were put not digits!",
           "mode": 'It was put not correct mode! There are only "Moskow" '
                   'and "Piter"'}


def get_tickets_from_file() -> list:
    filepath = input('Enter filename: ')
    tickets_list = []
    if is_existence_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for string in f:
                tickets_list.append(string.strip())
    else:
        get_tickets_from_file()
    return tickets_list


def is_existence_file(filepath):
    try:
        f = open(filepath)
        f.close()
    except FileNotFoundError:
        print('File does not exist')
        return False
    else:
        return True


class HappyTicket:

    def __init__(self, tickets: list, mode: str):
        self.MODES = {"moskow": self.moscow_mode,
                      "piter": self.peter_mode}
        self._mode = mode
        if self._is_mode:
            self._start = self.MODES[self._mode.lower()]
        self._tickets = tickets
        self._happy_tickets = 0
        self._result = ''

    def main(self):
        for ticket in self._tickets:
            self._start(ticket)
        self._result = f'There are {self._happy_tickets} ' \
                       f'happy {self._mode.lower()} tickets'
        return self._result

    def moscow_mode(self, ticket: str):
        if self._is_valid(ticket):
            ticket = str(abs(int(ticket)))
            if self._is_happy_moscow(ticket):
                self._happy_tickets += 1
            return self._happy_tickets

    def peter_mode(self, ticket: str):
        if self._is_valid(ticket):
            ticket = str(abs(int(ticket)))
            if self._is_happy_peter(ticket):
                self._happy_tickets += 1
            return self._happy_tickets

    def _is_mode(self):
        try:
            self.MODES[self._mode.lower()]
        except KeyError:
            print(ERR_MSG['mode'])
        else:
            return True

    @staticmethod
    def _is_valid(ticket) -> bool:
        try:
            int(ticket)
            if len(str(abs(int(ticket)))) != 6:
                raise ValueError
        except (ValueError, TypeError):
            print(ticket, ERR_MSG['ticket'])
            return False
        else:
            return True

    @staticmethod
    def _is_happy_moscow(ticket) -> bool:
        first_part = [int(d) for d in ticket[:3]]
        second_part = [int(d) for d in ticket[3:]]
        if sum(first_part) == sum(second_part):
            return True
        else:
            return False

    @staticmethod
    def _is_happy_peter(ticket) -> bool:
        even_digits = sum([int(d) for d in ticket if int(d) % 2 == 0])
        odd_digits = sum([int(d) for d in ticket if int(d) % 2 == 1])
        if even_digits == odd_digits:
            return True
        else:
            return False

    def __repr__(self):
        return self._result


if __name__ == "__main__":
    tickets = get_tickets_from_file()
    mode = input("Enter mode: ")

    I = HappyTicket(tickets, mode)
    I.main()
    print(I)

    M = HappyTicket(['253145', 'd626', '111111'], 'MoskoW')
    M.main()
    print(M)

    P = HappyTicket(['121358', 'd626', '278561'], 'pIteR')
    P.main()
    print(P)
