from __future__ import annotations

from enum import Enum, auto
from os import path
from typing import List, Optional

from numpy import prod

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay8.txt'), 'r')

trees: List[str] = [tree.replace('\n', '') for tree in file.readlines()]


class Direction(Enum):
    north = auto()
    south = auto()
    east = auto()
    west = auto()


class State(Enum):
    unchecked = auto()
    visible = auto()
    blocked = auto()


class Tree:
    def __init__(self, height: int) -> None:
        self.height: int = height

        self.neighbours: dict[str, Optional[Tree]] = {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        }

        self.visibility: dict[str, Optional[State]] = {
            'north': State.unchecked,
            'south': State.unchecked,
            'east': State.unchecked,
            'west': State.unchecked
        }

    def add_neighbour(self, direction: Direction, tree: Tree):
        if isinstance(tree, Tree) and isinstance(direction, Direction):
            self.neighbours[direction.name] = tree

    def __repr__(self) -> str:
        return f'A tree of height {self.height}'

    def is_visible(self) -> bool:
        return any(direction == State.visible for direction in self.visibility.values())

    def get_view(self):
        score = 1
        for direction, neighbour in self.neighbours.items():
            direction = Direction[direction]
            if neighbour is None:
                continue
            tree: Tree = neighbour
            number_of_trees = 0
            while True:
                if tree.height >= self.height:
                    score *= number_of_trees + 1
                    break
                number_of_trees += 1
                tree = tree.neighbours[direction.name]
                if tree is None:
                    score *= number_of_trees
                    break

        return score


class Forest:
    def __init__(self, trees: List[str]) -> None:
        self.construct_forest(trees)

    def construct_forest(self, trees: List[str]) -> None:
        self.height = len(trees[0])
        self.width = len(trees)
        self.trees: List[List[Tree]] = [[Tree(int(trees[h][w]))for w in range(self.width)] for h in range(self.height)]
        for h in range(self.height):
            for w in range(self.width):
                self.update_neighbours(h, w)
        # ((self.update_neighbours(h, w) for w in range(self.width)) for h in range(self.height))

    def update_neighbours(self, height: int, width: int):
        tree = self.trees[height][width]
        for h_offset, w_offset, direction in [(1, 0, Direction.south), (-1, 0, Direction.north), (0, 1, Direction.east), (0, -1, Direction.west)]:
            try:
                if height + h_offset >= 0 and width + w_offset >= 0:
                    tree.add_neighbour(direction, self.trees[height + h_offset][width + w_offset])
            except IndexError:
                continue

    def find_best_view(self):
        return max(self.trees[h][w].get_view() for w in range(1, self.width - 1) for h in range(1, self.height - 1))

    def check_from_north(self):
        for w in range(self.width):
            max_height_tree: int = -1
            for h in range(self.height):
                tree = self.trees[h][w]
                if tree.height <= max_height_tree:
                    tree.visibility["north"] = State.blocked
                else:
                    tree.visibility["north"] = State.visible
                    max_height_tree = tree.height

    def check_from_south(self):
        for w in range(self.width):
            max_height_tree = -1
            for h in range(1, self.height + 1):

                tree = self.trees[-h][w]
                if tree.height <= max_height_tree:
                    tree.visibility["south"] = State.blocked
                else:
                    tree.visibility["south"] = State.visible
                    max_height_tree = tree.height

    def check_from_west(self):
        for h in range(self.height):
            max_height_tree = -1
            for w in range(self.width):
                tree = self.trees[h][w]
                if tree.height <= max_height_tree:
                    tree.visibility["west"] = State.blocked
                else:
                    tree.visibility["west"] = State.visible
                    max_height_tree = tree.height

    def check_from_east(self):
        for h in range(self.height):
            max_height_tree = -1
            for w in range(1, self.width + 1):

                tree = self.trees[h][-w]
                if tree.height <= max_height_tree:
                    tree.visibility["east"] = State.blocked
                else:
                    tree.visibility["east"] = State.visible
                    max_height_tree = tree.height

    def check_visible_trees(self) -> None:
        forest.check_from_north()
        forest.check_from_south()
        forest.check_from_east()
        forest.check_from_west()

    def count_visible_trees(self) -> int:
        count = 0
        for tree_line in self.trees:
            for tree in tree_line:
                if tree.is_visible():
                    count += 1
        return count


forest = Forest(trees)
forest.check_visible_trees()
print(forest.trees[4][3].get_view())
print(forest.find_best_view())