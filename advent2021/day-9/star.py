from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[int(n) for n in list(line.rstrip())] for line in lines]


def adjacent(pos, grid):
    r, c = pos
    adj = [grid[a[0]][a[1]] for a in [[r-1, c], [r+1, c], [r, c-1],
                                      [r, c+1]] if a[0] > -1 and a[1] > -1
           and a[0] < len(grid)
           and a[1] < len(grid[r])]
    return adj


def solution(input):
    grid = input
    cnt = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            current = grid[r][c]
            adj = adjacent([r, c], grid)
            if current < min(adj):
                cnt += current + 1
    return cnt


if __name__ == '__main__':
    print(solution(input))
