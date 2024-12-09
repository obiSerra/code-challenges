from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]
    input = input[0]

def expand_input(input):
    expanded = []
    idx = 0
    expanded_map = {}
    empty_map = {}
    for i, n in enumerate(input):
        if i%2 == 0:
            expanded_map[idx] = (int(n), len(expanded))
            expanded += [idx]*int(n)
            idx += 1
        else:
            empty_map[len(expanded)] = int(n)
            expanded += ["."]*int(n)
    return expanded, empty_map, expanded_map


def solution(input):
    input, empty_map, expanded_map = expand_input(input)
    empty_map = list(empty_map.items())
    expanded_map = list(expanded_map.items())
    expanded_map.sort(key=lambda x: x[0], reverse=True)

    for i, (id, (v, i_ps)) in enumerate(expanded_map):
        
        for j, (id2, v2) in enumerate(empty_map):
            if v <= v2 and id2 < i_ps:
                input[id2:id2+v] = [id]*v
                input[i_ps:i_ps+v] = ["."]*v
                empty_map[j] = (id2+v, v2-v)
                break    
    s = 0
    for i, n in enumerate(input):
        if n != ".":
            s += i*n    
    return s


if __name__ == '__main__':
    print(solution(input))
