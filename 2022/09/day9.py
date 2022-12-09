from __future__ import annotations

from enum import Enum, auto
from os import path
from typing import List, Optional, Tuple

from scipy.spatial import distance
import numpy as np
ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay9.txt'), 'r')

instructions: List[str] = [instrutction.replace('\n', '') for instrutction in file.readlines()]


class Direction(Enum):
    U = (1, 0)
    R = (0, 1)
    D = (-1, 0)
    L = (0, -1)


def move_tail(head_coord: Tuple[int, int], tail_coord: Tuple[int, int]) -> Tuple[int, int]:
    h_x = head_coord[0]
    h_y = head_coord[1]
    t_x = tail_coord[0]
    t_y = tail_coord[1]
    x_dist = h_x - t_x
    y_dist = h_y - t_y
    return (t_x + np.sign(x_dist), t_y + np.sign(y_dist)) if distance.euclidean((h_x, h_y), (t_x, t_y)) > 1.5 else tail_coord


tiles_visited_9: List[Tuple[int, int]] = [(0, 0)]
tiles_visited_2: List[Tuple[int, int]] = [(0, 0)]

nots: List[Tuple[int, int]] = [(0, 0) for _ in range(10)]

for instruction in instructions:
    direction, number_of_moves = instruction.split(' ')
    direction = Direction[direction]
    number_of_moves = int(number_of_moves)

    for _ in range(number_of_moves):
        nots[0] = (nots[0][0] + direction.value[0], nots[0][1] + direction.value[1])
        for not_position in range(1, len(nots)):
            tail_position = move_tail(nots[not_position - 1], nots[not_position])
            nots[not_position] = tail_position
        if nots[-1] not in tiles_visited_9:
            tiles_visited_9.append(nots[-1])
        if nots[1] not in tiles_visited_2:
            tiles_visited_2.append(nots[1])

print(len(tiles_visited_2))
print(len(tiles_visited_9))
