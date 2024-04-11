import math
from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]
    input = [[re.findall(r"\d+", l) for l in re.sub(r"^Card.*:", "", line).strip().split("|")] for line in input]


def solution(input):
    cards = [1 for i in range(len(input))]
    for i, (win, own) in enumerate(input):
        ps = []
        for w in win:
            if w in own:
                ps.append(int(w))

        cnt = cards[i]
        for j in range(1, len(ps) + 1):
            cards[i + j] += cnt

    return sum(cards)


if __name__ == "__main__":
    print(solution(input))
