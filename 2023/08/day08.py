
from os import path
import math

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
maps = [map.replace('\n', '') for map in file.readlines()]

instructions = maps[0]
starting_nodes = []
maps_dict = {}
for map in maps[2:]:
    key, values = map.split(' = ')
    left, right = values.strip('()').split(', ')
    maps_dict[key] = {'R': right, 'L': left}
    if key.endswith('A'):
        starting_nodes.append(maps_dict[key])

index = 0
current_item_name = 'AAA'
current_item = maps_dict['AAA']

steps = 0
while True:
    if current_item_name == 'ZZZ':
        print(steps)
        break
    current_item_name = current_item[instructions[index]]
    current_item = maps_dict[current_item_name]
    index = (index + 1) % len(instructions)
    steps += 1


index = 0
steps = 0
steps_stop = []
full_tour = 0
while True:
    steps += 1
    names = []
    new_nodes = []
    for node in starting_nodes:
        current_item_name = node[instructions[index]]
        if current_item_name.endswith('Z'):
            steps_stop.append((steps + 1) // len(instructions))
        else:
            new_nodes.append(maps_dict[current_item_name])
            names.append(current_item_name)
    if not new_nodes:
        break
    index = (index + 1) % len(instructions)
    starting_nodes = new_nodes

print(math.lcm(*steps_stop)*len(instructions))
