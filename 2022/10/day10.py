from __future__ import annotations

import time
from enum import Enum
from os import path
from typing import List, Tuple

import numpy as np
import parse
from scipy.spatial import distance

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay10.txt'), 'r')

commands: List[str] = [command.replace('\n', '') for command in file.readlines()]

SYMBOL_FILL = '⬜'
SYMBOL_SPACE = '⬛'
cycles = []
x = 1
p = parse.compile("addx {}")
drawing = ''
index = 0
for command in commands:
    parsed_command = p.parse(command)
    drawing += SYMBOL_FILL if index % 40 in [x - 1, x, x + 1] else SYMBOL_SPACE
    index += 1
    cycles.append(x)
    if parsed_command is not None:
        drawing += SYMBOL_FILL if index % 40 in [x - 1, x, x + 1] else SYMBOL_SPACE
        index += 1
        print(f'x: {x} value to add: {parsed_command[0]}')
        x += int(parsed_command[0])
        cycles.append(x)

# print(sum((cycles[18 + 40*cursor] * (20 + 40*cursor) for cursor in range(6))))

print(drawing[:40])
print(drawing[40:80])
print(drawing[80:120])
print(drawing[120:160])
print(drawing[160:200])
print(drawing[200:240])
