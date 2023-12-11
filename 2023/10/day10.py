
from os import path
import math

from collections import Counter
import numpy as np
SYMBOLS = {
    '-': {(0, -1): (0, 1), (0, 1): (0, -1)},
    '|': {(1, 0): (-1, 0), (-1, 0): (1, 0)},
    'L': {(-1, 0): (0, 1), (0, 1): (-1, 0)},
    'J': {(-1, 0): (0, -1), (0, -1): (-1, 0)},
    '7': {(0, -1): (1, 0), (1, 0): (0, -1)},
    'F': {(1, 0): (0, 1), (0, 1): (1, 0)}
}


ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input_test.txt'), 'r')
PIPES = [series.replace('\n', '') for series in file.readlines()]


def get_next_pos(previous_pos: tuple[int, int], current_pos: tuple[int, int]):
    symbol = PIPES[current_pos[0]][current_pos[1]]
    diff_pos = (previous_pos[0] - current_pos[0], previous_pos[1] - current_pos[1])
    next_pos_diff = SYMBOLS[symbol][diff_pos]
    return (current_pos[0] + next_pos_diff[0], current_pos[1] + next_pos_diff[1])


def find_start(pipes) -> tuple[tuple[int, int], list[tuple[int, int]]]:
    for x in range(len(pipes)):
        for y in range(len(pipes[x])):
            if pipes[x][y] == 'S':
                out_pos = []
                if pipes[x - 1][y] in '7|F':
                    out_pos.append((x - 1, y))
                if pipes[x + 1][y] in 'J|L':
                    out_pos.append((x + 1, y))
                if pipes[x][y - 1] in 'F- L':
                    out_pos.append((x, y - 1))
                if pipes[x][y + 1] in '7-J':
                    out_pos.append((x, y + 1))
                return ((x, y), out_pos)


STARTING_POS, NEXT_POS = find_start(PIPES)
POSITIONS = {STARTING_POS, *NEXT_POS}
right_arm = NEXT_POS[0]
left_arm = NEXT_POS[1]

previous_right = STARTING_POS
previous_left = STARTING_POS
count = 1

loop = [['.'] * len(PIPES[0])]*len(PIPES)

while right_arm != left_arm or right_arm == previous_left or previous_right == left_arm:
    buffer_right = right_arm
    right_arm = get_next_pos(previous_right, right_arm)
    previous_right = buffer_right

    buffer_left = left_arm
    left_arm = get_next_pos(previous_left, left_arm)
    previous_left = buffer_left

    POSITIONS.add(right_arm)
    POSITIONS.add(left_arm)
    count += 1

print(count)

total = 0
for x in range(1, len(PIPES) - 1):
    crossed_y = 0
    previous_symbol = None
    for y in range(len(PIPES[x]) - 1):
        if (x, y) in POSITIONS:
            current_symbol = PIPES[x][y]
            if current_symbol == '-':
                continue
            elif current_symbol == '|':
                crossed_y += 1
            elif previous_symbol is not None:
                match (previous_symbol, current_symbol):
                    case ('L', '7'):
                        crossed_y += 1
                    case ('F', 'J'):
                        crossed_y += 1
                    case _:
                        pass
                previous_symbol = None
            else:
                previous_symbol = current_symbol
        elif crossed_y % 2 == 1:
            total += 1
        # print(f'pos: {x, y}, {"is as pipe" if (x, y) in POSITIONS else ""} crossed: {crossed_y}, total: {total}')
print(total)
