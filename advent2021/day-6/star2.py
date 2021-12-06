from os import path
from star import solution

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [int(n) for n in lines[0].split(',')]


if __name__ == '__main__':
    print(solution(input, 256))
