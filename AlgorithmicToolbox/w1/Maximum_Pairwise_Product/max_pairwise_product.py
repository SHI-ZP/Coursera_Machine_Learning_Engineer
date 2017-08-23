# Uses python3
def _find_max(list):
    _max = 0
    for e in list:
        if e > _max:
            _max = e
    return _max

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    _1st_max = _find_max(a)
    a.remove(_1st_max)
    _2nd_max = _find_max(a)
    print(_1st_max * _2nd_max)
