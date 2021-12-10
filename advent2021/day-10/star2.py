from os import path
import math
input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [list(line.strip()) for line in lines]

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
points = [1, 2, 3, 4]


def chunk(to_parse, opened):
    if not to_parse:
        return opened

    nxt = to_parse[0]
    if nxt in openers:
        opened.append(nxt)
        return chunk(to_parse[1:], opened)
    elif nxt in closers:
        if openers.index(opened[-1]) == closers.index(nxt):
            return chunk(to_parse[1:], opened[:-1])
        else:
            return []


def solution(input):

    all_scores = []
    for line in input:
        score = 0
        rems = chunk(line, [])
        if rems:
            rems.reverse()
            for r in rems:
                score = score * 5 + points[openers.index(r)]
            all_scores.append(score)

    all_scores.sort()

    return all_scores[math.floor(len(all_scores)/2)]


if __name__ == '__main__':
    print(solution(input))
