conv_table = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
rev_conv = {n: k for (k, n) in conv_table.items()}


def encode(st):
    return ''.join([c if c not in conv_table else conv_table[c] for c in st])


def decode(st):
    return ''.join([c if c not in rev_conv else rev_conv[c] for c in st])


print(encode('hello'))
print(decode('h2ll4'))
