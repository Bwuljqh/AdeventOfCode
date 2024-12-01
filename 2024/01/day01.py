
from os import path
from collections import Counter
import numpy as np
import itertools

itertools.permutations

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')


INPUTS = np.array([stream.replace('\n', '').split() for stream in file.readlines()]).T.astype("int")

print("First start", sum(abs(np.sort(INPUTS[0]) - np.sort(INPUTS[1]))))

left_list = dict(Counter(INPUTS[0]))
right_list = dict(Counter(INPUTS[1]))


print("Second star", sum([right_list.get(key, 0)*value*key for key, value in left_list.items()]))