def ema(close, length):
    smoothing_constant = 2 / (length + 1)
    ema_array = []

    for x in range(len(close)):
        if x == 0:
            _sma = sum(close[:length]) / length

        if x == 1:
            _ema = (close[x] - _sma) * smoothing_constant + _sma
            ema_array.append(round(_ema, 2))

        if x > 1:
            _ema = (close[x] - ema_array[-1]) * \
                smoothing_constant + ema_array[-1]
            ema_array.append(round(_ema, 2))

    return ema_array


def macd(ema, close):
    ema26 = ema(close, 26)
    ema12 = ema(close, 12)

    macd_array = [None for x in range(len(ema26))]

    for x in range(len(ema26)):
        macd_array[x] = round(ema12[x] - ema26[x], 2)

    macd_signal_array = ema(macd_array, 9)
    macd_signal_array.insert(0, 0)

    macd_histogram_array = [None for x in range(len(macd_array))]

    for x in range(len(macd_array)):
        macd_histogram_array[x] = round(
            macd_array[x] - macd_signal_array[x], 2)

    return macd_array, macd_signal_array, macd_histogram_array
