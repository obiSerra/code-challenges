from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[w.strip().split(' ') for w in line.strip().split('|')] for
             line in lines]


def solve_line(patterns, output):
    patterns.sort(key=lambda x: len(x))
    patterns = [set(p) for p in patterns]
    numbers = {
        0: None,
        1: [p for p in patterns if len(p) == 2][0],
        2: None,
        3: None,
        4: [p for p in patterns if len(p) == 4][0],
        5: None,
        6: None,
        7: [p for p in patterns if len(p) == 3][0],
        8: [p for p in patterns if len(p) == 7][0],
        9: None,
    }

    numbers[6] = [e for e in [p for p in patterns if len(
        p) == 6] if len(numbers[1].difference(e)) != 0][0]

    patterns = [p for p in patterns if p != numbers[6]]

    numbers[9] = [e for e in [p for p in patterns if len(
        p) == 6] if len(numbers[4].difference(e)) == 0][0]

    patterns = [p for p in patterns if p != numbers[9]]
    numbers[0] = [p for p in patterns if len(p) == 6][0]

    patterns = [p for p in patterns if p != numbers[0]]

    numbers[2] = [e for e in [p for p in patterns if len(
        p) == 5] if len(numbers[9].difference(e)) == 2][0]

    patterns = [p for p in patterns if p != numbers[2]]

    numbers[5] = [e for e in [p for p in patterns if len(
        p) == 5] if len(numbers[6].difference(e)) == 1][0]

    patterns = [p for p in patterns if p != numbers[5]]

    numbers[3] = [p for p in patterns if len(p) == 5][0]

    numbers = {n: list(numbers[n]) for n in numbers}
    for n in numbers:
        numbers[n].sort()

    num_table = {''.join(list(numbers[n])): n for n in numbers.keys()}
    output = [list(o) for o in output]

    for o in output:
        o.sort()

    return int(''.join([str(num_table[''.join(o)]) for o in output]))


def solution(input):
    cnt = 0
    for entry in input:
        pattern, output = entry
        cnt += solve_line(pattern, output)
    return cnt


if __name__ == '__main__':
    print(solution(input))
