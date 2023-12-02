from os import path

BALLS = {'blue': 14,
         'red': 12,
         'green': 13}
BALLS_L = {'b': 14,
           'r': 12,
           'g': 13}

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
games = [chart_line.replace('\n', '') for chart_line in file.readlines()]

# Part 1
game_id_index = 5
total = 0
for game in games:
    counter = 0
    if game[game_id_index + 1].isdigit():
        if game[game_id_index + 2].isdigit():
            game_id = int(f'{game[game_id_index]}{game[game_id_index + 1]}{game[game_id_index + 2]}')
            counter = 8
        else:
            game_id = int(f'{game[game_id_index]}{game[game_id_index + 1]}')
            counter = 7
    else:
        game_id = int(game[game_id_index])
        counter = 6
    total += game_id
    while counter < len(game):
        char = game[counter]
        if char in [' ', ',', ';']:
            counter += 1
            continue
        if char.isdigit():
            next_char = game[counter + 1]
            if next_char.isdigit():
                color_index = 1
                number = int(char + next_char)
            else:
                color_index = 0
                number = int(char)
            color_char = game[counter + color_index + 2]

            if number > BALLS_L[color_char]:
                total -= game_id
                break
            else:
                counter += 1 + color_index
        else:
            counter += 1
print(total)

# Part 2
game_id_index = 5
total = 0
for game in games:
    counter = 0
    if game[game_id_index + 1].isdigit():
        if game[game_id_index + 2].isdigit():
            counter = 8
        else:
            counter = 7
    else:
        counter = 6

    game_balls = {'b': 0,
                  'r': 0,
                  'g': 0}
    while counter < len(game):
        char = game[counter]
        if char in [' ', ',', ';']:
            counter += 1
            continue
        if char.isdigit():
            next_char = game[counter + 1]
            if next_char.isdigit():
                color_index = 1
                number = int(char + next_char)
            else:
                color_index = 0
                number = int(char)
            color_char = game[counter + color_index + 2]

            if number > game_balls[color_char]:
                game_balls[color_char] = number
            else:
                counter += 1 + color_index
        else:
            counter += 1
    total += game_balls['r'] * game_balls['g'] * game_balls['b']
print(total)
