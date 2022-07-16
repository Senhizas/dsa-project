def sma(source: list, length: int = 10):
    sma_array = []
    
    for x in range(len(source)):
        if x >= length:
            sma_array.append(sum(source[x-length:x]) / length)

    return sma_array
