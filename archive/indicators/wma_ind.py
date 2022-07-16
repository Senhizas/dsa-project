def wma(source: list, length: int = 10):
    weighted_array = []
    wma_array = []

    for x in reversed(range(length)):
        weighted_array.append(x + 1)

    for x in range(len(source) + 1):
        if x >= length:
            sample_array = source[x-length:x][::-1]
            element_wise_multiplication = [
                a * b for a, b in zip(sample_array, weighted_array)]
            result = sum(element_wise_multiplication) / sum(weighted_array)
            wma_array.append(round(result, 2))

    return wma_array
