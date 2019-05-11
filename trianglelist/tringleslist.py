class TrianglesList:

    def __init__(self, params_string):
        self.template_data = self.get_header(params_string)
        self.data = self.get_data(params_string)
        self.append_squares()
        self.is_exist_triangle()
        self.__repr__()

    def get_header(self, params):
        list_to_strip = params[0].split(',')
        complete_template = [e.strip() for e in list_to_strip]
        return complete_template

    def get_data(self, params):
        values_to_dict = [e.split(',') for e in params][1:]
        data_to_work = [dict(zip(self.template_data,
                                 [el.strip() for el in e]))
                        for e in values_to_dict]
        return data_to_work

    def append_squares(self):
        for e in self.data:
            e['square'] = self.calculate_squares(e)

    def is_exist_triangle(self):
        for e in self.data:
            try:
                e['square'] = float(e['square'])
                if e['square'] == 0.0:
                    raise TypeError
            except TypeError:
                print(f'Triangle {e["name"]} can\'t exist')
                self.data.remove(e)
                return self.is_exist_triangle()

    def calculate_squares(self, values_dict):
        """
        Calculate square of triangle by Heron's formula.
        S = sqrt(p * (p-a) * (p-b) * (p-c)),
        where p = (a+b+c) / 2
        :param values_dict:
        :return:
        """
        semi_perimeter = (float(values_dict[self.template_data[1]]) +
                          float(values_dict[self.template_data[2]]) +
                          float(values_dict[self.template_data[3]])) / 2
        semi_a = semi_perimeter - float(values_dict[self.template_data[1]])
        semi_b = semi_perimeter - float(values_dict[self.template_data[2]])
        semi_c = semi_perimeter - float(values_dict[self.template_data[3]])
        square = (semi_perimeter * semi_a * semi_b * semi_c)**0.5
        return square

    def __repr__(self):
        print(f'{"Triangles List:":=^50}')
        for index, values in enumerate(sorted(self.data,
                                              key=lambda x: x['square'],
                                              reverse=True), 1):
            print(f'{index}. [Triangle {values[self.template_data[0]]}]: '
                  f'{values["square"]:.2f} cm')
