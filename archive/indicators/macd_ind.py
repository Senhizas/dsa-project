def ema(source: list, length: int = 10):
    smoothing_constant = 2 / (length + 1)
    ema_array = []

    for x in range(len(source)):
        if x == 0:
            _sma = sum(source[:length]) / length

        if x == 1:
            _ema = (source[x] - _sma) * smoothing_constant + _sma
            ema_array.append(round(_ema, 2))

        if x > 1:
            _ema = (source[x] - ema_array[-1]) * \
                smoothing_constant + ema_array[-1]
            ema_array.append(round(_ema, 2))

    return ema_array


def macd(source: list, fast_length: int = 12, slow_length: int = 26, signal_length: int = 9):
    ema12 = ema(source, fast_length)
    ema26 = ema(source, slow_length)

    macd_array = [None for x in range(len(ema26))]

    for x in range(len(ema26)):
        macd_array[x] = round(ema12[x] - ema26[x], 2)

    macd_signal_array = ema(macd_array, signal_length)
    macd_signal_array.insert(0, 0)

    macd_histogram_array = [None for x in range(len(macd_array))]

    for x in range(len(macd_array)):
        macd_histogram_array[x] = round(
            macd_array[x] - macd_signal_array[x], 2)

    return macd_array, macd_signal_array, macd_histogram_array
