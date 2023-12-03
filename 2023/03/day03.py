from os import path
from numpy import sign
OFFSETS = [(-1, -1),
           (-1, 0),
           (-1, 1),
           (0, -1),
           (0, 1),
           (1, -1),
           (1, 0),
           (1, 1)]

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
schematic = [schematic_line.replace('\n', '') for schematic_line in file.readlines()]


def find_numbers(x: int, y: int, schematic: list[str]) -> list[tuple[int, tuple[int, int], int]]:
    numbers = []
    for offset_x, offset_y in OFFSETS:
        try:
            if schematic[x + offset_x][y + offset_y].isdigit():
                numbers.append(get_number_from_pos(x + offset_x, y + offset_y, schematic))
        except IndexError:
            continue
    return numbers


def get_number_from_pos(x: int, y: int, schematic: list[str]) -> tuple[int, tuple[int, int], int]:
    number = schematic[x][y]
    starting_pos = 0
    try:
        char = schematic[x][y - 1]
        if char.isdigit():
            number = char + number
            starting_pos -= 1
            next_char = schematic[x][y - 2]
            if next_char.isdigit():
                number = next_char + number
                starting_pos -= 1
    except IndexError:
        pass

    try:
        char = schematic[x][y + 1]
        if char.isdigit():
            number += char
            next_char = schematic[x][y + 2]
            if next_char.isdigit():
                number += next_char
    except IndexError:
        pass
    return (int(number), (x, y + starting_pos), len(number))


# Part 1
starting_pos: set[tuple] = set()
total = 0
for x in range(len(schematic)):
    for y in range(len(schematic[x])):
        char = schematic[x][y]
        if char != '.' and not char.isdigit():
            numbers = find_numbers(x, y, schematic)
            for number in numbers:
                if number[1] not in starting_pos:
                    total += number[0]
                    starting_pos.add(number[1])
print(total)

# Part 2
starting_pos: set[tuple] = set()
total = 0
for x in range(len(schematic)):
    for y in range(len(schematic[x])):
        char = schematic[x][y]
        if char == '*':
            numbers = list(set(find_numbers(x, y, schematic)))
            if len(numbers) == 2:
                total += numbers[0][0] * numbers[1][0]
print(total)
