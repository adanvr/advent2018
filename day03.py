from typing import NamedTuple, Tuple
import re
from collections import Counter

regex = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

Coord = Tuple[int, int]

class Rectangle(NamedTuple):
    '''
    Create class in order to represent a rectangle of fabric from AoC.
    '''
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim):
        #Method aimed at parsing relevant info from AoC data
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(regex, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)

    def all_squares(self):
        for i in range(self.x_lo, self.x_hi):
            for j in range(self.y_lo, self.y_hi):
                yield (i, j)


assert Rectangle.from_claim("#123 @ 3,2: 5x4") == Rectangle(123, 3, 2, 8, 6)

def coverage(rectangles):
    counts = Counter()
    for rectangle in rectangles:
        for coord in rectangle.all_squares():
            counts[coord] += 1

    return counts


def multi_claimed(data):
    rectangles = [Rectangle.from_claim(datum) for datum in data]
    counts = coverage(rectangles)

    return len([count for count in counts.values() if count >= 2])

test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
assert multi_claimed(test_data) == 4

with open('data/input03.txt') as f:
    data= [line.strip() for line in f]

print(multi_claimed(data))

def non_overlapping_claim(data):
    rectangles = [Rectangle.from_claim(datum) for datum in data]
    counts = coverage(rectangles)

    good_rectangles = [rectangle
                       for rectangle in rectangles
                       if all(counts[coord] == 1 for coord in rectangle.all_squares())]

    assert len(good_rectangles) == 1

    return good_rectangles[0].id

assert non_overlapping_claim(test_data) == 3

print(non_overlapping_claim(data))