from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip().split(":") for line in lines]

    input = [(int(line[0].strip()), [int(n) for n in line[1].strip().split(" ")]) for line in input]

def solve_eq(result, current, numbers):
    if len(numbers) == 0:
        return current == result

    ops = ["+", "*"]

    res = []
    for op in ops:
        new_current = current
        if op == "+":
            new_current += numbers[0]
            res.append(solve_eq(result, new_current, numbers[1:])) 
        elif op == "*":
            new_current *= numbers[0]
            res.append(solve_eq(result, new_current, numbers[1:]))

    return any(res)

def solution(input):
    tot = 0
    for line in input:
        res = solve_eq(line[0], line[1][0], line[1][1:])
        if res:
            tot += line[0]
    return tot


if __name__ == '__main__':
    print(solution(input))
