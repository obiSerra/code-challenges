import functools
from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]
    input = [line.split(" ") for line in input]


def get_rank(hand):
    k = {}
    vs = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    for card in hand:
        k[card] = k.get(card, 0) + 1

        n = 0
        if card.isnumeric():
            n = int(card) - 2
        else:
            n = {"T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}[card]
        vs += alphabet[n]

    rank = "0"
    p = list(k.values())
    if 5 in p:
        rank = "6"
    elif 4 in p:
        rank = "5"
    elif 3 in p and 2 in p:
        rank = "4"
    elif 3 in p:
        rank = "3"
    elif p.count(2) == 2:
        rank = "2"
    elif 2 in p:
        rank = "1"

    return rank + vs


def solution(input):
    valued_hands = [(get_rank(hand), hand, int(bid)) for hand, bid in input]
    valued_hands.sort(key=lambda x: x[0])
    points = 0
    for i, (hand, orig, bid) in enumerate(valued_hands):
        # print(hand, orig, i + 1)
        points += bid * (i + 1)
    return points


if __name__ == "__main__":
    print(solution(input))
