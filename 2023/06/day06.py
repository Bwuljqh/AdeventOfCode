
from os import path

import numpy as np

ITERATIONS = 1

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
almanach = [line.replace('\n', '') for line in file.readlines()]

# Part 1

times = np.array(almanach[0].split(':')[-1].split())
times = np.array([int(time) for time in times])
distances = np.array(almanach[1].split(':')[-1].split())
distances = np.array([int(distance) for distance in distances])

sums = 1

for time_index in range(len(times)):
    time = times[time_index]
    distance = distances[time_index]
    results = np.array([pos * (time - pos) for pos in range(time)])
    sums *= sum(np.where(results > distance, True, False))

print(sums)

# Part 2

time = int("".join(almanach[0].split(':')[-1].split()))
distance = int("".join(almanach[1].split(':')[-1].split()))

delta = time**2 - 4 * distance

root_1 = -time + (delta**0.5)/2
root_2 = -time - (delta**0.5)/2

# sums = sum(second * (time - second) > distance for second in range(time))

print(int(root_1) - int(root_2) + 1)
