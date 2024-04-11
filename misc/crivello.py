import argparse


def crivello(n):
    print(f"Crivello di Eratostene per {n}\n")
    nums = [True] * (n + 1)
    nums[0] = False
    nums[1] = False

    primi = []

    for i in range(2, n + 1):
        if nums[i]:
            primi.append(i)

            for j in range(i * i, n + 1, i):
                nums[j] = False

    # Codice per stampare i numeri primi su piu' righe
    print(f"Ci sono {len(primi)} numeri primi fino a {n}:")
    per_riga = 20
    for i in range(0, len(primi), per_riga):
        print(", ".join([str(p) for p in primi[i : i + per_riga]]))


# Questa parte serve solo per far funzionare lo script
parser = argparse.ArgumentParser(description="Scomposizioni.")
parser.add_argument("numero", metavar="N", type=int, help="il numero da scomporre")


if __name__ == "__main__":
    args = parser.parse_args()
    crivello(args.numero)
