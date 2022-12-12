from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def need_to_move(t, h):
    return abs(t[0] - h[0]) > 1 or abs(t[1] - h[1]) > 1


def move_tail(tail, head):
    # print("need_to_move", need_to_move(tail, head))
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
    tails = [(0, 0) for _ in range(9)]
    positions = set()

    for i in input:
        d, length = i.split(" ")
        length = int(length)
        # print(d, length)
        for j in range(length):
            if d == "R":
                head = (head[0] + 1, head[1])
            elif d == "L":
                head = (head[0] - 1, head[1])
            elif d == "U":
                head = (head[0], head[1] + 1)
            elif d == "D":
                head = (head[0], head[1] - 1)

            p_t = head
            for _ in range(9):

                tails[_] = move_tail(tails[_], p_t)
                p_t = tails[_]
                # print(head, tail)
            positions.add(tails[8])

    # print(len(positions), positions)

    # for x in range(6):
    #     for y in range(6):
    #         if x == 0 and y == 0:
    #             print("s", end="")
    #         if (y, x) in positions:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()

    return len(positions)


if __name__ == "__main__":
    print(solution(input))
