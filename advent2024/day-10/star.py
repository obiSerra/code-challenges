from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[int(n) for n in line.strip()] for line in lines]

def calculate_trail(input, point, ends):

    x, y = point
    if x < 0 or y < 0:
        return []
    try:
        v = input[x][y]
    except IndexError:
        return []
    
    if v == 9:
        return [tuple(point)]

    next_stp = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]

    valid_steps = []
    for step in next_stp:
        try:
            if input[step[0]][step[1]] == v+1:
                valid_steps.append(step)
        except IndexError:
            pass

    end_list = []
    for valid_step in valid_steps:
        end_list += calculate_trail(input, valid_step, ends)
    
    return end_list

def solution(input):

    starting_point = []

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                starting_point.append((i, j))

    res = []
    for point in starting_point:
        res.append(calculate_trail(input, point, []))

    c = 0
    for i in range(len(res)):
        c += len(set(res[i]))

    return c


if __name__ == '__main__':
    print(solution(input))
