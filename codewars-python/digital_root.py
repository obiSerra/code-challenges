def digital_root(n):
    while n > 9:
        n = sum([int(e) for e in str(n)])
    return n


print(digital_root(942))
