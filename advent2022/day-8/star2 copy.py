from os import path
import pprint

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input_test.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):

    input = [list(s) for s in input]
    vis = {}

    for i in range(1, len(input) - 1):
        for j in range(1, len(input[i]) - 1):
            vis[(i, j)] = {"v": input[i][j]}

            if input[i][j] > input[i][j - 1]:
                try:
                    h = vis[(i, j - 1)]["l"]
                except KeyError:
                    h = 0
            else:
                h = 0
            vis[(i, j)]["l"] = h + 1

    for i in range(1, len(input) - 1):
        for j in range(len(input[i]) - 2, 0, -1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}

            if input[i][j] > input[i][j + 1]:
                try:
                    h = vis[(i, j + 1)]["r"]
                except KeyError:
                    h = 0
            else:
                h = 0
            vis[(i, j)]["r"] = h + 1

    for j in range(1, len(input) - 1):
        for i in range(1, len(input[j]) - 1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}

            if input[i][j] > input[i - 1][j]:
                try:
                    h = vis[(i - 1, j)]["t"]
                except KeyError:
                    h = 0
            else:
                h = 0
            vis[(i, j)]["t"] = h + 1

    for j in range(len(input) - 2, 0, -1):
        for i in range(len(input[j]) - 2, 0, -1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}

            if input[i][j] > input[i + 1][j]:
                try:
                    h = vis[(i + 1, j)]["b"]
                except KeyError:
                    h = 0
            else:
                h = 0
            vis[(i, j)]["b"] = h + 1

    m = 0

    for k in vis:
        v = vis[k]
        t = v["l"] * v["r"] * v["t"] * v["b"]
        m = max(t, m)
    
    return vis


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(solution(input))
