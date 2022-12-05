from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.replace("\n", "") for line in lines]


def parse_input(input):
    crates_h = []
    for i in input:
        if "[" not in i:
            break
        i = i.replace("    ", " - ")

        els = i.split(" ")
        els = [x.replace("[", "").replace("]", "") for x in els if x != ""]

        crates_h.append(els)
    crates = []
    for i in range(len(crates_h[0])):
        crates.append([])
        for c in crates_h:
            if c[i] != "-":
                crates[i].append(c[i])
    moves = []
    for i in input:
        if "move" not in i:
            continue
        ms = i.split(" ")
        m = [int(ms[1]), int(ms[3]) - 1, int(ms[5]) - 1]
        moves.append(m)
    return crates, moves


def solution(input, mover_9001=False):
    crates, moves = parse_input(input)

    for m in moves:
        to_move = [crates[m[1]].pop(0) for _ in range(m[0])]
        if not mover_9001:
            to_move.reverse()
        crates[m[2]] = to_move + crates[m[2]]
    return "".join([c[0] for c in crates])


if __name__ == "__main__":
    print(solution(input))
