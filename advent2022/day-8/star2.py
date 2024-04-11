from os import path
import pprint

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):

    input = [list(s) for s in input]
    vis = {}

    for i in range(1, len(input) - 1):
        for j in range(1, len(input[i]) - 1):
            vis[(i, j)] = {"v": input[i][j]}
            h = 0
            jj = j-1
            while jj > 1 and input[i][j] > input[i][jj]:
                jj -= 1
                h += 1

            vis[(i, j)]["l"] = h + 1

    for i in range(1, len(input) - 1):
        for j in range(len(input[i]) - 2, 0, -1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}
            h = 0

            jj = j+1
            try:
                while input[i][j] > input[jj][j]:
                    jj += 1
                    h += 1
            except IndexError:
                pass
            vis[(i, j)]["r"] = h + 1

    for j in range(1, len(input) - 1):
        for i in range(1, len(input[j]) - 1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}
            h = 0

            ii = i-1
            while ii > 1 and input[i][j] > input[ii][j]:
                ii -= 1
                h += 1

            vis[(i, j)]["t"] = h + 1

    for j in range(len(input) - 2, 0, -1):
        for i in range(len(input[j]) - 2, 0, -1):
            if (i, j) not in vis:
                vis[(i, j)] = {"v": input[i][j]}
            h = 0
            ii = i+1
            try:
                while input[i][j] > input[ii][j]:
                    ii += 1
                    h += 1
            except IndexError:
                pass

            vis[(i, j)]["b"] = h + 1

    m = 0

    for k in vis:
        v = vis[k]
        t = v["l"] * v["r"] * v["t"] * v["b"]
        if t > m:
            print(k, v)
        m = max(t, m)

    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(vis)

    return m


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(solution(input))



#1607424