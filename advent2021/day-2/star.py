from os import path

input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.rstrip() for line in lines]


class Submarine:
    depth = 0
    fwd = 0


def solution(input):
    sub = Submarine()

    for cmd in input:
        val = int(cmd.split(' ')[1])
        if cmd.startswith('forward'):
            sub.fwd += val
        elif cmd.startswith('up'):
            sub.depth -= val
        elif cmd.startswith('down'):
            sub.depth += val

    return sub.depth * sub.fwd


if __name__ == '__main__':
    print(solution(input))
