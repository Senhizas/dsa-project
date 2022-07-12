
def slope(source, length):
    x_values = []
    y_values = []
    xy_values = []
    xsq_values = []
    for x in range(length):
        x_values.append(x+1)
        y_values.append(source[x])
        xy_values.append(x_values[-1] * y_values[-1])
        xsq_values.append(x_values[-1] ** 2)

    _slope = ((length * sum(xy_values)) - (sum(x_values) * sum(y_values))
              ) / ((length * sum(xsq_values)) - (sum(x_values) ** 2)) * -1
    _average = sum(y_values) / length
    _intercept = (sum(y_values) - (_slope * sum(x_values))) / length

    return _slope, _average, _intercept


def dev(source, high, low, length, slope, average, intercept):
    upper_dev = 0
    lower_dev = 0
    stdDevAcc = 0
    dsxx = 0
    dsyy = 0
    dsxy = 0
    period = length - 1
    daY = intercept + slope * period / 2
    _intercept = intercept

    for x in range(period):
        _price = high[x] - _intercept

        if _price > upper_dev:
            upper_dev = _price

        _price = _intercept - low[x]

        if _price > lower_dev:
            lower_dev = _price

        _price = source[x]
        dxt = _price - average
        dyt = _intercept - daY
        _price -= _intercept
        stdDevAcc += _price * _price
        dsxx += dxt * dxt
        dsyy += dyt * dyt
        dsxy += dxt * dyt
        _intercept += slope

    if period == 0:
        stdDev = (stdDevAcc / 1) ** (1 / 2)
    else:
        stdDev = (stdDevAcc / period) ** (1 / 2)

    if dsxx == 0 or dsyy == 0:
        pearsonR = 0
    else:
        pearsonR = dsxy / ((dsxx * dsyy) ** (1 / 2)) * -1

    return stdDev, pearsonR, upper_dev, lower_dev

def lin_regression(close, length):
    s, a, i = slope(close, 100)
    startPrice = i + s * (100 - 1)
    endPrice = i
    std, pr, ud, ld = dev(close, 100, s, a, i)

    upperMultInput = 2.0
    lowerMultInput = 2.0
    upperStartPrice = startPrice + (upperMultInput * std)
    upperEndPrice = endPrice + (upperMultInput * std)
    lowerStartPrice = startPrice + (-lowerMultInput * std)
    lowerEndPrice = endPrice + (-lowerMultInput * std)
