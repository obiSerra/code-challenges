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
        l2.append(ii[1])

    l1.sort()

    return l1, l2

def solution(input):
    l1, l2 = parse_input(input)
   
    app = {}

    for l in l2:
        if l in app:
            app[l] += 1
        else:
            app[l] = 1

    s = 0
    for l in l1:
        s += l * app.get(str(l), 0)

    return s


if __name__ == '__main__':
    print(solution(input))
