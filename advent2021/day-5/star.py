from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.rstrip() for line in lines]


class Point:
    def __init__(self, pt):
        x, y = [int(e) for e in pt.split(',')]
        self.x = x
        self.y = y


class Grid:
    def __init__(self, max_x, max_y):
        self.cells = []
        for c in range(0, max_x+1):
            row = []
            for r in range(0, max_y+1):
                row.append(0)
            self.cells.append(row)

    def print(self):
        for r in self.cells:
            print(r)

    def move(self, start, end):
        if start.x == end.x:
            s = min(start.y, end.y)
            e = max(start.y, end.y)
            while s <= e:
                self.cells[s][start.x] += 1
                s += 1
        elif start.y == end.y:
            s = min(start.x, end.x)
            e = max(start.x, end.x)
            while s <= e:
                self.cells[start.y][s] += 1
                s += 1

    def count_out(self):
        cnt = 0
        for r in self.cells:
            for c in r:
                if c > 1:
                    cnt += 1
        return cnt


def parse_input(input):
    top = 0
    moves = []
    for inp in input:
        start, end = [Point(el) for el in inp.split(' -> ')]
        moves.append([start, end])
        top = max([start.y, end.x, start.x, end.x, top])

    grid = Grid(top, top)
    for m in moves:

        start, end = m
        grid.move(start, end)

    return grid.count_out()


def solution(input):
    return parse_input(input)


if __name__ == '__main__':
    print(solution(input))
