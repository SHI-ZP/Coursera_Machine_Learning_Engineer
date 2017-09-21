def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


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

if __name__ == '__main__':
    a = [1, 7, 1, 6, 6, 5, 6, 3]
    print(find_median_pivot(a, 0, 7))