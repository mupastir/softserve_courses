class PersonTest:

    def __init__(self, data='Petrov Ivan Aleksiyovich,05/03/1979,22/07/2019,12:20-13:17,190'):
        self.data = data

    def __repr__(self):
        result_string = '{} {}.{}.\nAge: {}.\nTest time: {}:{}'.format(self.fullname[0],
                                                                       self.fullname[1][0],
                                                                       self.fullname[2][0],
                                                                       self.age,
                                                                       self.test_time[0],
                                                                       self.test_time[1])
        return print(result_string)

    def __call__(self):
        fullname, birthday, test_date, start_end_test_time, mark = [e for e in self.data.split(',')]
        self.fullname = [name for name in fullname.split(' ')]
        self.age = self.__findage__(birthday)
        start_time, end_time = self.__preparetime__(start_end_test_time)
        self.test_time = self.__calctime__(start_time, end_time)
        return self.__repr__()

    def __findage__(self, birthdate: str):
        from datetime import date
        today = date.today()
        birthdate = [int(date) for date in birthdate.split('/')]
        return today.year - birthdate[2] - ((today.month, today.day) < (birthdate[1], birthdate[0]))

    def __calctime__(self, start_time: list, end_time: list):
        start_time = start_time[0] * 60 + start_time[1]
        end_time = end_time[0] * 60 + end_time[1]
        if start_time > end_time:
            test_time = end_time - start_time + 1440
        else:
            test_time = end_time - start_time
        return [int(test_time // 60), int(test_time % 60)]

    def __preparetime__(self, string_time: str):
        """
        Convert time string to two lists: start_time=[hh, mm], end_time=[hh, mm]
        :param string_time: 12:20-13:17
        :return: [12, 20], [13, 17]
        """
        start_time, end_time = [t for t in string_time.split('-')]
        start_time = [int(tt) for tt in start_time.split(':')]
        end_time = [int(tt) for tt in end_time.split(':')]
        return start_time, end_time
