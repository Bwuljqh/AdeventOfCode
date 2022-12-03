import string
from os import path

string.ascii_lowercase.index('b')

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay3.txt'), 'r')

sacks = [sack.replace('\n', '') for sack in file.readlines()]


def get_letter_value(letter: str):
    if letter.isupper():
        return string.ascii_uppercase.index(letter) + 1 + 26
    elif letter.islower():
        return string.ascii_lowercase.index(letter) + 1


intersections = (set(sack[:int(len(sack)/2)]).intersection(set(sack[int(len(sack)/2):])) for sack in sacks)
print(sum(get_letter_value(intersection.pop()) for intersection in intersections))

badges = 0
for sack in range(int(len(sacks)/3)):
    badges += get_letter_value(set(sacks[3*sack]).intersection(set(sacks[3*sack + 1])).intersection(set(sacks[3*sack + 2])).pop())
print(badges)
