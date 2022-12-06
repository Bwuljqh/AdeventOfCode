from os import path
import pprint
from typing import List, Tuple

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay6.txt'), 'r')

signal: str = [instruction.replace('\n', '') for instruction in file.readlines()][0]

START_OF_MESSAGE_MARKER_LENGHT = 14

for cursor in range(len(signal)-START_OF_MESSAGE_MARKER_LENGHT):
    if len(set(signal[cursor:cursor+START_OF_MESSAGE_MARKER_LENGHT])) == START_OF_MESSAGE_MARKER_LENGHT:
        print(cursor + START_OF_MESSAGE_MARKER_LENGHT)
        exit()
