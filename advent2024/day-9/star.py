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
    for i, n in enumerate(input):
        if i%2 == 0:
            expanded += [idx]*int(n)
            idx += 1
        else:
            expanded += ["."]*int(n)
    return expanded


def solution(input):
    input = expand_input(input)
    first_empty = input.index(".")

    for i in range(len(input)-1, 0, -1):
        if input[i] == ".":
            continue
        else:
            input[first_empty] = input[i]
            input[i] = "."
            first_empty = input.index(".")
            if first_empty == i-1:
                break
    s = 0
    for i, n in enumerate(input):
        if n == ".":
            break
        s += i*n
    return s


if __name__ == '__main__':
    print(solution(input))
