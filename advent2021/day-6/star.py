from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [int(n) for n in lines[0].split(',')]


class Shoal:
    def __init__(self, fishes):
        self.calc_fishes(fishes)

    def calc_fishes(self, fishes):
        self.fishes = {}

        for f in fishes:
            if f not in self.fishes:
                self.fishes[f] = 0
            self.fishes[f] += 1

    def day_pass(self):
        next_day = {}
        for k in self.fishes.keys():
            nv = k - 1
            if nv < 0:
                nv = 6
                next_day[8] = self.fishes[k]
            if nv not in next_day:
                next_day[nv] = 0
            next_day[nv] += self.fishes[k]

        self.fishes = next_day


def solution(input, days):
    sh = Shoal(input)
    for i in range(0, days):
        sh.day_pass()

    cnt = 0

    for f in sh.fishes.values():
        cnt += f
    return cnt


if __name__ == '__main__':
    print(solution(input, 80))
