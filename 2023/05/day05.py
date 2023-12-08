import time
from os import path
from typing import Tuple

import numpy as np

ITERATIONS = 1

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
almanach = [line.replace('\n', '') for line in file.readlines()]

seeds = np.array(almanach[0].split(': ')[-1].split())
seeds = np.array([int(seed) for seed in seeds])

# Part 1
index = 1
current_source = seeds
while index < len(almanach):
    line = almanach[index]
    if line.endswith(':'):
        index += 1
        destination_line = len(current_source) * [-1]
        while index < len(almanach):
            line = almanach[index]
            if line == '':
                break
            destination, source, range_len = line.split()
            destination = np.int64(destination)
            source = np.int64(source)
            range_len = np.int64(range_len)
            for seed_index in range(len(current_source)):
                if destination_line[seed_index] == -1:
                    seed = current_source[seed_index]
                    if seed >= source and seed < source + range_len:
                        destination_line[seed_index] = seed - source + destination
            index += 1
        for seed_index in range(len(current_source)):
            if destination_line[seed_index] == -1:
                destination_line[seed_index] = current_source[seed_index]
        current_source = destination_line
    else:
        index += 1

# Part 2


def find_intersection(array: tuple[int, int], filter: tuple[int, int]) -> tuple[tuple[int, int], list[tuple[int, int]]]:
    if array[0] >= filter[0] and array[1] <= filter[1]:
        return array, []
    if array[0] <= filter[0] and array[1] >= filter[1]:
        return (filter[0], filter[1]), [None if array[0] == filter[0] else (array[0], filter[0] - 1),
                                        None if filter[1] == array[1] else (filter[1] + 1, array[1])]
    if array[1] < filter[0] or filter[1] < array[0]:
        return None, []
    if array[1] == filter[0]:
        return (array[1], filter[0]), [(array[0], array[1] - 1)]
    if array[0] == filter[1]:
        return (array[0], filter[1]), [(array[0] + 1, array[1])]
    if array[0] >= filter[0] and array[1] >= filter[1]:
        return (array[0], filter[1]), [None if filter[1] == array[1] else (filter[1] + 1, array[1])]
    if array[0] <= filter[0] and array[1] <= filter[1]:
        return (filter[0], array[1]), [None if array[0] == filter[0] else (array[0], filter[0] - 1)]

    print(array, filter)
    print('An unknown configuration appeared')

    # print(find_intersection((2, 7), (6, 10)))  # (6, 7) [(2, 5)]
    # print(find_intersection((6, 10), (2, 7)))  # (6, 7) [(8, 10)]
    # print(find_intersection((0, 6), (2, 7)))  # (2, 6) [(0, 1)]
    # print(find_intersection((0, 3), (0, 5)))  # (0, 3) []
    # print(find_intersection((0, 2), (1, 2)))  # (1, 2) [(0, 0)]
    # print(find_intersection((0, 3), (4, 7)))  # None, []
    # print(find_intersection((0, 3), (3, 7)))  # (3, 3) [(0, 2)]
    # print(find_intersection((3, 7), (0, 3)))  # (3, 3) [(4, 7)]
    # print(find_intersection((0, 7), (3, 5)))  # (3, 5) [(0,2), (6, 7)]


time_total = 0
counter = 0

# Loop to compute average time
while counter != ITERATIONS:
    new_seeds = [
        (seeds[index * 2], seeds[index * 2 + 1] + seeds[index * 2] - 1)
        for index in range(len(seeds) // 2)
    ]
    new_seeds = sorted(new_seeds, key=lambda x: x[0])

    sections = {}
    current_section = None
    for line in almanach[1:]:
        if line.endswith(':'):
            section_name = line.split(' ')[0].split('-')[-1]
            current_section = len(sections)
            sections[current_section] = {'item': [], 'name': section_name}
        elif line != '':
            destination, source, range_len = line.split()
            destination = np.int64(destination)
            source = np.int64(source)
            range_len = np.int64(range_len)
            sections[current_section]['item'].append([destination, source, range_len])

    start = time.time()
    current_source = new_seeds
    # print(new_seeds)
    for section_number in range(len(sections)):
        section = sections[section_number]
        section_name = section['name']
        section_item = section['item']
        # print(f'starting section {section_name}')
        current_destination = []
        index = 0
        while index < len(current_source):
            # print(len(current_source))
            # Appply each filter to the source
            seed = current_source[index]
            has_intersect = False
            new_arrays = []
            # print(f'\n processing source {seed}\n')
            for destination, source, range_len in section_item:
                # print(f'    applying filter {source, range_len }')
                if seed is None:
                    print(current_source)
                intersect, rest = find_intersection(seed, (source, source + range_len - 1))
                if intersect is not None:
                    has_intersect = True
                    # print(f'    intersection found between {(seed)} and {(source, source + range_len)} : {intersect}')
                    new_arrays.extend(rest_array for rest_array in rest if rest_array is not None)
                    # print(f'             adding to destination: {(intersect[0] - source + destination, intersect[1] - source + destination)} from interesect {intersect} and new start {destination}')
                    current_destination.append((intersect[0] - source + destination, intersect[1] - source + destination))
                    break
            if has_intersect:
                current_source.pop(index)
                index -= 1
            current_source += new_arrays
            index += 1
        current_source = current_destination + current_source
        current_source = sorted(current_source, key=lambda x: x[0])
        # print(f'{section_name}: {current_source}')
        # index_source = 0
        # while index_source < len(current_source) - 1:
        #     cur = current_source[index_source]
        #     next_item = current_source[index_source + 1]
        #     intersect, _ = find_intersection(cur, next_item)
        #     if intersect is not None:
        #         current_source[index_source] = (cur[0], max(cur[1], next_item[1]))
        #         current_source.pop(index_source + 1)
        #     else:
        #         index_source += 1
        # print(f'\nnext source {current_source}\n')

    # print(f'answer: {sorted(current_source, key=lambda x: x[0])[0][0]}')

    time_total += time.time() - start
    counter += 1

print(f'average time in seconds: {time_total / counter}')
print(f'answer: {sorted(current_source, key=lambda x: x[0])[0][0]}')
