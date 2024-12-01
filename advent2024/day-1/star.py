from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def parse_input(input):
    l1 = []
    l2 = []

    for i in input:
        ii = re.split(r'\s+', i)
        l1.append(int(ii[0]))
        l2.append(int(ii[1]))

    l1.sort()
    l2.sort()

    return l1, l2

def solution(input):
    l1, l2 = parse_input(input)
    vals = []
    for a,b in zip(l1, l2):
        vals.append(abs(a-b))

    return sum(vals)


if __name__ == '__main__':
    print(solution(input))
