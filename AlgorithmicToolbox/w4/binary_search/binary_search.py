# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    middle = a[left + int((right-left)/2)]
    # if middle <=

    while left <= right:
        # print("left-right " + str(left-right))
        index_middle = left + int((right - left) / 2)
        # print("index_middle " + str(index_middle))
        if a[index_middle] > x:
            right = index_middle - 1
        elif a[index_middle] < x:
            left = index_middle + 1
        else:
            return index_middle

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        # print("x")
        # print(x)
        print(binary_search(a, x), end = ' ')

# 5 1 5 8 12 13
# 5 8 1 23 1 11

# 10 2 3 4 5 6 7 8 9 10 11
# 12 1 2 3 4 5 6 7 8 9 10 11 12
