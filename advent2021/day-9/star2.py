from os import path
import functools

input = []


final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[int(n) for n in list(line.rstrip())] for line in lines]


def adjacent(pos, grid):
    r, c = pos
    adj = [a for a in [[r-1, c], [r+1, c], [r, c-1],
                       [r, c+1]] if a[0] > -1 and a[1] > -1
           and a[0] < len(grid)
           and a[1] < len(grid[r])]
    return adj


def find_lows(input):
    lows = []

    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            current = input[r][c]
            adj = adjacent([r, c], input)
            if current < min([input[a[0]][a[1]] for a in adj]):
                lows.append([r, c])
    return lows


def _hash(point):
    return ','.join([str(p) for p in point])


def find_basin(point, grid, lst=[], memo={}):
    if _hash(point) in memo:
        return memo[_hash(point)]
    r, c = point
    current = grid[r][c]
    adj = adjacent(point, grid)
    lows = [a for a in adj if grid[a[0]][a[1]]
            > current and grid[a[0]][a[1]] != 9]
    for ll in lows:
        lst.append(ll)
        find_basin(ll, grid, lst=lst, memo=memo)
    memo[_hash(point)] = lst
    return [a.split(',') for a in list(set([_hash(e) for e in lst]))]


def solution(input):

    lows = find_lows(input)
    basins = []
    for low in lows:
        bas = find_basin(low, input, lst=[], memo={})
        basins.append(len(bas) + 1)

    basins.sort()

    return functools.reduce(lambda a, b: a*b, basins[-3::])


if __name__ == '__main__':
    assert solution(input) == 1280496
    print(solution(input))
