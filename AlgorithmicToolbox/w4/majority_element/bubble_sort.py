import random


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                # print(a)

if __name__ == '__main__':
    a = [random.randint(1, 100) for i in range(20)]
    bubble_sort(a)
    print(a)
