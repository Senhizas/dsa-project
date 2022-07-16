def vwap(high: list, low: list, close: list, volume: list, length: int = 14):
    tpxv_array = []
    vwap_array = []

    for x in range(len(volume) + 1):
        if x < len(volume):
            tp = (high[x] + low[x] + close[x]) / 3
            tpxv = tp * volume[x]
            tpxv_array.append(tpxv)

        if x >= length:
            vwap_array.append(
                sum(tpxv_array[x-length:x]) / sum(volume[x-length:x]))

    return vwap_array
