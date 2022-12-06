from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines][0]


def solution(input, buffer_length=4):
    buffer = []
    for i in range(len(input)):
        buffer.append(input[i])
        buffer = buffer[-buffer_length:]
        if len(set(buffer)) == buffer_length:
            return i + 1


if __name__ == "__main__":
    print(solution(input))
