from os import path

NUMBERS = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'inputDay1.txt'), 'r')

charts = [sack.replace('\n', '') for sack in file.readlines()]

charts_number = ["".join(digit if digit.isdigit() else "" for digit in line) for line in charts]

print(sum(int(f'{line[0]}{line[-1]}') for line in charts_number))


# second star


new_charts = []
for line in charts:
    new_line = ''
    while len(line) > 0:
        if line[0].isdigit():
            new_line += line[0]
        else:
            for number, digit in NUMBERS.items():
                if line.startswith(number):
                    new_line += str(digit)
        line = line[1:]
    new_charts.append(new_line)
charts_numbers_with_words = ["".join(digit if digit.isdigit() else "" for digit in line) for line in new_charts]


print(sum(int(f'{line[0]}{line[-1]}') for line in charts_numbers_with_words))
