from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def parse_line(line):
    g, l = line.split(":")
    id = int(g.replace("Game ", ""))
    sets = [x.split(",") for x in l.split(";")]
    ks = []
    for s in sets:
        k = {}
        for e in s:
            m = re.search(r"(\d+) (\w+)", e)
            k[m.group(2)] = int(m.group(1))
        ks.append(k)
    return [id, ks]


def solution(input):
    valid = []
    for line in input:
        id, sets = parse_line(line)
        is_valid = True
        for s in sets:
            if s.get("red", 0) > 12 or s.get("blue", 0) > 14 or s.get("green", 0) > 13:
                is_valid = False
                break
        if is_valid:
            valid.append(id)
    return sum(valid)


if __name__ == "__main__":
    print(solution(input))
