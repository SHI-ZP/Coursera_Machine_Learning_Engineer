def partition3(array, left, right):
    a = array
    _pivot_value = a[left]
    _lt = left
    _gt = right
    i = left + 1
    while i <= _gt:
        if a[i] > _pivot_value:
            a[i], a[_gt] = a[_gt], a[i]
            # i += 1
            _gt -= 1
        elif a[i] < _pivot_value:
            a[i], a[_lt] = a[_lt], a[i]
            i += 1
            _lt += 1
        else:
            i += 1

    if _lt != 0:
        a[0], a[_lt-1] = a[_lt-1], a[0]

    return _lt, _gt, a

if __name__ == '__main__':
    from random import randint
    a = [randint(1, 100) for i in range(10)]
    print(a)
    print(partition3(a, 0, len(a)-1))
    # print(partition3([36, 64, 18, 4, 61, 78, 8, 22, 72, 92], 0, len(a)-1))
