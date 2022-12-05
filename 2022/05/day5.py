from os import path
import pprint
from typing import List, Tuple

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay5.txt'), 'r')

instructions: List[str] = [instruction.replace('\n', '') for instruction in file.readlines()]


class Pallet:
    def __init__(self, crates: str) -> None:
        self.crates = crates

    def add_one_crate(self, crate) -> None:
        self.crates += crate

    def remove_one_crate(self) -> str:
        self.crates, result = self.crates[:-1], self.crates[-1]
        return result

    def add_stack_of_crates(self, crates) -> None:
        self.crates += crates

    def remove_stack_of_crates(self, number_of_crates) -> str:
        self.crates, result = self.crates[:-number_of_crates], self.crates[-number_of_crates:]
        return result

    def get_height_of_pallet(self) -> int:
        return len(self.crates)

    def is_empty(self) -> bool:
        return not(len(self.crates))


def parse_instruction(instruction: str) -> Tuple[int, int, int]:
    split_instruction = instruction.split(' ')
    number = int(split_instruction[1])
    index_giving_pallet = int(split_instruction[3])
    index_receiving_pallet = int(split_instruction[5])
    return number, index_giving_pallet, index_receiving_pallet


class Crane:
    def __init__(self, pallets: List[Pallet]) -> None:
        self.pallets = ['dummy'] + pallets

    def execute_instruction_9000(self, instruction: str):
        number_of_crates, index_giving_pallet, index_receiving_pallet = parse_instruction(instruction)
        for _ in range(number_of_crates):
            if self.pallets[index_giving_pallet].is_empty():
                return
            else:
                self.pallets[index_receiving_pallet].add_one_crate(self.pallets[index_giving_pallet].remove_one_crate())

    def execute_instructions_9000(self, instructions: List[str]) -> None:
        for instruction in instructions:
            self.execute_instruction_9000(instruction)

    def execute_instruction_9001(self, instruction: str):
        number_of_crates, index_giving_pallet, index_receiving_pallet = parse_instruction(instruction)
        if self.pallets[index_giving_pallet].get_height_of_pallet() < number_of_crates:
            number_of_crates = self.pallets[index_giving_pallet].get_height_of_pallet()
        removed_crates = self.pallets[index_giving_pallet].remove_stack_of_crates(number_of_crates)
        self.pallets[index_receiving_pallet].add_stack_of_crates(removed_crates)

    def execute_instructions_9001(self, instructions: List[str]) -> None:
        for instruction in instructions:
            self.execute_instruction_9001(instruction)

    def __str__(self) -> str:
        return str([pallets.crates for pallets in self.pallets[1:]])


pallet1 = Pallet('GTRW')
pallet2 = Pallet('GCHPMSVW')
pallet3 = Pallet('CLTSGM')
pallet4 = Pallet('JHDMWRF')
pallet5 = Pallet('PQLHSWFJ')
pallet6 = Pallet('PJDNFMS')
pallet7 = Pallet('ZBDFGCSJ')
pallet8 = Pallet('RTB')
pallet9 = Pallet('HNWLC')

crane = Crane([pallet1, pallet2, pallet3, pallet4, pallet5, pallet6, pallet7, pallet8, pallet9])

# pallet1 = Pallet('ZN')
# pallet2 = Pallet('MCD')
# pallet3 = Pallet('P')

# crane = Crane([pallet1, pallet2, pallet3])
crane.execute_instructions_9001(instructions)
pprint.pprint([pallets.crates for pallets in crane.pallets[1:]])
pprint.pprint(''.join((pallets.crates[-1] for pallets in crane.pallets[1:])))
