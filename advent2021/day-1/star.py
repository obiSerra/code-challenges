from os import path

input = [
    '199',
    '200',
    '208',
    '210',
    '200',
    '207',
    '240',
    '269',
    '260',
    '263',
]

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.rstrip() for line in lines]


def solution_1(input):
    last = None
    inc = 0
    for i in input:
        if last is not None and int(i) > last:
            inc += 1
        last = int(i)
    return inc



print(solution_1(input))
