# Uses python3
import sys


def optimal_summands(n):
    if not (1 <= n <= 10e+9):
        return ['Invalid Input']

    summands = []
    _least = 1
    _num = n

    # for i in range(n):
    #     if 2 * _least < _num:
    #         summands.append(_least)
    #         _least += 1
    #
    #     else:
    #         break

    while True:
        if 2 * _least < _num:
            summands.append(_least)
            _num -= _least
            _least += 1
        else:
            summands.append(_num)
            break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

    print("")
    _sum = 0
    for x in summands:
        _sum += x
    print(_sum)
