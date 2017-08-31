# Uses python3
import sys
import cProfile
LOWER = 0
UPPER = 10e+18


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum(head, end):
    if LOWER <= head <= end <= UPPER:
        if end <= 1:
            return end

        _previous = 0
        _current = 1
        _sequence = []
        _SET = [i for i in range(10)]

        for i in range(end + 1):
            if 0 == i:
                _sequence.append(0 % 10)
            elif 1 == i:
                _sequence.append(1 % 10)
            else:
                _previous, _current = _current, _previous + _current
                _sequence.append(_current % 10)
                if 0 == _sequence[i - 1] and 1 == _sequence[i]:
                    for _ in range(2):
                        _sequence.pop()
                    break

        if head < end:
            _complete_sum = (int(end / len(_sequence)) * sum(_sequence) + sum(_sequence[:(end % len(_sequence)) + 1]))
            _front_falf_sum = (int(head / len(_sequence)) * sum(_sequence) + sum(_sequence[:(head % len(_sequence))]))
            # print(_SET[(_complete_sum % 10) - (_front_falf_sum % 10)])
            return _SET[(_complete_sum % 10) - (_front_falf_sum % 10)]
        else:
            # print(_sequence[end % len(_sequence)])
            return _sequence[end % len(_sequence)]


def main():
    _from, _to = 1532341345435345, 1000000000000000000
    # print(fibonacci_partial_sum_naive(_from, _to))
    # print(fibonacci_partial_sum(_from, _to))

if __name__ == '__main__':
    main()
    input = sys.stdin.read()
    from_, to = map(int, input.split())

    print(from_)
    print(to)

    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))
