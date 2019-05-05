from datetime import date


class PersonTest:

    def __init__(self, data='Petrov Ivan Aleksiyovich,05/03/1979,22/07/2019,12:20-13:17,190'):
        self.data = data
        self.today = date.today()
        self.name_template = ['surname', 'name', 'fathersname']
        self.date_template = ['dd', 'mm', 'yy']
        self.time_template = ['hh', 'mm']
        fullname, birthday, test_date, start_end_test_time, mark = [e for e in self.data.split(',')]
        self.fullname = dict(zip(self.name_template, [name for name in fullname.split(' ')]))
        self.age = self.findage(birthday)
        start_time, end_time = self.preparetime(start_end_test_time)
        self.test_time = self.calctime(start_time, end_time)
        self.print_result()

    def findage(self, birthdate: str):
        birthdate = dict(zip(self.date_template, [int(date) for date in birthdate.split('/')]))
        return self.today.year - birthdate['yy'] - ((self.today.month, self.today.day) < (birthdate['mm'], birthdate['dd']))

    def calctime(self, start_time: dict, end_time: dict):
        """
        Function calculate how many time was spent to pass test
        :param start_time: {'hh':12, 'mm':20}
        :param end_time: {'hh':13, 'mm':17}
        :return: {'hh':0, 'mm':57}
        """
        day_in_hours = 24*60
        start_time, end_time = self.time_in_minutes(start_time, end_time)
        if start_time > end_time:
            test_time = end_time - start_time + day_in_hours
        else:
            test_time = end_time - start_time
        return dict(zip(self.time_template, [int(test_time // 60), int(test_time % 60)]))

    def time_in_minutes(self, start_time: dict, end_time: dict):
        return start_time['hh'] * 60 + start_time['mm'], end_time['hh'] * 60 + end_time['mm']

    def preparetime(self, string_time: str):
        """
        Convert time string to two dicts: start_time={'hh': hh,'mm': mm}, end_time={'hh': hh,'mm': mm}
        :param string_time: 12:20-13:17
        :return: {'hh':12, 'mm':20}, {'hh':13, 'mm':17}
        """
        start_time, end_time = string_time.split('-')
        start_time = dict(zip(self.time_template, [int(tt) for tt in start_time.split(':')]))
        end_time = dict(zip(self.time_template, [int(tt) for tt in end_time.split(':')]))
        return start_time, end_time

    def print_result(self):
        print('{} {}.{}.\nAge: {}.\nTest time: {}:{}'.format(self.fullname['surname'],
                                                             self.fullname['name'][0],
                                                             self.fullname['fathersname'][0],
                                                             self.age,
                                                             self.test_time['hh'],
                                                             self.test_time['mm']))
