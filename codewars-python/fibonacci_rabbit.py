
def calculate_rabbits(n, b, mature=0, immature=1):
    if n <= 0:
        return mature
    return calculate_rabbits(n - 1, b, mature + immature, mature * b)


def fibo_rabbit(n, b):
    return calculate_rabbits(n, b)


if __name__ == "__main__":
    print(fibo_rabbit(5, 3))
