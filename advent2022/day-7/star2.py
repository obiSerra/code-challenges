from os import path
from star import recursionlimit, nav_fs

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def get_dir(fs, rem, to_del=float("inf")):
    size = fs.get_size()
    if size > rem and size < to_del:
        to_del = size

    for d in fs.get_subdirs():
        to_del = get_dir(fs[d], rem, to_del)

    return to_del


def solution(input):
    with recursionlimit(10000):
        fs = nav_fs(input)

    tot = 70000000
    needed = 30000000
    unused = tot - fs.get_size()
    rem = needed - unused
    return get_dir(fs, rem)


if __name__ == "__main__":
    print(solution(input))
