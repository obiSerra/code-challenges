from os import path

from star import Point, Grid

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.rstrip() for line in lines]


class DGrid(Grid):
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
        else:
            while True:
                self.cells[start.y][start.x] += 1
                if start.x == end.x and start.y == end.y:
                    break
                if start.x > end.x:
                    start.x -= 1
                elif start.x < end.x:
                    start.x += 1
                if start.y > end.y:
                    start.y -= 1
                elif start.y < end.y:
                    start.y += 1

                


def parse_input(input):
    top = 0
    moves = []
    for inp in input:
        start, end = [Point(el) for el in inp.split(' -> ')]
        moves.append([start, end])
        top = max([start.y, end.x, start.x, end.x, top])

    grid = DGrid(top, top)
    for m in moves:

        start, end = m
        # print([start.x, start.y], [end.x, end.y])
        grid.move(start, end)

        # grid.print()
        # print()
        # print()
        # print()
    return grid.count_out()


def solution(input):
    return parse_input(input)


if __name__ == '__main__':
    print(solution(input))
