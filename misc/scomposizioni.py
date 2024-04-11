import argparse


# Funzioni Utili


def numero_primo(n):
    mid = n // 2  # Parto dalla meta' del numero (perche' non ci sono divisori oltre la meta')
    for i in range(2, mid + 1):  # Parto da 2 (perche' 1 e' divisore di tutti i numeri)
        if n % i == 0:  # Se il resto della divisione e' 0, allora il numero non e' primo
            return False  # Ritorno False
    return True  # Se non ho trovato divisori, allora il numero e' primo


def trova_divisore(n, min=2):
    mid = n // 2  # Parto dalla meta' del numero (perche' non ci sono divisori oltre la meta')
    for i in range(min, mid + 1):  # Parto da 2 (perche' 1 e' divisore di tutti i numeri)
        if n % i == 0:  # Se il resto della divisione e' 0, allora ho trovato il divisore
            return i  # Rirorno il divisore
    return n  # Se non ho trovato divisori, allora il numero e' primo


def scomponi(n):
    v = n
    divisori = {}
    print(f"Scomponi {str(n)}\n")
    while v > 1:
        d = trova_divisore(v, max(list(divisori.keys()) + [2]))

        divisori[d] = divisori.get(d, 0) + 1
        print(f"{v} | {d}")
        v = v // d

    print("1 | 1")
    fact = ", ".join([f"{f} ^ {divisori[f]}" for f in divisori.keys()])
    print(f"\nScomposizione: {fact}")


# Questa parte serve solo per far funzionare lo script
parser = argparse.ArgumentParser(description="Scomposizioni.")
parser.add_argument("numero", metavar="N", type=int, help="il numero da scomporre")


if __name__ == "__main__":
    args = parser.parse_args()
    scomponi(args.numero)
