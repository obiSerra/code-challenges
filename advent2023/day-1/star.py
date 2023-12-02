from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    digs = [list(re.sub(r"[a-z]*", "", v)) for v in input]
    digs = [int(l[0] + l[-1]) for l in digs]
    return sum(digs)


if __name__ == "__main__":
    print(solution(input))
