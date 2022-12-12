from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def need_to_move(t, h):
    return abs(t[0] - h[0]) > 1 or abs(t[1] - h[1]) > 1


def move_tail(tail, head):
    if not need_to_move(tail, head):
        return tail

    if tail[0] == head[0]:
        if head[1] > tail[1]:
            return (tail[0], tail[1] + 1)
        else:
            return (tail[0], tail[1] - 1)

    elif tail[1] == head[1]:
        if head[0] > tail[0]:
            return (tail[0] + 1, tail[1])
        else:
            return (tail[0] - 1, tail[1])

    elif head[0] > tail[0] and head[1] > tail[1]:
        return (tail[0] + 1, tail[1] + 1)
    elif head[0] > tail[0] and head[1] < tail[1]:
        return (tail[0] + 1, tail[1] - 1)
    elif head[0] < tail[0] and head[1] < tail[1]:
        return (tail[0] - 1, tail[1] - 1)
    elif head[0] < tail[0] and head[1] > tail[1]:
        return (tail[0] - 1, tail[1] + 1)


def solution(input):
    head = (0, 0)
    tail = (0, 0)

    positions = set()

    for i in input:
        d, length = i.split(" ")
        length = int(length)
        for j in range(length):
            if d == "R":
                head = (head[0] + 1, head[1])
            elif d == "L":
                head = (head[0] - 1, head[1])
            elif d == "U":
                head = (head[0], head[1] + 1)
            elif d == "D":
                head = (head[0], head[1] - 1)

            tail = move_tail(tail, head)
            positions.add(tail)

    return len(positions)


if __name__ == "__main__":
    print(solution(input))
