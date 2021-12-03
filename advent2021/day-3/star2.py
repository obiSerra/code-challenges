from os import path

from star import count_commons, to_decimal

input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.rstrip() for line in lines]


def filter_by_common(i, els, common=True):
    counter = count_commons(els)
    counter_vals = [c for c in counter.values()]
    c = counter_vals[i]
    comm = '0' if c['0'] > c['1'] else '1'
    if len(els) > 1 and common is True:
        els = [o for o in els if o[i] == comm]
    elif len(els) > 1 and common is False:
        els = [o for o in els if o[i] != comm]
    return els


def filter_by_uncommon(i, els):
    return filter_by_common(i, els, False)


def solution(input):
    counter = count_commons(input)
    counter_vals = [c for c in counter.values()]

    oxy = [i for i in input]
    co2 = [i for i in input]

    for i in range(0, len(counter_vals)):
        oxy = filter_by_common(i, oxy)
        co2 = filter_by_uncommon(i, co2)

    return to_decimal(oxy[0]) * to_decimal(co2[0])


if __name__ == '__main__':

    assert solution(input) == 903810
    print(solution(input))
