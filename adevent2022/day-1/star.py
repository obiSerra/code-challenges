from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    elves = [0]
    for s in input:
        if s == "":
            elves.append(0)
            continue
        elves[-1] = elves[-1] + int(s)
    return max(elves)


if __name__ == "__main__":
    print(solution(input))
