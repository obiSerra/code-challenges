from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    turns = [[v.split("-") for v in i.split(",")] for i in input]
    tot = 0
    for t in turns:
        e1, e2 = t
        if int(e1[0]) <= int(e2[0]) and int(e1[1]) >= int(e2[1]):
            tot += 1
        elif int(e2[0]) <= int(e1[0]) and int(e2[1]) >= int(e1[1]):
            tot += 1
    return tot


if __name__ == "__main__":
    print(solution(input))
