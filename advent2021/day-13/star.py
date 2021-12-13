from os import path
import re


input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def print_grid(grid):
    for g in grid:
        print(g)


def solution(input):
    points = [[int(n) for n in p.split(',')]
              for p in input if p and not p.startswith('fold')]
    folds = [p for p in input if p.startswith('fold')]

    xs = [pt[0] for pt in points]
    ys = [pt[1] for pt in points]

    grid = []
    for y in range(0, max(ys)+1):
        row = []
        for x in range(0, max(xs)+1):
            row.append('.')
        grid.append(row)

    for p in points:
        x, y = p

        grid[y][x] = "#"

    for f in [folds[0]]:
        m = re.search('y=([0-9]+)', f)
        if m is not None:
            fold_line = int(m.group(1))
            for y in range(fold_line, len(grid)):
                for x in range(0, len(grid[0])):
                    new_line = abs((y - fold_line) - fold_line)
                    if grid[new_line][x] == '.':
                        grid[new_line][x] = grid[y][x]
                grid[y] = None

            grid = [g for g in grid if g is not None]

        m = re.search('x=([0-9]+)', f)

        if m is not None:
            fold_line = int(m.group(1))
            for y in range(0, len(grid)):
                for x in range(fold_line, len(grid[0])):
                    new_row = abs((x - fold_line) - fold_line)
                    if grid[y][new_row] == '.':
                        grid[y][new_row] = grid[y][x]
                    grid[y][x] = None

            grid = [[g for g in gr if g is not None] for gr in grid]

    cnt = 0

    for row in grid:
        for p in row:
            if p == '#':
                cnt += 1

    return cnt


if __name__ == '__main__':
    print(solution(input))
