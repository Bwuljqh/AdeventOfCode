from os import path
import re
from parse import parse

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')

INPUTS = ''.join(stream.replace('\n', '') for stream in file.readlines())

match = [(i.start(), i.group()) for i in re.finditer(r"mul\([0-9]+,[0-9]+\)", INPUTS)]
match.sort(key=lambda x: x[0])
match_do = [i for i in re.finditer(r"do\(\)|don't\(\)", INPUTS)]

sum_total_part_1 = 0
sum_total_part_2 = 0

mult = 1
for i in match_do:
    if i.group() == 'don\'t()':
        new_mult = 0
    else:
        new_mult = 1

    while match[0][0] < i.start():
        parsed = parse('mul({},{})', match.pop(0)[1])
        sum_total_part_1 += int(parsed[0]) * int(parsed[1])
        sum_total_part_2 += int(parsed[0]) * int(parsed[1]) * mult

    mult = new_mult

print("part 1", sum_total_part_1)
print("part 2", sum_total_part_2)
