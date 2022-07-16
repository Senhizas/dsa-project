def ema(source: list, length: int = 10):
    smoothing_constant = 2 / (length + 1)
    ema_array = []

    for x in range(len(source)):
        if x == 0:
            _sma = sum(source[:length]) / length

        if x == 1:
            _ema = (source[x] - _sma) * smoothing_constant + _sma
            ema_array.append(round(_ema, 2))
        
        if x > 1:
            _ema = (source[x] - ema_array[-1]) * smoothing_constant + ema_array[-1]
            ema_array.append(round(_ema, 2))
            
    return ema_array
