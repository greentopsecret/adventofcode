"""
"""


def task1(data: str) -> int:
    data = parse(data)

    return 0


def task2(data: str) -> int:
    data = parse(data)

    return 0


def parse(data: str):
    return (int(x) for x in data.split(','))


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        _data = f.read()
        print('Part 1: %d' % task1(_data))
        # print('Part 2: %d' % task2(_data))
