def atr(high, low, close, length):
    tr_array = []
    atr_array = []

    for x in range(len(close)):
        if x == 0:
            tr_array.append(round(high[x] - low[x], 2))
        elif x > 0:
            tr_array.append(max([round(high[x] - low[x], 2), round(abs(high[x] - close[x-1]), 2), round(abs(low[x] - close[x-1]), 2)]))

        if x == length:
            print(len(tr_array[x-length:x]))
            atr_array.append(round(sum(tr_array[x-length:x]) / length, 2))

        elif x > length:
            _atr = ((atr_array[-1] * (length - 1)) + tr_array[-1]) / length
            atr_array.append(round(_atr, 2))

    return atr_array