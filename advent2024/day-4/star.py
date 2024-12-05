from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


dirs = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
]

def debug_input(input, valid):
    dbg_input = []
    for i in range(len(input)):
        nl = []
        for _ in range(len(input[i])):
            nl.append(".")
        dbg_input.append(nl)
    
    for ((r,c, d), w) in valid:
      for i, (dx, dy) in enumerate(dirs[d]):
        if c +dx <0 or r + dy < 0:
            print(f"Error: {c + dx} {r + dy}")
        dbg_input[c + dx][r + dy] = w[i]


    for line in dbg_input:
        print(''.join(line))


def solution(input):
    words = []

    for r in range(len(input)):
        for c in range(len(input[r])):
            for di, d in enumerate(dirs):
                try:
                    word = ""
                    for dx, dy in d:
                        if c +dx >=0 and r + dy >= 0:
                            word += input[c + dx][r + dy]
                    words.append(((r, c, di), word))
                except Exception:
                    pass

    valid = [v for v in words if v[-1] == "XMAS" or v[-1] == "SAMX"]

    debug_input(input, valid[2526:2527])

    return len(valid)


if __name__ == "__main__":
    print(solution(input))
