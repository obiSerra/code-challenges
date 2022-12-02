from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def solution(input):
    tot = 0
    for m in input:
        adv_move, exp_res = m.split(" ")
        adv_val = "ABC".index(adv_move) + 1

        if exp_res == "Y":
            your_val = adv_val
            r = 3
        elif exp_res == "X":

            if adv_val == 1:
                your_val = 3
            elif adv_val == 2:
                your_val = 1
            else:
                your_val = 2
            r = 0
        else:
            if adv_val == 1:
                your_val = 2
            elif adv_val == 2:
                your_val = 3
            else:
                your_val = 1

            r = 6

        tot += r + your_val
    return tot


if __name__ == "__main__":
    print(solution(input))
