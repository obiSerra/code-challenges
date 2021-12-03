from os import path

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


def to_decimal(binary):
    rv = list(binary)
    sum = 0
    for i in range(0, len(rv)):
        n = int(rv[::-1][i]) * pow(2, i)
        sum += n
    return sum


def count_commons(input):
    counter = {}
    for entry in input:
        for i in range(0, len(entry)):
            if i not in counter:
                counter[i] = {'0': 0, '1': 0}
            counter[i][str(entry[i])] += 1
    return counter


def solution(input):
    counter = count_commons(input)
    gamma = ''
    epsilon = ''
    for c in counter.values():
        if c['0'] > c['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return to_decimal(gamma) * to_decimal(epsilon)


if __name__ == '__main__':
    print(solution(input))
