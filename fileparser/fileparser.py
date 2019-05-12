import fileinput


class FileParser:

    def __init__(self, filepath: str,
                 string_to_count: str,
                 string_to_replace=None):
        self.filename = filepath
        self.string_to_count = string_to_count
        self.occurrences = 0
        if string_to_replace is None:
            self.count_occurrences()
            self.__repr__()
        else:
            self.string_to_search = str(string_to_count)
            self.string_to_replace = str(string_to_replace)
            self.replace_string()

    def __repr__(self):
        print(f'{self.string_to_count} --> {self.occurrences} times')

    def count_occurrences(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                self.occurrences += line.count(self.string_to_count)

    def replace_string(self):
        with open(self.filename, 'r+', encoding='utf-8') as f:
            for line in fileinput.input(self.filename):
                f.write(line.replace(self.string_to_search,
                                        self.string_to_replace))
