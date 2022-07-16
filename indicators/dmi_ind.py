def rma(source: list, length: int = 10):
    rma_array = []
    alpha = 1 / length

    for x in range(len(source)):
        
        if x == length:
            rma_array.append(round(sum(source[x-length:x]) / length, 4))
        
        elif x >= length:
            rma_array.append(round(alpha * source[x] + (1 - alpha) * rma_array[-1], 4))

    return rma_array

def dmi(high: list, low: list, close: list, length: int = 14):
    tr_array = []
    plus_dm_array = []
    minus_dm_array = []
    _adx = []
    plus_di_array = []
    minus_di_array = []
    adx_array = []

    for x in range(len(high)):
        if x == 0:
            tr_array.append(round(high[x] - low[x], 4))

        elif x > 0:
            tr_array.append(max([round(high[x] - low[x], 2), round(abs(high[x] - close[x-1]), 2), round(abs(low[x] - close[x-1]), 4)]))
            up = high[x] - high[x-1]
            down = (low[x] - low[x-1]) * -1

            if up > down and up > 0:
                plus_dm = up
            else:
                plus_dm = 0

            if down > up and down > 0:
                minus_dm = down
            else:
                minus_dm = 0

            plus_dm_array.append(plus_dm)
            minus_dm_array.append(minus_dm)

            if len(tr_array) >= length:
                tr_rma = rma(tr_array, length)

                if tr_rma:
                    try:
                        plus_di = (100 * rma(plus_dm_array, length)[-1] / tr_rma[-1])
                        minus_di = (100 * rma(minus_dm_array, length)[-1] / tr_rma[-1])
                        plus_di_array.append(round(plus_di, 4))
                        minus_di_array.append(round(minus_di, 4))
                        addition = plus_di + minus_di

                        if addition == 0:
                            addition = 1
                            
                        _adx.append(abs(plus_di - minus_di) / addition)
                        adx_array.append(round(100 * rma(_adx, length)[-1], 4))
                    except:
                        pass

    return adx_array, plus_di_array, minus_di_array
