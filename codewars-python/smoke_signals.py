

days = [
    (["4", "5.1"], ["Ambush in the jungle", "Orange army retreats"]),
    (["4", "5.1", "3.2.1"], ["Tanks deployed",
     "Orange army retreats", "Ambush in the jungle"]),
    (["5.1"], ["Orange army retreats"])
]

days_2 = [(["8.2.1", "4.3.4", "1"], ["Ambush in the jungle", "General assassinated", "Ambush in the jungle"]),
          (["1", "2.2", "9.3"], ["Ambush in the jungle",
           "Orange army retreats", "Push into the mountains"]),
          (["4.3.4", "6"], ["Ambush in the jungle",
                            "Orange general goes on vacation"]),
          (["8.2.1", "9.3", "1"], ["Ambush in the jungle", "General assassinated", "Push into the mountains"])]


def decode_smoke_signals(days, mapping={}):
    if all(
            [len(c) + len(m) == 0 for c, m in [d for d in days]]):
        return mapping
    options = {}
    for i, d in enumerate(days):
        cc, mm = d
        for c in cc:
            if c in mapping:
                days[i][0].remove(c)
                days[i][1].remove(mapping[c])
    for d in days:
        cc, mm = d
        for c in cc:
            p_msgs = options.get(c, None)
            if p_msgs is None:
                options[c] = set(mm)
            else:
                options[c] = p_msgs.intersection(set(mm))
    mapping = {**mapping, **{c: list(options[c])[0]
                             for c in options.keys() if len(list(options[c])) == 1}}

    return decode_smoke_signals(days, mapping=mapping)


def test_solution():
    assert decode_smoke_signals(
        [(["4", "5.1"], ["Ambush in the jungle", "Orange army retreats"]),
         (["4", "5.1", "3.2.1"], ["Tanks deployed",
                                  "Orange army retreats", "Ambush in the jungle"]),
         (["5.1"], ["Orange army retreats"])]
    ) == {
        "5.1": "Orange army retreats",
        "4": "Ambush in the jungle",
        "3.2.1": "Tanks deployed"
    }

    assert decode_smoke_signals(days_2) == {
        "4.3.4": "Ambush in the jungle",
        "6": "Orange general goes on vacation",
        "1": "Ambush in the jungle",
        "8.2.1": "General assassinated",
        "9.3": "Push into the mountains",
        "2.2": "Orange army retreats"
    }

    print("IS OK")


if __name__ == "__main__":
    test_solution()
    # print(decode_smoke_signals(days))
    # print(decode_smoke_signals(days_2))
