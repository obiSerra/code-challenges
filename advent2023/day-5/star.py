from os import path
import re

input = []

final_path = path.join(path.dirname(path.abspath(__file__)), "input.txt")

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def get_dest(dest_start, source_start, len, value):
    if value > source_start and value <= source_start + len:
        delta = value - source_start
        return dest_start + delta
    return value


def solution(input):
    seeds = re.findall(r"\d+", input[0])

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

    locations = []
    # print("MAP CREATED")
    for s in seeds:
        # print(f"SEED: {s}")
        s = int(s)
        for k, vs in maps.items():
            # print(f"{k}")
            vs = [v for v in vs if len(v) > 0]
            for d_s, s_s, n in vs:
                dest = get_dest(int(d_s), int(s_s), int(n), s)
                # print(dest)
                # print(f"{k}: {s} -> {dest}")
                if dest != s:
                    s = dest
                    break
                s = dest

        locations.append(s)

    return min(locations)


if __name__ == "__main__":
    print(solution(input))
