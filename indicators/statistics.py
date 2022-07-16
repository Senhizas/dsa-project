from base import OHLCV

class StatisticFunctions(OHLCV):

    def __init__(self, open_: list, high_: list, low_: list, close_: list, volume_: list) -> None:

        """Initializes the class accessing properties of the parent class OHLCV"""

        super().__init__(open_, high_, low_, close_, volume_)

    def slope(self, source: list, length):
        x_values = []
        y_values = []
        xy_values = []
        xsq_values = []

        for x in range(length):
            x_values.append(x+1)
            y_values.append(source[x])
            xy_values.append(x_values[-1] * y_values[-1])
            xsq_values.append(x_values[-1] ** 2)

        _slope = ((length * sum(xy_values)) - (sum(x_values) * sum(y_values))
                  ) / ((length * sum(xsq_values)) - (sum(x_values) ** 2)) * -1
        _average = sum(y_values) / length
        _intercept = (sum(y_values) - (_slope * sum(x_values))) / length

        return _slope, _average, _intercept

    def dev(self, source, length, slope, average, intercept):
        upper_dev = 0
        lower_dev = 0
        std_dev_acc = 0
        dsxx = 0
        dsyy = 0
        dsxy = 0
        period = length - 1
        daY = intercept + slope * period / 2
        _intercept = intercept

        for x in range(period):
            _price = self.high[x] - _intercept

            if _price > upper_dev:
                upper_dev = _price

            _price = _intercept - self.low[x]

            if _price > lower_dev:
                lower_dev = _price

            _price = source[x]
            dxt = _price - average
            dyt = _intercept - daY
            _price -= _intercept
            std_dev_acc += _price * _price
            dsxx += dxt * dxt
            dsyy += dyt * dyt
            dsxy += dxt * dyt
            _intercept += slope

        if period == 0:
            std_dev = (std_dev_acc / 1) ** (1 / 2)
        else:
            std_dev = (std_dev_acc / period) ** (1 / 2)

        if dsxx == 0 or dsyy == 0:
            pearsonR = 0
        else:
            pearsonR = dsxy / ((dsxx * dsyy) ** (1 / 2)) * -1

        return std_dev, pearsonR, upper_dev, lower_dev

    def lin_regression(self, close, length):
        s, a, i = self.slope(close, length)
        startPrice = i + s * (length - 1)
        endPrice = i
        std, pr, ud, ld = self.dev(close, length, s, a, i)

        upper_mult_input = 2.0
        lower_mult_input = 2.0
        upperStartPrice = startPrice + (upper_mult_input * std)
        upperEndPrice = endPrice + (upper_mult_input * std)
        lowerStartPrice = startPrice + (-lower_mult_input * std)
        lowerEndPrice = endPrice + (-lower_mult_input * std)

    def _fibonacci_sequence(self, length: int = 15):
        fib_seq = [None for x in range(length)]

        def _fibonacci_value(self, n):
            if n == 0 or n == 1:
                return n
            else:
                a = self._fibonacci_value(n - 2)
                b = self._fibonacci_value(n - 1)
                return a + b

        for x in range(length):
            fib_seq[x] = self._fibonacci_value(x)

        return fib_seq


    def fibonacci_ratios(self):
        sequence = self._fibonacci_sequence()
        fib_ratio = []

        for x in range(1, 4):
            ratio = round((sequence[-1-x] / sequence[-1]), 3)

            if x == 1:
                fib_ratio.append(round(ratio ** (1 / 2) * 100, 1))

            fib_ratio.append(round(ratio * 100, 1))

        return fib_ratio
