def bbands(close, length, multiplier):
    sd = []
    for x in range(len(close) + 1):
        if x >= length:
            middle_band = round(sum(close[x-length:x]) / length, 6)
            sample_price = close[x-length:x]

            for y in range(length):
                sd.append(round((sample_price[y] - middle_band) ** 2, 6))

            st_dev = round((sum(sd) / length) ** (1/2), 6)
            sd.clear()
            upper_band = middle_band + (st_dev * multiplier)
            lower_band = middle_band - (st_dev * multiplier)

    return upper_band, middle_band, lower_band
