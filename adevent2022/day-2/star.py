from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    tot = 0
    for m in input:
        adv_move, your_move = m.split(" ")
        adv_val = "ABC".index(adv_move) + 1
        your_val = "XYZ".index(your_move) + 1
        diff = adv_val - your_val

        if diff == 0:
            r = 3
        elif diff == 1 or diff == -2:
            r = 0
        else:
            r = 6

        tot += r + your_val
    return tot


if __name__ == "__main__":
    print(solution(input))
