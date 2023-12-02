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
    ps = []
    for line in input:
        id, sets = parse_line(line)
        k = {}
        for s in sets:
            for e in s:
                k[e] = max(k.get(e, s[e]), s[e])
        ps.append(k.get("red", 0) * k.get("blue", 0) * k.get("green", 0))
    return sum(ps)


if __name__ == "__main__":
    print(solution(input))
