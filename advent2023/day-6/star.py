import functools
from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def calc_dist(time, p):
    return p * (time - p)


def solution(input):
    input = [[int(nn) for nn in n] for n in [re.findall(r"\d+", i) for i in input]]
    races = []
    for i in range(0, len(input[0])):
        races.append((input[0][i], input[1][i]))

    wins = []
    up = 0
    down = 0
    print(races)
    for time, distance in races:
        # print("Time", time, "Distance", distance)
        for i in range(1, time):
            traveled = calc_dist(time, i)
            if traveled > distance:
                down = i
                # print("Found DOWN", i)
                break
        for i in range(time, 1, -1):
            traveled = calc_dist(time, i)
            # print("Traveled", traveled, i)
            if traveled > distance:
                up = i
                # print("Found UP", i)
                break

        wins.append(up + 1 - down)
    return functools.reduce(lambda a, b: a * b, wins)


if __name__ == "__main__":
    print(solution(input))
