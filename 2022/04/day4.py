import string
from os import path
from typing import List

string.ascii_lowercase.index('b')

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay4.txt'), 'r')

elves_ranges: List[str] = [elves_range.replace('\n', '') for elves_range in file.readlines()]

count_included = 0
count_overlap = 0
for elves_range in elves_ranges:

    elf1, elf2 = elves_range.split(',')

    elf1_range = elf1.split('-')
    range_1 = set(range(int(elf1_range[0]), int(elf1_range[1]) + 1))
    elf2_range = elf2.split('-')
    range_2 = set(range(int(elf2_range[0]), int(elf2_range[1]) + 1))

    if range_1.issubset(range_2) or range_2.issubset(range_1):
        count_included += 1
    if not range_1.isdisjoint(range_2):
        count_overlap += 1

print(count_included)
print(count_overlap)
