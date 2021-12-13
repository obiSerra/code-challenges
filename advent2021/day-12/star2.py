from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip().split('-') for line in lines]


def make_adj(input):
    adj = {}
    for el in input:
        a, b = el
        if a not in adj:
            adj[a] = []
        if b not in adj:
            adj[b] = []
        adj[a].append(b)
        adj[b].append(a)
    return adj


def can_be_visited(path, cave):
    if cave == 'start':
        return False

    cnt = len([c for c in path if c == cave])

    mins = [c for c in path if c.upper() != c]

    mins_rep = len(mins) - len(set(mins))

    if cave.upper() != cave and mins_rep + cnt > 1:
        return False

    return True


def explore_all(adj_list, paths):
    new_paths = [p for p in paths if 'end' in p]
    to_explore = [p for p in paths if 'end' not in p]

    if not to_explore:
        return paths
    for pth in to_explore:
        last_p = pth[-1]
        next_moves = adj_list[last_p]
        for move in next_moves:
            all_pth = [pt for pt in pth]
            if can_be_visited(all_pth, move):
                all_pth.append(move)
                new_paths.append(all_pth)

    return explore_all(adj_list, new_paths)


def solution(input):
    adj = make_adj(input)
    return len(explore_all(adj, [['start']]))


if __name__ == '__main__':
    print(solution(input))
