from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[int(n) for n in list(line.strip())] for line in lines]


def adjacent(pos, grid):
    r, c = pos
    adj = [a for a in [[r-1, c], [r+1, c], [r, c-1],
                       [r, c+1], [r-1, c-1], [r+1, c+1], [r+1, c-1],
                       [r-1, c+1]] if a[0] > -1 and a[1] > -1
           and a[0] < len(grid)
           and a[1] < len(grid[r])]
    return adj


def solve_flash(input):
    flashes = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] > 9:
                flashes += 1
                input[r][c] = 0
                for a in adjacent([r, c], input):
                    if input[a[0]][a[1]] != 0:
                        input[a[0]][a[1]] += 1
    return flashes, input


def run_step(input):
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            input[r][c] += 1

    fl, input = solve_flash(input)
    while fl > 0:
        fl, input = solve_flash(input)

    return input


def solution(input):
    i = 0
    while True:
        i += 1
        input = run_step(input)
        all_flashes = True
        for r in range(0, len(input)):
            for c in range(0, len(input[r])):
                if input[r][c] != 0:
                    all_flashes = False
        if all_flashes is True:
            break

    return i


if __name__ == '__main__':
    print(solution(input))
