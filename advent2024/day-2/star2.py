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
    if d > -4 and d < 0 and asc:
        return recursive_sol(l[1:], asc)
    elif d < 4 and d > 0 and not asc:
        return recursive_sol(l[1:], asc)

    return False

def solution(input):
    ls = [[int(n) for n in l.split()] for l in input]
    correct = [recursive_sol(l, True if l[0]<l[1] else False) for l in ls]
    c = correct.count(True)
    for i,v in enumerate(correct):
        if not v:
            to_check = ls[i]
            nl = [to_check[:j] + to_check[j+1:] for j in range(len(to_check))]
            correct = [recursive_sol(l, True if l[0]<l[1] else False) for l in nl]
            if correct.count(True) > 0:
                c += 1


    return c

if __name__ == '__main__':
    print(solution(input))
