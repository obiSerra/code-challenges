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
        self.to_draw = []

    def _register(self, i):
        col = self.cycle % 40
        if abs(col - self.x) <= 1:
            self.to_draw.append(self.cycle)

    def execute(self, instruction):
        if instruction == "noop":
            self._register(instruction)
            self.cycle += 1
        elif instruction.startswith("addx"):
            self._register(instruction)
            self.cycle += 1
            self._register(instruction)
            self.cycle += 1
            self.x += int(instruction.split(" ")[1])

    def draw(self):
        for i in range(241):
            if i > 0 and i % 40 == 0:
                print()
            if i in self.to_draw:
                print("#", end="")
            else:
                print(" ", end="")


def solution(input):
    reg = Register()
    for i in input:
        reg.execute(i)
    return reg.draw()


if __name__ == "__main__":
    print(solution(input))
