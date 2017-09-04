# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    _current_capacity = capacity
    _unit_values = [values[i] / weights[i] for i in range(len(values))]
    _item_dict = {}
    for j in range(len(values)):
        _item_dict[_unit_values[j]] = [values[j], weights[j]]

    while _current_capacity > 0:
        if _current_capacity >= _item_dict[max(_item_dict.keys())][1]:
            _current_capacity -= _item_dict[max(_item_dict.keys())][1]
            value += _item_dict[max(_item_dict.keys())][0]
            _item_dict.pop(max(_item_dict.keys()))
        else:
            value += _current_capacity * max(_item_dict.keys())
            _current_capacity = 0
        print(_current_capacity)

    return value


def main():
    capacity = 60
    weights = [20, 50, 30]
    values = [60, 100, 120]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

if __name__ == "__main__":
    # main()
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
