from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


class Register:
    def __init__(self) -> None:
        self.cycle = 0
        self.x = 1
        self.total = 0

    def _register(self, i):
        if (self.cycle - 20) % 40 == 0:
            print(self.cycle, self.x, self.total, i)
            self.total += self.x * self.cycle

    def execute(self, instruction):
        if instruction == "noop":
            self.cycle += 1
            self._register(instruction)
        elif instruction.startswith("addx"):
            self.cycle += 1
            self._register(instruction)
            self.cycle += 1
            self._register(instruction)
            self.x += int(instruction.split(" ")[1])


def solution(input):
    reg = Register()
    for i in input:
        reg.execute(i)
    return reg.total


if __name__ == "__main__":
    print(solution(input))
