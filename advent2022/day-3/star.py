from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


alph = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solution(input):
    lst = [list(i) for i in input]
    sacks = [[s[: (len(s) // 2)], s[(len(s) // 2) :]] for s in lst]
    common = [[a for a in s[0] if a in s[1]][0] for s in sacks]
    return sum([alph.index(a) for a in common])


if __name__ == "__main__":
    print(solution(input))
