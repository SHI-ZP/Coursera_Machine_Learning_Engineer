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


def fibonacci_sum_last_digit_v2(n):
    if n <= 1:
        return n % 10

    _previous = 0
    _current = 1
    _sequence = []

    for i in range(n + 1):
        if 0 == i:
            _sequence.append(0 % 10)
        elif 1 == i:
            _sequence.append(1 % 10)
        else:
            _previous, _current = _current, _previous + _current
            _sequence.append(_current % 10)
            if 0 == _sequence[i-1] and 1 == _sequence[i]:
                for _ in range(2):
                    _sequence.pop()
                break

    # _sum_sequence = sum(_sequence)
    # _divider = int(n / len(_sequence))
    # _remainder = n % len(_sequence)
    # _partial_sum_sequence_1 = sum(_sequence[:_remainder - 1])
    # _partial_sum_sequence_2 = sum(_sequence[:_remainder + 1])

    # _sum_last_digit_1 = (_divider * _sum_sequence + _partial_sum_sequence_1) % 10
    # _sum_last_digit_2 = (_divider * _sum_sequence + _partial_sum_sequence_2) % 10

    return (int(n / len(_sequence)) * sum(_sequence) + sum(_sequence[:(n % len(_sequence)) + 1])) % 10


def main():
    print(fibonacci_sum_naive(0))
    print(fibonacci_sum_naive(1))
    print(fibonacci_sum_naive(7))

    print(fibonacci_sum_last_digit_v2(0))
    print(fibonacci_sum_last_digit_v2(1))
    print(fibonacci_sum_last_digit_v2(7))
    fibonacci_sum_last_digit_v2(99999999999991)

if __name__ == '__main__':
    main()
    # input = sys.stdin.read()
    # n = int(input)
    # print(fibonacci_sum_last_digit_v2(n))
    # cProfile.run('fibonacci_sum_last_digit_v2(n)')
