from os import path

import sys


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        print(self.old_limit)
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


class Directory(dict):
    def __init__(self, name):
        self.name = name

    def get_size(self):
        size = 0
        for k, v in self.items():
            if isinstance(v, Directory):
                size += v.get_size()
            else:
                size += v
        return size

    def get_subdirs(self):
        return [k for k, v in self.items() if isinstance(v, Directory)]


def nav_fs(commands, fs=None, current_dir=[]):
    if fs is None:
        fs = Directory("/")
    if not commands:
        return fs

    command = commands.pop(0)
    if command.startswith("$ cd"):
        new_dir = command[5:]
        if new_dir == "..":
            current_dir.pop()
        else:
            current_dir.append(new_dir)
            f = fs
            for c in current_dir:
                if c in f:
                    f = f[c]
                else:
                    f[c] = Directory(c)
                    f = f[c]
    elif not command.startswith("$") and not command.startswith("dir"):
        size, file = command.split(" ")
        f = fs
        for c in current_dir:
            f = f[c]
        f[file] = int(size)

    return nav_fs(commands, fs, current_dir=current_dir)


def get_dir(fs, dirs=0):
    if fs.get_size() < 100000:
        dirs += fs.get_size()

    for d in fs.get_subdirs():
        dirs += get_dir(fs[d], 0)

    return dirs


def solution(input):
    with recursionlimit(10000):
        fs = nav_fs(input)
    return get_dir(fs)


if __name__ == "__main__":
    print(solution(input))
