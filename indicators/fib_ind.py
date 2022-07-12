def fibonacci_sequence(length):
    fib_seq = [None for x in range(length)]

    def fibonacci_value(n):
        if n == 0 or n == 1:
            return n
        else:
            a = fibonacci_value(n - 2)
            b = fibonacci_value(n - 1)
            return a + b

    for x in range(length):
        fib_seq[x] = fibonacci_value(x)

    return fib_seq


def fibonacci_ratios():
    sequence = fibonacci_sequence(15)
    fib_ratio = []

    for x in range(1, 4):
        ratio = round((sequence[-1-x] / sequence[-1]), 3)

        if x == 1:
            fib_ratio.append(round(ratio ** (1 / 2) * 100, 1))

        fib_ratio.append(round(ratio * 100, 1))

    return fib_ratio
