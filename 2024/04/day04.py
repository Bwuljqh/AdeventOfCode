from os import path
import numpy as np
from typing import Type
from collections import Counter

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')

WORD = 'XMAS'
INPUTS = [stream.replace('\n', '') for stream in file.readlines()]

DIRECTIONS = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
]
DIRECTIONS_LIGHT = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
]

Coords = Type[tuple[int, int]]


def check_word_part_1(grid: list[str], pos: Coords, previous_pos: list[Coords] = [], word=WORD):
    counter = 0
    iteration = len(previous_pos)

    letter_to_find = word[iteration + 1]
    end = letter_to_find == word[-1]

    directions = DIRECTIONS
    if previous_pos:
        directions = [(pos[0] - previous_pos[-1][0], pos[1] - previous_pos[-1][1])]

    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if any(np.sign(coord) == -1 for coord in new_pos):
            continue
        try:
            new_letter = grid[new_pos[0]][new_pos[1]]
        except IndexError:
            continue
        if new_letter == letter_to_find:
            if end is True:
                return 1
            else:
                counter += check_word_part_1(grid, new_pos, previous_pos + [pos])
    return counter


def check_word_part_2(a_list: list[Coords], grid: list[str], pos: Coords, previous_pos: list[Coords] = [], word=WORD):
    counter = 0
    iteration = len(previous_pos)
    letter_to_find = word[iteration + 1]
    end = letter_to_find == word[-1]

    directions = DIRECTIONS_LIGHT
    if previous_pos:
        directions = [(pos[0] - previous_pos[-1][0], pos[1] - previous_pos[-1][1])]

    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if any(np.sign(coord) == -1 for coord in new_pos):
            continue
        try:
            new_letter = grid[new_pos[0]][new_pos[1]]
        except IndexError:
            continue
        if new_letter == letter_to_find:
            if end is True:
                a_list.append(pos)
                return 1
            else:
                counter += check_word_part_2(a_list, grid, new_pos, previous_pos + [pos], word)
    return counter


counter_part_1 = 0
counter_part_2 = 0
a_list = []

for x in range(len(INPUTS)):
    for y in range(len(INPUTS[x])):
        if INPUTS[x][y] == WORD[0]:
            counter_part_1 += check_word_part_1(INPUTS, (x, y), [])
        if INPUTS[x][y] == WORD[1]:
            counter_part_2 += check_word_part_2(a_list, INPUTS, (x, y), [], "MAS")

print("part 1", counter_part_1)
print("part 2", len([i for i in dict(Counter(a_list)).values() if i == 2]))
