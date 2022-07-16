def rma(source: list, length: int = 10):
    rma_array = []
    alpha = 1 / length

    for x in range(len(source)):

        if x == length:
            rma_array.append(sum(source[x-length:x]) / length)

        elif x >= length:
            rma_array.append(alpha * source[x] + (1 - alpha) * rma_array[-1])

    return rma_array
