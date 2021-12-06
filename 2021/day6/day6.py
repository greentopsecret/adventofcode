"""
"""
from collections import defaultdict


def get_frequencies(data) -> dict:
    frequencies = defaultdict(int)
    for number in data:
        frequencies[number] += 1

    return frequencies


def parse(data: str):
    return (int(x) for x in data.split(','))


def task(data: str, days: int) -> int:
    data = parse(data)
    frequencies = get_frequencies(data)
    frequencies_updated = defaultdict(int)
    for _ in range(0, days):
        for i in range(9):
            if i == 0:
                frequencies_updated[8] = frequencies[0]
                frequencies_updated[6] += frequencies[0]
            else:
                frequencies_updated[i - 1] += frequencies[i]
        frequencies = frequencies_updated
        frequencies_updated = defaultdict(int)

    return sum(frequencies.values())


def task2(data):
    pass


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        _data = f.read()
        print('Result for the part 1: %s' % task(_data, days=80))
        print('Result for the part 2: %s' % task(_data, days=256))
