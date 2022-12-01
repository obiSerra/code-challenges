from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]


def split_couples(template):
    couples = []
    for i in range(1, len(template)):
        couples.append([template[i-1], template[i]])

    return couples


def run_step(template, rules):
    couples = split_couples(template)
    new_template = ''

    for c in couples:
        new_c = c[0] + rules[''.join(c)] + c[1]
        if new_template != '':
            new_template += new_c[1:]
        else:
            new_template = new_c
    return new_template


def count_occurences(string):
    occ = {}
    [occ.update({s: occ.get(s, 0)+1}) for s in string]
    return occ


def solution(input):
    template = input[0]
    rules = {k[0]: k[1] for k in [r.split(' -> ') for r in input[2:]]}
    for i in range(0, 10):
        template = run_step(template, rules)

    occurences = count_occurences(template).values()

    return max(occurences) - min(occurences)


if __name__ == '__main__':
    print(solution(input))
