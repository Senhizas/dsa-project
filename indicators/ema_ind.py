def ema(close, length):
    smoothing_constant = 2 / (length + 1)
    ema_array = []

    for x in range(len(close)):
        if x == 0:
            _sma = sum(close[:length]) / length

        if x == 1:
            _ema = (close[x] - _sma) * smoothing_constant + _sma
            ema_array.append(round(_ema, 2))
        
        if x > 1:
            _ema = (close[x] - ema_array[-1]) * smoothing_constant + ema_array[-1]
            ema_array.append(round(_ema, 2))
            
    return ema_array
