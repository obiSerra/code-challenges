from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input_test.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


class Monkey:
    def __init__(self, definition) -> None:
        self.name = int(definition[0].split(" ")[1].replace(":", ""))
        items = definition[1].replace("Starting items: ", "").split(", ")
        self.items = [int(item) for item in items]
        self.operation = definition[2].replace("Operation: new = ", "").split(" ")

        self.value = 0

        # print(self.name, self.operation)

    def run_operations(self):
        while len(self.items) > 0:
            val = self.items.pop(0)
            print(val)


def solution(input):
    input.append("")
    monkeys = []
    data = []
    for a in input:
        data.append(a)
        if a == "":
            monkeys.append(Monkey(data))
            data = []

    # monkeys = monkeys[1:]
    for _ in range(20):
        for monkey in monkeys:
            monkey.run_operations()

    return None


if __name__ == "__main__":
    print(solution(input))
