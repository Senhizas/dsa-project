def stoch(high, low, close, length, smooth_d):
    k = []
    d = []

    for x in range(len(high)):
        if x >= length:
            k.append(((close[x] - min(low[x-length:x])) /
                     (max(high[x-length:x]) - min(low[x-length:x]))) * 100)

    for x in range(len(k) + 1):
        if x >= smooth_d:
            print(len(k[x-3:x]))
            d.append(sum(k[x-3:x]) / 3)

    return k, d
