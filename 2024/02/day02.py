
import copy
from os import path
from collections import Counter
import numpy as np
import itertools

itertools.permutations

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')

# for stream in file.readlines():
#     print(stream.replace('\n', '').split())
# exit()


INPUTS = [np.array((stream.replace('\n', '').split())).astype("int") for stream in file.readlines()]

counter = 0


def test_list(result) -> tuple[bool, None | int]:
    sign = np.sign(result[0])
    for i in range(len(result)):
        diff = result[i]
        if abs(diff) not in [1, 2, 3] or np.sign(diff) != sign:
            return False, i
    return True, None


for data in INPUTS:
    result = data[1:] - data[:-1]
    test = test_list(result)
    if test[0]:
        counter += 1
    else:
        for i in [test[1] - 1, test[1], test[1] + 1]:
            if i > len(data) or i < 0:
                continue
            data_copy = list(copy.copy(data))
            data_copy.pop(i)
            data_copy = np.array(data_copy)
            if test_list(data_copy[1:] - data_copy[:-1])[0]:
                counter += 1
                break
print(counter)
