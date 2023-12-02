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
file = open(path.join(ROOTDIR, 'inputDay1Alienor.txt'), 'r')
charts = [chart_line.replace('\n', '') for chart_line in file.readlines()]

charts_digits_only = ["".join(char if char.isdigit() else "" for char in line) for line in charts]

print(sum(int(f'{line[0]}{line[-1]}') for line in charts_digits_only))


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
charts_digits_only = ["".join(digit if digit.isdigit() else "" for digit in line) for line in new_charts]
print(sum(int(f'{line[0]}{line[-1]}') for line in charts_digits_only))

# Other solution

NUMBERS = {'one': 'one1one',
           'two': 'two2two',
           'three': 'three3three',
           'four': 'four4four',
           'five': 'five5five',
           'six': 'six6six',
           'seven': 'seven7seven',
           'eight': 'eight8eight',
           'nine': 'nine9nine'}

new_charts = []
for line in charts:
    new_line = line
    for number, digit in NUMBERS.items():
        new_line = new_line.replace(number, digit)
    new_charts.append(new_line)
charts_digits_only = ["".join(digit if digit.isdigit() else "" for digit in line) for line in new_charts]

print(sum(int(f'{line[0]}{line[-1]}') for line in charts_digits_only))

# Other solution

NUMBERS = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

sum_total = 0
for line in charts:
    current_line_front = line
    current_line_back = line
    first_digit = None
    last_digit = None
    while True:
        if first_digit is None and current_line_front[0].isdigit():
            first_digit = current_line_front[0]
        elif first_digit is None:
            for number, digit in NUMBERS.items():
                if current_line_front.startswith(number):
                    first_digit = str(digit)
        if last_digit is None and current_line_back[-1].isdigit():
            last_digit = current_line_back[-1]
        elif last_digit is None:
            for number, digit in NUMBERS.items():
                if current_line_back.endswith(number):
                    last_digit = str(digit)
        if first_digit is not None and last_digit is not None:
            sum_total += int(f'{first_digit}{last_digit}')
            break
        else:
            current_line_front = current_line_front[1:]
            current_line_back = current_line_back[:-1]
print(sum_total)
