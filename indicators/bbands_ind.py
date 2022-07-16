def bbands(source: list, length: int = 20, multiplier: int = 2):
    sd = []
    
    for x in range(len(source) + 1):
        if x >= length:
            middle_band = round(sum(source[x-length:x]) / length, 6)
            sample_price = source[x-length:x]

            for y in range(length):
                sd.append(round((sample_price[y] - middle_band) ** 2, 6))

            st_dev = round((sum(sd) / length) ** (1/2), 6)
            sd.clear()
            upper_band = middle_band + (st_dev * multiplier)
            lower_band = middle_band - (st_dev * multiplier)

    return upper_band, middle_band, lower_band
