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
    points = 0
    for win, own in input:
        ps = []
        p = 0
        for w in win:
            if w in own:
                ps.append(int(w))
                p = p + 1 if p == 0 else p * 2

        v = 0 if len(ps) == 0 else int(math.pow(2, len(ps) - 1))

        points += v

    return points


if __name__ == "__main__":
    print(solution(input))
