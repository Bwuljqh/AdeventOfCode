from os import path

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
scratch_cards = [scratch_card.replace('\n', '') for scratch_card in file.readlines()]

# part 1

total = 0

for scratch_card in scratch_cards:
    core_card = scratch_card.split(':')[-1]
    winning_numbers, numbers = core_card.split('|')
    score = 0.5
    for number in numbers.split():
        if number in winning_numbers.split():
            score *= 2
    total += int(score)
print(total)

# part 2

cards = {number: 0 for number in range(1, 219)}

for scratch_card in scratch_cards:
    game, core_card = scratch_card.split(':')
    game_id = int(game.split()[-1])
    cards[game_id] += 1
    winning_numbers, numbers = core_card.split('|')
    wins = 0
    for number in numbers.split():
        if number in winning_numbers.split():
            cards[game_id + wins + 1] += 1 * cards[game_id]
            wins += 1

print(sum(cards.values()))
