from tringleslist import TrianglesList

if __name__ == "__main__":
    with open('MOCK_DATA.csv', 'r', encoding='utf-8') as f:
        TrianglesList(f.readlines())
