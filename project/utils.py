"""Declare utility modules."""


def generate_big_file():
    """Prints big file of our structure."""
    import random
    import datetime

    # declaring columns
    print(',',  end='')
    columns_declaration = []
    for i in range(50):
        columns_declaration.append(f'col{i}')
    print(','.join(columns_declaration))

    # creating all columns
    SIZE = 3 * (10 ** 6)
    for _ in range(SIZE):
        print(datetime.datetime.now(), end=',')
        data = []
        for i in range(50):
            data.append(str(random.random()))
        print(','.join(data))


def main():
    """Start main utils module."""
    generate_big_file()


if __name__ == '__main__':
    generate_big_file()
