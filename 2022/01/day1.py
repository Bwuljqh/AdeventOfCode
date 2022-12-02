from os import path
import matplotlib.pyplot as plt

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay1.txt'), 'r')

elf_troup = ''.join(file.readlines())
numbered_calories = [[int(elf_calorie) for elf_calorie in elf.split('\n')] for elf in elf_troup.split('\n\n')]
summed_calories = [sum(elf) for elf in numbered_calories]

summed_calories.sort()
print(sum(summed_calories[-3:]))

plt.figure(dpi=300)
plt.bar(range(len(summed_calories)), summed_calories)
plt.show()
