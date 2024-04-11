from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input_test.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]

def solution(input):
    return input


if __name__ == '__main__':
    print(solution(input))
