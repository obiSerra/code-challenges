from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [list(line.strip()) for line in lines]

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
points = [3, 57, 1197, 25137]


def chunk(to_parse, opened):
    if not to_parse:
        return 0

    nxt = to_parse[0]
    if nxt in openers:
        opened.append(nxt)
        return chunk(to_parse[1:], opened)
    elif nxt in closers:
        if openers.index(opened[-1]) == closers.index(nxt):
            return chunk(to_parse[1:], opened[:-1])
        else:
            return points[closers.index(nxt)]


def solution(input):

    points = 0
    for line in input:
        points += chunk(line, [])

    return points


if __name__ == '__main__':
    print(solution(input))
