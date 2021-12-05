from os import path
from star import Bingo

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    extraction = input[0].split(',')
    bingos = []
    for line in input[1:]:
        if line == '':
            bingos.append(Bingo())
        else:
            bingos[-1].add_line(line)

    done = {}
    last_done = None
    for e in extraction:
        for i in range(0, len(bingos)):
            b = bingos[i]
            b.extract(e)
            res = b.done_bingo()
            if res is not None and i not in done:
                last_done = [res, int(e)]
                done[i] = True

    return last_done[0] * last_done[1]


if __name__ == '__main__':
    print(solution(input))
