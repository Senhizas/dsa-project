import matplotlib.pyplot as plt
from sample_data import *


def linear_insert(array, k, item) -> list:
    """Function arguments:
    array is a linear array
    k is a positive integer such that k <= len(array)
    item is the specific element to be inserted at kth position."""

    n = len(array) - 2
    j = n

    while j >= k:
        array[j+1] = array[j]
        j = j - 1

    array[k] = item
    n = n + 1

    return array


def fibonacci_sequence(length: int = 15) -> list:
    """The Fibonacci Sequence is the series of numbers: 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number 
    is found by adding up the two numbers before it

    Function arguments:
    length(default) = 15; length of the fibonacci sequence"""

    fib_seq = [None for x in range(length)]

    def _fibonacci_value(n) -> int:

        if n == 0 or n == 1:
            return n
        else:
            a = _fibonacci_value(n - 2)
            b = _fibonacci_value(n - 1)
            return a + b

    for x in range(length):
        fib_seq = linear_insert(fib_seq, x, _fibonacci_value(x))

    return fib_seq


def fibonacci_ratios() -> list:
    """Fibonacci ratios are informed by mathematical relationships 
    found using fibonnaci sequence.
    See https://www.investopedia.com/terms/f/fibonacciretracement.asp """

    sequence = fibonacci_sequence()
    fib_ratio_array = [None for x in range(7)]

    for x in range(6):
        ratio = round((sequence[-1-x] / sequence[-1]), 3)

        if x == 1:
            _ratio = round(ratio ** (1 / 2), 3)
            fib_ratio_array = linear_insert(fib_ratio_array, x, _ratio)
        elif x == 4:
            ratio = (sequence[0] / sequence[1])
        elif x == 5:
            ratio = (sequence[2] / sequence[3])

        value = ratio
        fib_ratio_array = linear_insert(fib_ratio_array, x, value)

    return fib_ratio_array


def bubble_sort(data) -> list:
    """Bubble sort is an algorithm that sorts the elements 
    in the given array.
    Function arguments:
    data is a linear array"""

    n = len(data) - 2

    for k in range(n):
        ptr = 0

        while ptr <= n-k:
            if data[ptr] > data[ptr+1]:
                data[ptr], data[ptr+1] = data[ptr+1], data[ptr]

            ptr = ptr + 1

    return data


def main():
    fib_ratios = fibonacci_ratios()
    fib_retracement_level = bubble_sort(fib_ratios)

    def _plots_for_different_scenarios(data, title):
        max_value = max(data)
        min_value = min(data)

        difference = round(max_value - min_value, 3)
        first_level = round(max_value - difference * fib_retracement_level[1], 3)
        second_level = round(max_value - difference * fib_retracement_level[2], 3)
        third_level = round(max_value - difference * fib_retracement_level[3], 3)
        fourth_level = round(max_value - difference * fib_retracement_level[4], 3)
        fifth_level = round(max_value - difference * fib_retracement_level[5], 3)

        plt.figure(figsize=(15, 8))
        plt.plot(data, linewidth=3, color='cornflowerblue')
        plt.axhline(max_value, label=fib_retracement_level[0], linewidth=2.5, linestyle='--', alpha=0.5, color='black')
        plt.axhline(first_level, label=fib_retracement_level[1], linewidth=2.5, linestyle='--', alpha=0.5, color='red')
        plt.axhline(second_level, label=fib_retracement_level[2], linewidth=2.5, linestyle='--', alpha=0.5, color='purple')
        plt.axhline(third_level, label=fib_retracement_level[3], linewidth=2.5, linestyle='--', alpha=0.5, color='orange')
        plt.axhline(fourth_level, label=fib_retracement_level[4], linewidth=2.5, linestyle='--', alpha=0.5, color='green')
        plt.axhline(fifth_level, label=fib_retracement_level[5],linewidth=2.5, linestyle='--', alpha=0.5, color='fuchsia')
        plt.axhline(min_value, label=fib_retracement_level[6], linewidth=2.5, linestyle='--', alpha=0.5, color='aqua')
        plt.title(title)
        plt.xlabel('Index')
        plt.ylabel('Random Price Data')
        plt.legend()
        plt.show()

    # Scenario 1
    _plots_for_different_scenarios(sample_data_1, f'Data reflecting from {38.2}% Fibonacci level.')

    # Scenario 2
    _plots_for_different_scenarios(sample_data_2, f'Data reflecting from {78.6}% Fibonacci level.')

    # Scenario 3
    _plots_for_different_scenarios(sample_data_3, f'Data testing {38.2}% and {78.6}% Fibonacci levels.')

    # Scenario 4
    _plots_for_different_scenarios(sample_data_4, f'Data testing {38.2}% and {50}% Fibonacci levels.')


if __name__ == "__main__":
    main()
