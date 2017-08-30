# Uses python3
import sys
import cProfile
LOWER = 0
UPPER = 10e+14


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_last_digit(n):
    if LOWER <= n <= UPPER:
        if n <= 1:
            return n
        else:
            _previous_last_digit = 0
            _current_last_digit = 1
            _sum_last_digit = 1
            for i in range(n - 1):
                _previous_last_digit, _current_last_digit = _current_last_digit, (_previous_last_digit + _current_last_digit) % 10
                _sum_last_digit += _current_last_digit
                _sum_last_digit %= 10

            # return _sum_last_digit
            return _current_last_digit


def main():
    for i in range(100):
        print(fibonacci_sum_last_digit(i))


if __name__ == '__main__':
    main()
    # input = sys.stdin.read()
    # n = int(input)
    # print(fibonacci_sum_last_digit(n))

    # cProfile.run('fibonacci_sum_last_digit(n)')