from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def recursive_sol(l, asc):
    if len(l) < 2:
        return True
    
    d = l[0] - l[1]
    # print(l, asc, d)
    if d > -4 and d < 0 and asc:
        return recursive_sol(l[1:], asc)
    elif d < 4 and d > 0 and not asc:
        return recursive_sol(l[1:], asc)
    
    return False

def solution(input):
    ls = [[int(n) for n in l.split()] for l in input]
    correct = [recursive_sol(l, True if l[0]<l[1] else False)for l in ls]
    return correct.count(True)


if __name__ == '__main__':
    print(solution(input))
