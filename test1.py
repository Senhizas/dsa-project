import talib as ta

def multiplication_table(table_limit, multiple):
    array = [None for i in range(table_limit)]

    for x in range(len(array) + 1):
        product = multiple * x
        array[x-1] = product
    return array


def moving_average(data, length):
    ma = [None for i in range(len(data) - length + 1)]

    for x in range(len(data) - length + 1):
        window = data[x:x+length]
        ma[x] = round(sum(window) / length, 2)
    return ma

def standard_deviation(data):
    mean = sum(data) / len(data)
    sd = [None for i in range(len(data))]
    
    for x in range(len(data)):
        sd[x] = (data[x] - mean) ** 2

    std = (sum(sd) / len(data)) ** (1 / 2)
    return std

a = 19030.6
b = 19049.78
print(max([a, b]))