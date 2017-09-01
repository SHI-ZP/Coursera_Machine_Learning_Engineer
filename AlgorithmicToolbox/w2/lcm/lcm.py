# Uses python3
import sys
import cProfile
UPPER = 2000000000
LOWER = 1


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_v2(a, b):
    if LOWER <= a <= UPPER and LOWER <= b <= UPPER:
        _max, _min = max(a, b), min(a, b)
        for i in range(1, _min * _max + 1):
            if not (i * _max) % _min:
                return i * _max
    else:
        return "Input out of range."


def gcd_v2(a, b):
    if LOWER <= a <= UPPER and LOWER <= b <= UPPER:
        _remainder = a % b
        if _remainder:
            return gcd_v2(b, _remainder)
        else:
            return b
    else:
        return "Input out of range."


def lcm_v3(a, b):
    if LOWER <= a <= UPPER and LOWER <= b <= UPPER:
        _gcd = gcd_v2(a, b)
        return a * b // _gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_v3(a, b))