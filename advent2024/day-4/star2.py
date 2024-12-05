from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


dirs = [

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
    kernel = [
        [(0, 0), (1,1), (2,2)],
        [(0, 2), (1,1), (2,0)],
    ]
    valid = []
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "A":
                sq = []
                try:
                    zr = r-1
                    zc = c-1

                    for k in kernel:
                        word = []
                        for dx, dy in k:
                            if zr + dx >= 0 and zc + dy >= 0:
                                word.append(input[zr + dx][zc + dy])
                        word.sort()

                        sq.append(''.join([''.join(w) for w in word]))
                except Exception:
                    pass 

                if ''.join(sq) == 'AMSAMS':
                    valid.append((r, c))
    return len(valid)
    

if __name__ == "__main__":
    print(solution(input))
