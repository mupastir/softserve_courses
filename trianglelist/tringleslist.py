class TrianglesList:

    def __init__(self, params_string: str):
        self.template_data = ['name', 'side-a', 'side-b', 'side-c']
        self.data = params_string.split(',')
        self.__repr__()

    def __repr__(self):
        print(f'{"Triangles List:":=^45}')
