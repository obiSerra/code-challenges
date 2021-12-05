from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


class Bingo:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append([[ln, False] for ln in line.split(' ') if ln != ''])

    def extract(self, num):
        for i in range(0, len(self.lines)):
            ln = self.lines[i]
            for j in range(0, len(ln)):
                n = ln[j]
                if n[0] == num:
                    self.lines[i][j][1] = True

    def calc_points(self):
        cnt = 0
        for ln in self.lines:
            for v in ln:
                if v[1] is False:
                    cnt += int(v[0])

        return cnt

    def done_bingo(self):
        ok = True
        for c in range(0, len(self.lines[0])):
            ok = True
            for r in range(0, len(self.lines)):
                ok = ok and self.lines[r][c][1]
            if ok:
                return self.calc_points()

        for ln in self.lines:
            if all([v[1] for v in ln]):
                return self.calc_points()

        return None


def solution(input):
    extraction = input[0].split(',')
    bingos = []
    for line in input[1:]:
        if line == '':
            bingos.append(Bingo())
        else:
            bingos[-1].add_line(line)

    for e in extraction:
        done = None
        for b in bingos:
            b.extract(e)
            res = b.done_bingo()
            if res is not None:
                done = res

        if done is not None:
            return done * int(e)


if __name__ == '__main__':
    print(solution(input))
