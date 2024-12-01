import time
from collections import Counter
from os import path
from typing import List, Tuple

import numpy as np
from more_itertools import distinct_permutations

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
springs = [spring.replace('\n', '').split(' ') for spring in file.readlines()]


class Spring:
    def __init__(self, spring: str, numbers: str) -> None:
        self.spring = spring
        self.numbers = numbers


# def can_be_placed_here(spring: str, length: int, pos: int) -> bool:
#     new_spring =
#     pass

def replace_question_mark(spring: str, combinaison: str):
    new_spring = ''
    index = 0
    for i in spring:
        if i == '?':
            new_spring += combinaison[index]
            index += 1
        else:
            new_spring += i
    return new_spring


def get_numbers(spring) -> str:
    return [len(i) for i in spring.split('.') if '#' in i]


old_springs = []
for spring, values in springs:
    old_springs.append(('?'.join([spring]), [int(value) for value in values.split(',')]))

new_springs = []
for spring, values in springs:
    new_springs.append(('?'.join([spring]*5), [int(value) for value in values.split(',')]*5))
# print(new_springs)
# counter = Counter(springs[1][0])
# total_hash = sum(int(i) for i in springs[1][1].split(','))

# question_marks = counter['?']
# hash_counter = counter['#']
# print(f'hash_nbr: {hash_counter}, total_hash: {total_hash}, question_marks: {question_marks}')
# start = time.time()
# print(len(list(distinct_permutations('.'*(question_marks - total_hash + hash_counter)+'#'*(total_hash - hash_counter), question_marks))))
# print(time.time() - start)


def count_options(spring: str, numbers: List[int], index=0, number_index=0, current_length=0, memo=None) -> int:
    if memo is None:
        memo = {}

    # Memoization key updated to include the entire spring state for accuracy
    memo_key = (spring, number_index, current_length)
    if memo_key in memo:
        return memo[memo_key]

    total = 0
    counter = current_length
    if '?' not in spring and get_numbers(spring) == numbers:
        return 1
    for i in range(index, len(spring)):
        char = spring[i]
        if char == '.':
            if counter != 0:
                if number_index >= len(numbers):
                    return 0
                if counter < numbers[number_index]:
                    return 0
            continue
        if char == '#':
            counter += 1
            if number_index >= len(numbers):
                return 0
            if counter == numbers[number_index]:
                try:
                    if spring[i + 1] == '#':
                        return 0
                    if spring[i + 1] == '?':
                        return count_options(spring[:i + 1] + '.' + spring[i+2:], numbers, i+1, number_index+1, 0)
                except IndexError:
                    pass
                number_index += 1
                counter = 0
        if char == '?':
            total += count_options(spring[:i] + '#' + spring[i+1:], numbers, i, number_index, counter, memo)
            total += count_options(spring[:i] + '.' + spring[i+1:], numbers, i, number_index, counter, memo)
            break
    memo[memo_key] = total
    return total


def count_options_refined(spring: str, numbers: List[int], index=0, number_index=0, current_length=0, memo=None) -> int:
    if memo is None:
        memo = {}

    # Memoization key updated to include the entire spring state for accuracy
    memo_key = (spring, number_index, current_length)
    if memo_key in memo:
        return memo[memo_key]

    total = 0
    if '?' not in spring:
        if get_numbers(spring) == numbers:
            return 1
        else:
            return 0

    for i in range(index, len(spring)):
        char = spring[i]
        if char == '.':
            if current_length != 0:
                if number_index >= len(numbers) or current_length < numbers[number_index]:
                    return 0
            continue
        elif char == '#':
            current_length += 1
            if number_index >= len(numbers) or current_length > numbers[number_index]:
                return 0
            if current_length == numbers[number_index]:
                if i + 1 < len(spring) and spring[i + 1] == '#':
                    return 0
                number_index += 1
                current_length = 0
        elif char == '?':
            # Recursively calculate for both '#' and '.' possibilities
            total += count_options_refined(spring[:i] + '#' + spring[i+1:], numbers, i, number_index, current_length, memo)
            total += count_options_refined(spring[:i] + '.' + spring[i+1:], numbers, i, number_index,
                                           current_length if current_length < numbers[number_index] else 0, memo)
            break

    memo[memo_key] = total
    return total

# print(count_options(new_springs[0][0], new_springs[0][1]))
# print(count_options(new_springs[1][0], new_springs[1][1]))
# print(count_options(new_springs[2][0], new_springs[2][1]))
# print(count_options(new_springs[3][0], new_springs[3][1]))
# print(count_options(new_springs[4][0], new_springs[4][1]))
# print(count_options(new_springs[5][0], new_springs[5][1]))
# print(count_options(new_springs[7][0], new_springs[7][1]))
# print(count_options(new_springs[8][0], new_springs[8][1]))
# exit()

# First Part


start = time.time()
total = 0
for spring, value in old_springs:
    temp = count_options(spring, value)
    total += temp
    # print(temp)
print(f'total {total}')
print(time.time() - start)

# Second part
start = time.time()
total = 0
index = 0
for spring, value in new_springs:
    temp = count_options(spring, value)
    total += temp
    print(temp, index)
    index += 1
print(f'total {total}')
print(time.time() - start)

# First Part Ugly

exit()

start = time.time()
count = 0
for spring, values in springs:
    counter = Counter(spring)
    total_hash = sum(int(i) for i in values.split(','))
    question_marks = counter['?']
    hash_counter = counter['#']
    # print(set(permutations('.'*question_marks+'#'*question_marks, question_marks)))
    # print(f'hash_nbr: {hash_counter}, total_hash: {total_hash}, question_marks: {question_marks}')
    for combination in distinct_permutations('.'*(question_marks - total_hash + hash_counter)+'#'*(total_hash - hash_counter), question_marks):
        new_spring = replace_question_mark(spring, combination)
        if get_numbers(new_spring) == values:
            count += 1

# print(count)
# print(time.time() - start)
