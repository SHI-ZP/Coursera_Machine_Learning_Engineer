#Uses python3

import sys
from collections import namedtuple
sequence = namedtuple("number", "real virtual len")


def largest_number(a):
    # print(a)
    _sequence = list(map(lambda z: sequence(int(z), int(z) * (10**(3-len(str(z)))), len(str(z))), a))
    # print(_sequence)
    for i in range(len(_sequence)):
        if _sequence[i].len == 1:
            _sequence[i] = _sequence[i]._replace(virtual=_sequence[i].virtual + 99.9)

    # print(_sequence)
    _sequence.sort(key=lambda s: s.virtual, reverse=True)
    # print(_sequence)
    _final = list(map(lambda p: p.real, _sequence))
    # print("")
    # print(_final)

    res = ""
    for x in _final:
        res += str(x)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
