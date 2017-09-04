# Uses python3
import sys
LOWER = 1
UPPER = 1000


def get_change(m):
    if LOWER <= m <= UPPER:
        num_coin = 0
        amount = m
        for i in [10, 5, 1]:
            while amount // i != 0:
                num_coin += 1
                amount -= i

        return num_coin
    else:
        return "Invalid Input"

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
