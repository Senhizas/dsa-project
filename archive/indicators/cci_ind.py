def cci(high: list, low: list, close: list, length: int = 20):
    tp_array = [None for x in range(len(close))]
    sma_array = []
    abs_values = []
    cci_array = []

    for x in range(len(close) + 1):
        if x < len(close):
            tp_array[x] = round((high[x] + low[x] + close[x]) / 3, 2)

        if x >= length:
            sma_array.append(round(sum(tp_array[x-length:x]) / length, 2))

            sample_tp_array = tp_array[x-length:x]
            for y in range(length):
                _ = abs(sample_tp_array[y] - sma_array[-1])
                abs_values.append(_)

            mean_deviation = round(sum(abs_values) / length, 2)
            abs_values.clear()

            cci_array.append(round((tp_array[x-1] - sma_array[-1]) / (0.015 * mean_deviation), 2))
    
    return cci_array
