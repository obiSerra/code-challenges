from os import path
import re
input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]
    input = ''.join(input)

def solution(input):
    valid =re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', input)

    enabled = True
    mul = []
    for v in valid:
        if 'don\'t' in v:
            enabled = False
        elif 'do' in v:
            enabled = True
        elif enabled:
            m = re.findall(r'\d+', v)
            mul.append(int(m[0]) * int(m[1]))

    return sum(mul)


if __name__ == '__main__':
    print(solution(input))
