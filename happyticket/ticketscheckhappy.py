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
        print(tickets.main())
    except FileNotFoundError:
        print(ERR_MSG["file"])
        main()
    except KeyError:
        print(ERR_MSG["mode"])
        main()
    except ValueError:
        print(ERR_MSG["ticket"])
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
        raise FileNotFoundError


class TicketsCheckHappy:

    def __init__(self, tickets: list, mode: str):
        self.MODES = {"moskow": self.moscow_mode,
                      "piter": self.peter_mode}
        self._mode = mode.lower()
        self._valid_mode()
        self._tickets = tickets
        self._valid_tickets()
        self._happy_tickets = 0
        self._result = ''
        self._start_mode = self.MODES[self._mode]

    def main(self) -> str:
        for ticket in self._tickets:
            self._start_mode(ticket)
        self._result = f'There are {self._happy_tickets} ' \
                       f'happy {self._mode.lower()} tickets'
        return self._result

    def moscow_mode(self, ticket: str) -> int:
        ticket = str(abs(int(ticket)))
        if self._is_happy_moscow(ticket):
            self._happy_tickets += 1
        return self._happy_tickets

    def peter_mode(self, ticket: str) -> int:
        ticket = str(abs(int(ticket)))
        if self._is_happy_peter(ticket):
            self._happy_tickets += 1
        return self._happy_tickets

    def _valid_mode(self):
        if self._mode not in self.MODES:
            raise KeyError(ERR_MSG['mode'])

    def _valid_tickets(self):
        for ticket in self._tickets:
            if len(ticket) != 6 or not ticket.isnumeric():
                raise ValueError(f'{ticket} {ERR_MSG["ticket"]}')

    @staticmethod
    def _is_happy_moscow(ticket) -> bool:
        first_part = [int(d) for d in ticket[:3]]
        second_part = [int(d) for d in ticket[3:]]
        if sum(first_part) == sum(second_part):
            return True
        return False

    @staticmethod
    def _is_happy_peter(ticket) -> bool:
        even_digits = sum([int(d) for d in ticket if int(d) % 2 == 0])
        odd_digits = sum([int(d) for d in ticket if int(d) % 2 == 1])
        if even_digits == odd_digits:
            return True
        return False

    def __repr__(self) -> str:
        return self._result


if __name__ == "__main__":
    main()

    M = TicketsCheckHappy(['253145', '545626', '111111'], 'MoskoW')
    print(M.main())

    P = TicketsCheckHappy(['121358', '278561'], 'pIteR')
    print(P.main())
