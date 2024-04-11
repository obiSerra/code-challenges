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
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    for card in hand:
        k[card] = k.get(card, 0) + 1

        n = 0
        if card.isnumeric():
            n = int(card) - 1
        elif card == "J":
            n = 8
        else:
            n = {"T": 8, "J": 0, "Q": 10, "K": 11, "A": 12}[card]
        vs += alphabet[n]

    rank = "0"
    vals = [v for v in list(k.items()) if v[0] != "J"]
    # print("pREV", vals)
    if "J" in k.keys():
        if list(k.keys()).count("J") == 5:
            vals = [["A", 5]]
        for i in range(k["J"]):
            vals.sort(key=lambda x: x[1], reverse=True)
            try:
                vals = [[vals[0][0], vals[0][1] + 1]] + vals[1:]
            except IndexError:
                vals = [["A", 1]]
                # print("ERR", k)

    k = dict(vals)
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
