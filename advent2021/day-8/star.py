from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[w.strip().split(' ') for w in line.strip().split('|')] for
             line in lines]


def solution(input):
    cnt = 0
    for entry in input:
        _, output = entry
        to_count = [2, 4, 3, 7]
        for o in output:
            if len(o) in to_count:
                cnt += 1
    return cnt


if __name__ == '__main__':
    print(solution(input))
