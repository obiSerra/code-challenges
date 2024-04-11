from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def get_neighbors(grid, r, c):
    neighbors = []

    for i in range(max(r - 1, 0), min(len(grid), r + 2)):
        for j in range(max(0, c - 1), min(len(grid[0]), c + 2)):
            # print("!", i, j, grid[i][j])
            if i == r and j == c:
                continue
            try:
                neighbors.append(grid[i][j])
            except IndexError:
                pass
    return neighbors


def solution(input):
    grid = [list(line) for line in input]
    nums = [re.finditer(r"\d+", line) for line in input]
    placeholders = {}

    for i, l in enumerate(grid):
        out_line = l
        for m in nums[i]:
            k = f"{i}_{m.start()}_{m.end()}"
            placeholders[k] = m.group()
            out_line = out_line[: m.start()] + [k for n in out_line[m.start() : m.end()]] + out_line[m.end() :]
        grid[i] = out_line

    gears = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "*":
                nei = get_neighbors(grid, r, c)
                vals = list(set([n for n in nei if re.match(r"^\d", n)]))
                if len(vals) == 2:
                    gears.append(int(placeholders[vals[0]]) * int(placeholders[vals[1]]))

    return sum(gears)


if __name__ == "__main__":
    print(solution(input))
