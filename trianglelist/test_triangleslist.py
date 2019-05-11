import io
import unittest.mock
from tringleslist import TrianglesList


class TestTriangle(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, required_string, mock_stdout, data=None):
        TrianglesList(data)
        self.assertEqual(mock_stdout.getvalue(), required_string)

    def test_basic(self):
        with open('triangles.csv', 'r', encoding='utf-8') as f:
            self.assert_stdout('=================Triangles List:'
                               '==================\n'
                               '1. [Triangle Cucumber]: 41.57 cm\n'
                               '2. [Triangle Ternar]: 14.99 cm\n'
                               '3. [Triangle micRO]: 0.45 cm\n',
                               data=f.readlines())


if __name__ == "__main__":
    unittest.main()
