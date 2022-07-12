def sma(close, length):
    sma_array = []
    for x in range(len(close)):
        if x >= length:
            sma_array.append(sum(close[x-length:x]) / length)

    return sma_array
