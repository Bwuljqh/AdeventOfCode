from __future__ import annotations
import operator
import time
from enum import Enum
from os import path
from typing import Callable, List, Optional, Tuple

import numpy as np
import parse
from scipy.spatial import distance

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay11.txt'), 'r')

monkeys_commands: List[str] = [shenanigans.replace('\n', '') for shenanigans in file.readlines()]

WORRY_DIVISION_AFTER_INSPECTION = 1
NUMBER_OF_MONKEYS = (len(monkeys_commands) + 1) // 7


def add_to_worry(worry, add):
    return worry + add


def multiply_by(worry, mult=None):
    return worry * worry if mult is None else worry * mult


class Monkey:

    def __init__(self) -> None:
        self.initialized = False
        self.inspection_counter = 0

    def construct_monkey(
            self, items: List[int],
            operation: Callable, operator: Optional[int],
            division_condition: int, recipient_if_true: Monkey, recipient_if_false: Monkey) -> None:
        self.items = items
        self.operation = operation
        self.operator = operator
        self.division_condition = division_condition
        self.recipient_if_true = recipient_if_true
        self.recipient_if_false = recipient_if_false
        self.initialized = True

    def inspect_item(self, item) -> None:

        worry = self.operation(item, self.operator)
        worry = worry // WORRY_DIVISION_AFTER_INSPECTION
        if worry % self.division_condition == 0:
            # self.recipient_if_true.catch_item(worry)
            self.recipient_if_true.items = np.append(self.recipient_if_true.items, worry % self.division_condition)
        else:
            # self.recipient_if_false.catch_item(worry)
            self.recipient_if_false.items = np.append(self.recipient_if_false.items, worry % self.division_condition)

    def process_items(self) -> None:
        for item in self.items:
            self.inspect_item(item)
        self.inspection_counter += len(self.items)
        self.items = np.array([])

    def catch_item(self, item: int):
        self.items.append(item)

    def __repr__(self) -> str:
        if self.initialized:
            return f"Monkey with items {self.items}"
        return "Uninitialized monkey"


monkeys = np.array([Monkey() for _ in range(NUMBER_OF_MONKEYS)])

for index in range(len(monkeys)):
    monkey = monkeys[index]
    items = np.array([int(item) for item in parse.parse("  Starting items: {}", monkeys_commands[index*7 + 1])[0].split(', ')])
    division_condition = int(parse.parse("  Test: divisible by {}", monkeys_commands[index*7 + 3])[0])
    reciptient_true = monkeys[int(parse.parse("    If true: throw to monkey {}", monkeys_commands[index*7 + 4])[0])]
    recipient_false = monkeys[int(parse.parse("    If false: throw to monkey {}", monkeys_commands[index*7 + 5])[0])]
    operation = parse.parse("  Operation: new = {} * {}", monkeys_commands[index*7 + 2])
    if operation is None:
        operation = parse.parse("  Operation: new = {} + {}", monkeys_commands[index*7 + 2])
        operator = int(operation[1])
        operation = add_to_worry
    else:
        operator = None if operation[1] == "old" else int(operation[1])
        operation = multiply_by
    monkey.construct_monkey(items, operation, operator, division_condition, reciptient_true, recipient_false)


def throw_items(number_of_rounds: int):
    for _ in range(number_of_rounds):
        for monkey in monkeys:
            monkey.process_items()


throw_items(20)
monkeys_inspections = [monkey.inspection_counter for monkey in monkeys]
monkeys_inspections.sort()
print(monkeys)
print(monkeys_inspections[-1] * monkeys_inspections[-2])
