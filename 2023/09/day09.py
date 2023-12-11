
from os import path
import math

from collections import Counter

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
series_list = [series.replace('\n', '') for series in file.readlines()]

series = [int(num) for num in series_list[2].split()]


def find_next_value(series: list[int]):
    diff_series = [series[i] - series[i - 1] for i in range(1, len(series))]
    set_diff = set(diff_series)
    if len(set_diff) == 1:
        return set_diff.pop() + series[-1]
    else:
        return find_next_value(diff_series) + series[-1]


def find_previous_value(series: list[int]):
    diff_series = [series[i] - series[i - 1] for i in range(1, len(series))]
    set_diff = set(diff_series)
    if len(set_diff) == 1:
        return series[0] - set_diff.pop()
    else:
        return series[0] - find_previous_value(diff_series)


total_next_value = 0
total_previous_value = 0
for series in series_list:
    integer_list = [int(num) for num in series.split()]
    total_next_value += find_next_value(integer_list)
    total_previous_value += find_previous_value(integer_list)

print(f'sum next values: {total_next_value}')
print(f'sum previous values: {total_previous_value}')
