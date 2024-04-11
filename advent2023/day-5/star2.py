from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input_test.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def get_dest(dest_start, source_start, len, value):
    if value > source_start and value <= source_start + len:
        delta = value - source_start
        return dest_start + delta
    return value


def intersection(a, b):
    only_a = []
    only_b = []
    both = []

    if a[0] < b[1] and a[1] > b[0]:
        if a[0] < b[0]:
            only_a = (a[0], b[0])
        else:
            only_b = (b[0], a[0])

        both = (max(a[0], b[0]), min(a[1], b[1]))

    else:
        only_a = a
        only_b = b

    return (only_a, only_b, both)


def verify_length(seed):
    c = 0
    for s in seed:
        c += s[1] - s[0]
    return c


def map_seed(k, vs, seeds):
    vs = [v for v in vs if len(v) > 0]
    to_return = set()
    
    
    
    for dest_start, source_start, l in vs:
        dest_start, source_start, l = int(dest_start), int(source_start), int(l)
        source_end = source_start + l
        found = False
        print([(a, c) for (a, b, c) in [intersection(seed, (source_start, source_end)) for seed in seeds] if len(c) > 0])
        for seed in seeds:
            only_a, _, both = intersection(seed, (source_start, source_end))
            if len(both) == 0:
                # print("FOUND", only_a, both)
                # if len(only_a) > 0:
                #     to_return.add(only_a)
                # if len(both) > 0:
                #     to_return.add(((dest_start + (both[0] - source_start), dest_start + (both[1] - source_start))))
                # to_return.append(only_a)

                found = True
            if found:
                break
        # if found:
        #     break

    to_return = list(to_return)
    if len(to_return) == 0:
        to_return = seeds
    to_return = [s for s in to_return if len(s) > 0]
    print(f"{k} => {to_return} {verify_length(to_return)}")
    return to_return


def solution(input):
    seeds = re.findall(r"\d+", input[0])
    seeds = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])) for i in range(0, len(seeds), 2)]

    maps = {}
    current_map = []
    current_map_name = None
    for l in input[1:]:
        k = re.findall(r"[a-z-]+", l)
        if len(k) > 0:
            if current_map_name is not None:
                maps[current_map_name] = current_map
            current_map = []
            current_map_name = k[0]
        else:
            current_map.append(re.findall(r"\d+", l))

    maps[current_map_name] = current_map

    # print("MAP CREATED")
    for seed_ in seeds:
        print(f"SEED: {seed_}")
        # s = int(s)

        seed = [seed_]
        for k, vs in maps.items():
            seed = map_seed(k, vs, seed)
        return min([s[0] for s in seed])


if __name__ == "__main__":
    print(solution(input))
