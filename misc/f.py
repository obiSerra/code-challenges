import sys


def nth_fb(nth, memo={}):
    if nth in memo:
        return memo[nth]
    if (nth == 1) or (nth == 2):
        return 1
    else:
        v = nth_fb(nth - 1) + nth_fb(nth - 2)
        memo[nth] = v
        return v


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python f.py <nth>")
        exit(1)

    print(nth_fb(int(sys.argv[1])))
