# Uses python3
import sys
import cProfile


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_v2(n, m):
    if n <= 1:
        return n % m

    _previous = 0
    _current = 1
    _sequence = []

    for i in range(n + 1):
        if 0 == i:
            _sequence.append(0 % m)
        elif 1 == i:
            _sequence.append(1 % m)
        else:
            _previous, _current = _current, _previous + _current
            _sequence.append(_current % m)
            if 0 == _sequence[i-1] and 1 == _sequence[i]:
                for _ in range(2):
                    _sequence.pop()
                break
    return _sequence[n % len(_sequence)]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_v2(n, m))
