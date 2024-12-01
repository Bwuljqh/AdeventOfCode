
from os import path
import math
from pprint import pprint
from collections import Counter
import numpy as np
import itertools

itertools.permutations

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
GALAXIES = np.array([stream.replace('\n', '') for stream in file.readlines()])
EXPANSION_VALUE = 1000000 - 1


class Galaxy():

    def __init__(self, x, y, number) -> None:
        self.x = x
        self.y = y
        self.number = number

    def find_distance(self, other, expansion):
        dist_x = abs(self.x - other.x)
        dist_y = abs(self.y - other.y)
        for row, value in expansion['row'].items():
            if (row > self.x and other.x > row) or (row > other.x and self.x > row):
                dist_x += value
        for col, value in expansion['col'].items():
            if (col > self.y and other.y > col) or (col > other.y and self.y > col):
                dist_y += value
        return dist_x + dist_y

    def __repr__(self) -> str:
        return f'Galaxy {self.number}: ({self.x}, {self.y})'


def find_galaxies(galaxies_maps) -> tuple[list[Galaxy], set[int], set[int]]:
    galaxies = []
    used_x = set()
    used_y = set()
    count = 1
    for x in range(len(galaxies_maps)):
        for y in range(len(galaxies_maps[x])):
            if galaxies_maps[x][y] == '#':
                galaxies.append(Galaxy(x, y, count))
                count += 1
                used_x.add(x)
                used_y.add(y)
    return galaxies, used_x, used_y


galaxies, used_x, used_y = find_galaxies(GALAXIES)

EXPANSION = {'row': {}, 'col': {}}
for x in range(len(GALAXIES)):
    if x not in used_x:
        EXPANSION['row'][x] = EXPANSION_VALUE
for y in range(len(GALAXIES[0])):
    if y not in used_y:
        EXPANSION['col'][y] = EXPANSION_VALUE

total = 0
for galaxy_1, galaxy_2 in itertools.combinations(galaxies, 2):
    total += galaxy_1.find_distance(galaxy_2, EXPANSION)
print(total)
