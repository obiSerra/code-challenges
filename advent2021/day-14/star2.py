from os import path
import math
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def run_step(template, rules, memo):
    new_template = template
    for r in rules.keys():
        new_template = new_template.replace(r, rules[r])
    return new_template


def count_occurences(string):
    occ = {}
    [occ.update({s: occ.get(s, 0)+1}) for s in string]
    return occ


def solution(input):
    template = input[0]
    rules = {k[0]: k[0][0] + k[1] + k[0][1]
             for k in [r.split(' -> ') for r in input[2:]]}
    for i in range(0, 10):
        template = run_step(template, rules, {})

    occurences = count_occurences(template).values()

    return max(occurences) - min(occurences)


if __name__ == '__main__':
    assert solution(input) == 2360
    print(solution(input))
