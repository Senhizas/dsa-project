def psar(high, low, close, start, inc, maximum):
    sar_array = []

    for x in range(1, len(close)):
        if x == 1:
            if close[x] > close[x-1]:
                is_below = True
                max_min = high[x]
                sar = low[x-1]
            else:
                is_below = False
                max_min = low[x]
                sar = high[x-1]
            acceleration = start

        sar = sar + acceleration * (max_min - sar)

        if is_below:
            if sar > low[x]:
                is_below = False
                sar = max(high[x], max_min)
                max_min = low[x]
                acceleration = start
        else:
            if sar < high[x]:
                is_below = True
                sar = min(low[x], max_min)
                max_min = high[x]
                acceleration = start

        if is_below:
            if high[x] > max_min:
                max_min = high[x]
                acceleration = min(acceleration + inc, maximum)
            sar = min(sar, low[x-1])
            if x > 1:
                sar = min(sar, low[x-2])

        else:
            if low[x] < max_min:
                max_min = low[x]
                acceleration = min(acceleration + inc, maximum)
            sar = max(sar, high[x-1])
            if x > 1:
                sar = max(sar, high[x-2])

        sar_array.append(round(sar, 2))

    return sar_array
