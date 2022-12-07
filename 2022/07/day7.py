from __future__ import annotations

from os import path
from typing import List, Optional

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay7.txt'), 'r')

signal: List[str] = [instruction.replace('\n', '') for instruction in file.readlines()]

TOTAL_SPACE = 70000000
GOAL_FREE_SPACE = 30000000


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, father: Optional[Directory] = None, files: Optional[List[File]] = None, directories: Optional[List[Directory]] = None) -> None:
        if files is None:
            files = []
        if directories is None:
            directories = []
        self.name = name
        self.files: List[File] = files
        self.directories: List[Directory] = directories
        self.father: Directory = father

    def add_file(self, file: File) -> None:
        self.files.append(file)

    def add_directory(self, directory: Directory) -> None:
        self.directories.append(directory)

    def get_total_weight(self) -> int:
        return sum(file.size for file in self.files) + sum(directory.get_total_weight() for directory in self.directories)

    def __str__(self) -> str:
        return f"{self.name}"


directories: List[Directory] = []

current_dir: Directory = Directory('', None)
for command in signal:
    split_command = command.split(' ')
    if split_command[0] == '$':
        if split_command[1] != 'cd':
            continue
        folder = split_command[2]
        if folder == '..':
            current_dir = current_dir.father
        else:
            new_directory = Directory(folder, current_dir)
            directories.append(new_directory)
            current_dir.add_directory(new_directory)
            current_dir = new_directory
    else:
        file_name = split_command[1]
        size = split_command[0]
        if size == 'dir':
            continue
        new_file = File(file_name, int(size))
        current_dir.add_file(new_file)

print(sum(directory.get_total_weight() for directory in directories if directory.get_total_weight() < 100000))


used_space = directories[0].get_total_weight()
free_space = TOTAL_SPACE - used_space
needed_space = GOAL_FREE_SPACE - free_space

print(min(directory.get_total_weight() for directory in directories if directory.get_total_weight() > needed_space))
