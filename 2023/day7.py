import numpy as np
from dataclasses import dataclass
from typing import ClassVar
from collections import Counter


@dataclass
class Hand:
    cards: str
    bid: int
    order_cards: ClassVar[np.ndarray[str]] = np.array(
        ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    )

    def __lt__(self, other):
        if self.hand_type() < other.hand_type():
            return True
        elif self.hand_type() == other.hand_type():
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                elif (
                    np.argwhere(self.order_cards == self.cards[i])[0, 0]
                    > np.argwhere(self.order_cards == other.cards[i])[0, 0]
                ):
                    return True
                else:
                    return False
            return False
        else:
            return False

    def hand_type(self):
        ctr = list(Counter(self.cards).values())
        if 5 in ctr:
            return 6
        elif 4 in ctr:
            return 5
        elif (3 in ctr) and (2 in ctr):
            return 4
        elif 3 in ctr:
            return 3
        elif ctr.count(2) == 2:
            return 2
        elif 2 in ctr:
            return 1
        else:
            return 0


@dataclass
class HandJoker(Hand):
    order_cards: ClassVar[np.ndarray[str]] = np.array(
        ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    )

    def hand_type(self):
        possibilites = []
        for chr in self.order_cards[:-1]:
            new_cards = self.cards.replace("J", chr)
            new_hand = Hand(new_cards, self.bid)
            possibilites.append(new_hand.hand_type())
        return np.max(possibilites)


def solve(data, part_two):
    hands = []
    for line in data:
        line = line.split()
        cards = line[0]
        bid = int(line[1])
        hand = HandJoker(cards, bid) if part_two else Hand(cards, bid)
        hands.append(hand)
    sorted = np.sort(hands)
    total = sum(sorted[k].bid * (k + 1) for k in range(len(sorted)))
    return total


def part1():
    with open("inputs/day7inp.txt", "r") as file:
        data = file.read().splitlines()
    return solve(data, False)


def part2():
    with open("inputs/day7inp.txt", "r") as file:
        data = file.read().splitlines()
    return solve(data, True)


if __name__ == "__main__":
    print(part1())
    print(part2())
