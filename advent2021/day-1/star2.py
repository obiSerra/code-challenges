from os import path
import math

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


def find_inc(input):
    last = None
    inc = 0
    for i in input:
        if last is not None and int(i) > last:
            inc += 1
        last = int(i)
    return inc


def solution(input):
    slices = {}
    for i in range(0, len(input)):
        slices_to_append = [i-j for j in range(0, 3) if i >= j]
        for sl in slices_to_append:
            if sl not in slices:
                slices[sl] = 0
            slices[sl] += int(input[i])

    return find_inc(slices.values())


print(solution(input))
