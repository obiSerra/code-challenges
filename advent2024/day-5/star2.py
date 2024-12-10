from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]

def parse_input(input):
    rules = []
    updates = []
    for line in input:
        if "|" in line:
            rules.append(line.split("|"))
        elif line == "":
            continue
        else:
            updates.append(line.split(","))

    return rules, updates

def find_incorrect(rule_map, updates):
    invalids = []
    for upd in updates:
        valid = True
        for i, page in enumerate(upd):
            for j in range(i):
                if page in rule_map[upd[j]]["before"]:
                    valid = False
                    a = upd[j]
                    b = upd[i]

                    upd[i] = a
                    upd[j] = b
        if not valid:
            invalids.append(upd)
    return invalids


def solution(input):
    rules, updates = parse_input(input)
    rule_map = {}
    for rule in rules:
        f, s = rule
        if f not in rule_map:
            rule_map[f] = {"before": [], "after": []}
        if s not in rule_map:
            rule_map[s] = {"before": [], "after": []}

        rule_map[f]["after"].append(s)
        rule_map[s]["before"].append(f)
    

    invalids = find_incorrect(rule_map, updates)
    
    # print(invalids)
    centers = [int(v[len(v) // 2]) for v in invalids]
    return sum(centers)


if __name__ == '__main__':
    print(solution(input))