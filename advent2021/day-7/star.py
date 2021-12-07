from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [int(n) for n in lines[0].split(',')]


def solution(input):
    min_val = min(input)
    max_val = max(input)
    points = {v: [] for v in range(min_val, max_val+1)}
    for inp in input:
        for p in points.keys():
            points[p].append(abs(p-inp))

    min_res = None
    for p in points.keys():
        s = sum(points[p])
        if min_res is None or s < min_res:
            min_res = s

    return min_res


if __name__ == '__main__':
    print(solution(input))
