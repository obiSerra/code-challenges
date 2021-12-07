from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [int(n) for n in lines[0].split(',')]


def solution(input):
    costs = {}

    min_val = min(input)
    max_val = max(input)
    points = {v: [] for v in range(min_val, max_val+1)}
    for inp in input:
        for p in points.keys():
            dist = abs(p-inp)
            if dist not in costs:
                cost = 0
                for i in range(0, dist+1):
                    cost += i

                costs[dist] = cost
            else:
                cost = costs[dist]
            points[p].append(cost)

    min_res = None
    for p in points.keys():
        s = sum(points[p])
        if min_res is None or s < min_res:
            min_res = s

    return min_res


if __name__ == '__main__':
    print(solution(input))
