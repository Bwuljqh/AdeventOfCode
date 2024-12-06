from copy import copy, deepcopy
from pprint import pprint
from os import path
import numpy as np
from typing import Type
from collections import Counter
import time

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')


INPUTS = []

counter = 0
starting_guard_pos = (None, None)

GUARD = '^'
WALL = '#'
X_SYMBOL = 'X'
for stream in file.readlines():
    line = stream.replace('\n', '')
    if GUARD in line:
        starting_guard_pos = (counter, line.find(GUARD))
    INPUTS.append([i for i in line])
    counter += 1

INPUTS = np.array(INPUTS)

INPUTS = np.rot90(INPUTS, axes=(0, 1), k=-1)
copy_inputs = deepcopy(INPUTS)

def rot_point(initial, centre, rotation):

    h, k = centre
    x, y = initial
    angle = rotation*np.pi/2
    return (int(np.round(h+(x - h)*np.cos(angle)-(y-k)*np.sin(angle))), int(np.round(k+(x-h)*np.sin(angle)+(y-k)*np.cos(angle))))


rotation_point = ((len(INPUTS) - 1)/2, (len(INPUTS) - 1)/2)
numbers_of_rotation = -1
guard_pos = rot_point(starting_guard_pos, rotation_point, numbers_of_rotation)


def find_guard(museum, symbol=GUARD):
    for i in range(len(museum)):
        for j in range(len(museum[i])):
            if museum[i, j] == symbol:
                return (i, j)


obstacles_indices = []
start = time.time()


def process(guard_pos=guard_pos, guard_map=INPUTS, numbers_of_rotation=numbers_of_rotation, obstacles_indices=obstacles_indices) -> tuple[bool, np.ndarray | None]:
    positions = set((guard_pos, numbers_of_rotation))
    while True:
        line = guard_map[guard_pos[0], guard_pos[1]:]
        line = list(line)
        if (guard_pos, numbers_of_rotation % 4) in positions:
            return True, None
        else:
            positions.add((guard_pos, numbers_of_rotation % 4))
        if WALL in line:

            stop = line.index(WALL)
            new_line = guard_map[guard_pos[0], guard_pos[1]:stop+guard_pos[1]]
            guard_map[guard_pos[0], guard_pos[1]:stop+guard_pos[1]] = [X_SYMBOL]*len(new_line)
            guard_pos = (guard_pos[0], stop + guard_pos[1] - 1)


            guard_map = np.rot90(guard_map, axes=(0, 1), k=1)
            guard_pos = rot_point(guard_pos, rotation_point, 1)
            numbers_of_rotation += 1

        else:
            guard_map[guard_pos[0], guard_pos[1]:] = [X_SYMBOL]*(len(guard_map) - guard_pos[1])
            break
    return False, INPUTS

start = time.time()
process(guard_map=INPUTS, guard_pos=rot_point(starting_guard_pos, rotation_point, numbers_of_rotation))

print('first part', np.count_nonzero(INPUTS == X_SYMBOL))

INPUTS = np.rot90(INPUTS, axes=(0, 1), k=-numbers_of_rotation - 1)

X = np.where(INPUTS == X_SYMBOL)
obstacles_indices = list(zip(X[0], X[1]))

blocks = 0
for obstacle in obstacles_indices:
    if obstacle == (1,2):
        pass
    copy_guard_map = copy(copy_inputs)
    copy_guard_map[obstacle] = WALL
    result = process(guard_map=copy_guard_map,  guard_pos=rot_point(starting_guard_pos, rotation_point, numbers_of_rotation))
    if result[0]:
        blocks += 1
        
print('second part', blocks)

print(time.time() -start)