from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    n_w = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words = "|".join(n_w)
    words += "|" + "|".join([str(v) for v in range(1, 10)])
    vals = []
    for line in input:
        m = re.findall(r"(?=(" + words + "))", line)
        # print(line, m)
        vs = ""
        if m[0] in n_w:
            vs += str(n_w.index(m[0]) + 1)
        else:
            vs += m[0]
        if m[-1] in n_w:
            vs += str(n_w.index(m[-1]) + 1)
        else:
            vs += m[-1]
        vals.append(int(vs))
    return sum(vals)


if __name__ == "__main__":
    print(solution(input))
