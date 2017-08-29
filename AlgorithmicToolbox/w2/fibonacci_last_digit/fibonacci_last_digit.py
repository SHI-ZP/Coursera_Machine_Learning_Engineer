# Uses python3
import sys
import cProfile


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_v2(n):
    last_digit = []
    if 0 <= n <= 1000000:
        for i in range(n):
            if 0 == i:
                last_digit.append(i % 10)
            elif 1 == i:
                last_digit.append(i % 10)
            else:
                last_digit.append((last_digit[i-1] + last_digit[i-2]) % 10)
    else:
        return "Input out of range."
    return (last_digit[n-1] + last_digit[n-2]) % 10


def get_fibonacci_last_digit_v3(n):
    if 0 <= n <= 1000000:
        if 0 <= n <= 1:
            return n
        _previous, _current = 0, 1
        for _ in range(n - 1):
            _previous, _current = _current, (_previous + _current) % 10
        return _current
    else:
        return "Input out of range."


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_v2(n))
    cProfile.run('get_fibonacci_last_digit_v2(n)')

    print(get_fibonacci_last_digit_v3(n))
    cProfile.run('get_fibonacci_last_digit_v3(n)')
