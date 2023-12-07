
from os import path

from collections import Counter

CATEGORIES = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARDS_SECOND_PART = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

ROOTDIR = path.dirname(__file__)
file = open(path.join(ROOTDIR, 'input.txt'), 'r')
hands = [hand.replace('\n', '') for hand in file.readlines()]


def identify_hand_category(hand: str, joker=False) -> str:

    counter = Counter(hand).most_common()
    most_common_item = counter[0][1]

    if joker and 'J' in hand:
        if new_hand := "".join(hand.split('J')):
            most_common_item = Counter(new_hand).most_common()[0][1] + len(hand) - len(new_hand)
        else:
            most_common_item = 5

    match most_common_item:
        case 5:
            return CATEGORIES[0]
        case 4:
            return CATEGORIES[1]
        case 3:
            return (
                CATEGORIES[2]
                if counter[1][1] == 2
                else CATEGORIES[3]
            )
        case 2:
            return (
                CATEGORIES[4]
                if counter[1][1] == 2
                else CATEGORIES[5]
            )
        case _:
            return CATEGORIES[6]


class Hand():

    def __init__(self, hand, bid, joker=False, cards_values=CARDS) -> None:
        self.hand = hand
        self.bid = bid
        self.category = identify_hand_category(self.hand, joker)
        self.cards = cards_values

    def __lt__(self, other):
        if self.category != other.category:
            return CATEGORIES.index(self.category) > CATEGORIES.index(other.category)
        index = 0
        while index < len(self.hand):
            if self.hand[index] != other.hand[index]:
                return self.cards.index(self.hand[index]) > self.cards.index(other.hand[index])
            else:
                index += 1

    def __repr__(self) -> str:
        return str((self.hand, self.bid))


unsorted_hands = []

for hand in hands:
    cards, bid = hand.split(' ')
    unsorted_hands.append(Hand(cards, int(bid), joker=False, cards_values=CARDS))
unsorted_hands = sorted(unsorted_hands, reverse=False)

print(sum((i + 1) * unsorted_hands[i].bid for i in range(len(unsorted_hands))))

unsorted_hands = []

for hand in hands:
    cards, bid = hand.split(' ')
    unsorted_hands.append(Hand(cards, int(bid), joker=True, cards_values=CARDS_SECOND_PART))
unsorted_hands = sorted(unsorted_hands, reverse=False)

print(sum((i + 1) * unsorted_hands[i].bid for i in range(len(unsorted_hands))))
