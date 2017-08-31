# Uses python3
import sys
import cProfile
UPPER = 2000000000
LOWER = 1


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_v2(a, b):
    if LOWER <= a <= UPPER and LOWER <= b <= UPPER:
        _remainder = a % b
        if _remainder:
            return gcd_v2(b, _remainder)
        else:
            return b
    else:
        return "Input out of range."


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    # cProfile.run('gcd_naive(a, b)')

    print(gcd_v2(a, b))
    # cProfile.run('gcd_v2(a, b)')

    # 28851538 1183019
    # 17657

