import os
from collections import Counter
from enum import Enum

ROOTDIR = os.path.dirname(__file__)
file = open(os.path.join(ROOTDIR, 'inputDay2.txt'), 'r')

games = [game.replace('\n', '') for game in file.readlines()]

SYMBOLS = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}


class points(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class results(Enum):
    win = 6
    loss = 0
    draw = 3


PLAYS = {
    'RockRock': 'draw',
    'RockPaper': 'win',
    'RockScissors': 'loss',
    'PaperRock': 'loss',
    'PaperPaper': 'draw',
    'PaperScissors': 'win',
    'ScissorsRock': 'win',
    'ScissorsPaper': 'loss',
    'ScissorsScissors': 'draw'
}

COMBINATIONS_POINTS_FIRST_PART = {
    'A X': results[PLAYS[''.join((SYMBOLS['A'], SYMBOLS['X']))]].value + points[SYMBOLS['X']].value,
    'A Y': results[PLAYS[''.join((SYMBOLS['A'], SYMBOLS['Y']))]].value + points[SYMBOLS['Y']].value,
    'A Z': results[PLAYS[''.join((SYMBOLS['A'], SYMBOLS['Z']))]].value + points[SYMBOLS['Z']].value,
    'B X': results[PLAYS[''.join((SYMBOLS['B'], SYMBOLS['X']))]].value + points[SYMBOLS['X']].value,
    'B Y': results[PLAYS[''.join((SYMBOLS['B'], SYMBOLS['Y']))]].value + points[SYMBOLS['Y']].value,
    'B Z': results[PLAYS[''.join((SYMBOLS['B'], SYMBOLS['Z']))]].value + points[SYMBOLS['Z']].value,
    'C X': results[PLAYS[''.join((SYMBOLS['C'], SYMBOLS['X']))]].value + points[SYMBOLS['X']].value,
    'C Y': results[PLAYS[''.join((SYMBOLS['C'], SYMBOLS['Y']))]].value + points[SYMBOLS['Y']].value,
    'C Z': results[PLAYS[''.join((SYMBOLS['C'], SYMBOLS['Z']))]].value + points[SYMBOLS['Z']].value
}

COMBINATIONS_POINTS_SECOND_PART = {
    'A X': results.loss.value + points.Scissors.value,
    'A Y': results.draw.value + points.Rock.value,
    'A Z': results.win.value + points.Paper.value,
    'B X': results.loss.value + points.Rock.value,
    'B Y': results.draw.value + points.Paper.value,
    'B Z': results.win.value + points.Scissors.value,
    'C X': results.loss.value + points.Paper.value,
    'C Y': results.draw.value + points.Scissors.value,
    'C Z': results.win.value + points.Rock.value
}

print(sum((COMBINATIONS_POINTS_SECOND_PART[game]*count for game, count in dict(Counter(games)).items())))
