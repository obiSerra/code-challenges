from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def find_res(a, b, v):
    dx = a[0] - b[0]
    dy = a[1] - b[1]

    i = 0
    r = []
    while a[0] - dx*i >= 0 and  a[1] - dy*i >=0 and (a[0] - dx*i) <= len(input) and (a[1] - dy*i) <= len(input[0]):
        try:
            r.append((a[0] - dx*i, a[1] - dy*i, v))
            i += 1
        except IndexError:
            print('break')
            break
    i = 0
    while a[0] + dx*i >= 0 and  a[1] + dy*i >=0 and (a[0] + dx*i) <= len(input) and (a[1] + dy*i) <= len(input[0]):
        try:
            r.append((a[0] + dx*i, a[1] + dy*i, v))
            i += 1
        except IndexError:
            break
    

    return r


def solution(input):
    antennas = {}
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col != '.':
                if col not in antennas:
                    antennas[col] = []
                antennas[col].append((i, j))

    res = []
    input = [list(row) for row in input]
    
    c = 0
    for antenna in antennas.items():
        if len(antenna[1]) == 1:
            continue
        c += len(antenna[1])
        for a in antenna[1]:
            for b in antenna[1]:
                if a != b:
                    res += find_res(a, b, input[a[0]][a[1]])
    
    for r in res:
        try:
            if r[0] >= 0 and r[1] >= 0:
                if input[r[0]][r[1]] == '.':
                    input[r[0]][r[1]] = '#'
        except IndexError:
            pass

    for row in input:
        c += row.count('#')
            
    # print('\n'.join([''.join(row) for row in input]))   
    return c


if __name__ == '__main__':
    print(solution(input))
