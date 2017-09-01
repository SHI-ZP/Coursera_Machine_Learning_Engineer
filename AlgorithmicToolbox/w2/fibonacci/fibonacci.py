# Uses python3
import cProfile


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_v2(n):
    if 0 <= n <= 45:
        if n <= 1:
            return n

        result = []
        for i in range(n):
            if 0 == i:
                result.append(0)
            elif 1 == i:
                result.append(1)
            else:
                result.append((result[i - 1] + result[i - 2]))
        return result[n - 1] + result[n - 2]
    else:
        return "Input out of range."


n = int(input())
print(calc_fib_v2(n))
# cProfile.run('calc_fib_v2(n)')
