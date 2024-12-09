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


    return [(a[0] - dx, a[1] - dy, v), (a[0] + dx, a[1] + dy, v)]


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
    for antenna in antennas.items():
        for a in antenna[1]:
            for b in antenna[1]:
                if a != b:
                    res += find_res(a, b, input[a[0]][a[1]])

    for r in res:
        try:
            if r[0] >= 0 and r[1] >= 0:
                if input[r[0]][r[1]] == '.' or input[r[0]][r[1]] != r[2]:
                    input[r[0]][r[1]] = '#'
        except IndexError:
            pass

    c = 0
    for row in input:
        c += row.count('#')
            
    # print('\n'.join([''.join(row) for row in input]))   
    return c


if __name__ == '__main__':
    print(solution(input))
