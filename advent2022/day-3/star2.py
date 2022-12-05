from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]

alph = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solution(input):
    groups = []
    for i in range(0, len(input), 3):
        groups.append(input[i: i + 3])

    tot = 0
    for g in groups:
        all_c = set(g[0] + g[1] + g[2])
        common = [c for c in all_c if c in g[0] and c in g[1] and c in g[2]][0]
        tot += alph.index(common)
    return tot


if __name__ == "__main__":
    print(solution(input))
