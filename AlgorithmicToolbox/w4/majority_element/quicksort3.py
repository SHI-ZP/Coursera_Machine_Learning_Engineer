def partition3(array, left, right):
    a = array
    _pivot_value = a[left]
    _lt = left
    _gt = right
    i = left + 1
    while i <= _gt:
        if a[i] > _pivot_value:
            a[i], a[_gt] = a[_gt], a[i]
            _gt -= 1
        elif a[i] < _pivot_value:
            a[i], a[_lt] = a[_lt], a[i]
            i += 1
            _lt += 1
        else:
            i += 1

    return _lt, _gt, a


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                print(a)


def find_median_pivot(a, left, right):
    pivot_index_list = [left, int((left + right) / 2), right]
    pivot_value_list = [a[i] for i in pivot_index_list]
    bubble_sort(pivot_value_list)
    _median_index = 0
    for i in range(3):
        if a[pivot_index_list[i]] == pivot_value_list[1]:
            _median_index = i
            break

    return pivot_index_list[_median_index]


def sort_quick3(a, left, right):
    if left >= right:
        return a

    _median_index = find_median_pivot(a, left, right)
    a[left], a[_median_index] = a[_median_index], a[left]

    print("a before")
    print(a)
    _a = a
    while left < right:
        m1, m2, _a = partition3(a, left, right)
        if (m1 - left) < (right - m2):
            sort_quick3(_a, left, m1 - 1)
            left = m2 + 1
        else:
            sort_quick3(_a, m2 + 1, right)
            right = m1 - 1
    print("a after")
    print(_a)
    return _a

if __name__ == '__main__':
    from random import randint
    a = [randint(1, 100) for i in range(10)]
    # a = [36, 64, 18, 4, 61, 78, 8, 22, 72, 92]
    print(a)
    print(sort_quick3(a, 0, len(a)-1))
