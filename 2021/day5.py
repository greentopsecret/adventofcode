import re
from collections import defaultdict

"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""


def parse_numbers(line):
    return tuple(int(j) for j in re.findall(r'(\d+)', line))


def convert_to_points(numbers) -> tuple:
    return (numbers[0], numbers[1]), (numbers[2], numbers[3])


def get_points(p1, p2):
    x = p1[0]
    y = p1[1]
    while x != p2[0] or y != p2[1]:
        yield x, y
        x += 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
        y += 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0

    yield p2


def task(raw_data, diagonal=True):
    _map = defaultdict(int)
    for line in raw_data.split('\n'):
        numbers = parse_numbers(line)
        if len(numbers) != 4:
            continue

        p1, p2 = convert_to_points(numbers)

        if not diagonal:
            # filter out not horizontal or vertical line
            if p1[0] != p2[0] and p1[1] != p2[1]:
                continue

        for p in get_points(p1, p2):
            _map[p] += 1

    return len([v for v in _map.values() if v > 1])


if __name__ == '__main__':
    with open('data/day5.txt', 'r') as f:
        data = f.read()
        print('Result for the part 1: %s' % task(data, diagonal=False))
        print('Result for the part 2: %s' % task(data, diagonal=True))
