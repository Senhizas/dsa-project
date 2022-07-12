def rsi(close, length):
    change = [0 for x in range(len(close) - 1)]
    gain = [0 for x in range(len(close) - 1)]
    loss = [0 for x in range(len(close) - 1)]
    average_gain = []
    average_loss = []
    rsi_array = []

    for x in range(len(close) - 1):
        if x > 0:
            change[x] = round(close[x+1] - close[x], 2)
            if change[x] > 0:
                gain[x] = change[x]
                loss[x] = 0
            elif change[x] < 0:
                loss[x] = abs(change[x])
                gain[x] = 0

        if x == length:
            _gain = sum(gain[:length+1]) / length
            _loss = sum(loss[:length+1]) / length
            average_gain.append(round(_gain, 2))
            average_loss.append(round(_loss, 2))
            rs = average_gain[-1] / average_loss[-1]
            rsi_array.append(round(100 - (100 / (1 + rs)), 2))

        if x > length:
            _gain = ((average_gain[-1] * (length - 1)) + gain[x]) / length
            _loss = ((average_loss[-1] * (length - 1)) + loss[x]) / length
            average_gain.append(round(_gain, 2))
            average_loss.append(round(_loss, 2))
            rs = average_gain[-1] / average_loss[-1]
            rsi_array.append(round(100 - (100 / (1 + rs)), 2))

    return rsi_array
