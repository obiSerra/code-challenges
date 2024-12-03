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
    valid =re.findall(r'mul\(\d+,\d+\)', input)
    mul = [re.findall(r'\d+', i) for i in valid]
    
    mul = [int(i[0]) * int(i[1]) for i in mul]

    return sum(mul)


if __name__ == '__main__':
    print(solution(input))
