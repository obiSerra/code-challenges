import copy
from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [[int(n) for n in line.strip()] for line in lines]

def calculate_trail(input, point, path):
    x, y = point
    if x < 0 or y < 0:
        return []
    try:
        v = input[x][y]
    except IndexError:
        return []
    
    if v == 9:
        return path
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
        path.append(tuple([*point, input[point[0]][point[1]]]))
        end_list += calculate_trail(input, valid_step, path)
    
    return end_list

def solution(input):

    queue = []

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                queue.append([(i, j, 0)])

    complete_trails = []

    # queue = queue[0:1]
    while len(queue) > 0:
        trail = queue.pop(0)
        
        last_point = trail[-1]
        x, y, _ = last_point

        v = input[x][y]

        if v == 9:
            complete_trails.append(trail)

        next_stp = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
        valid_steps = []
        for step in next_stp:
            try:
                if input[step[0]][step[1]] == v+1 and step[0] >= 0 and step[1] >= 0:
                    valid_steps.append(step)
            except IndexError:
                pass
        # print(valid_steps)
        # exit()
        
        for valid_step in valid_steps:
            queue.append(trail + [(*valid_step, input[valid_step[0]][valid_step[1]])])

    # stps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l']
    # for t in complete_trails:
    #     o = copy.deepcopy(input)
    #     for p in t:
    #         x, y, v = p
    #         o[x][y] = stps[v]
        # print('\n'.join([''.join([str(cell) for cell in row]) for row in o]))
        # print('\n\n')

    trail_count = len(complete_trails)
    
    return trail_count

if __name__ == '__main__':
    print(solution(input))
