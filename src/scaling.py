def calcul_deviation_average(arr):
    arr_sum = 0
    deviation = 0

    for value in arr:
        arr_sum = arr_sum + value

    average = arr_sum / len(arr)

    for value in arr:
        deviation = deviation + ((value - average) ** 2)

    deviation = deviation ** 0.5

    return average, deviation

def normalizer(arr):
    average, deviation = calcul_deviation_average(arr)

    for i in range(len(arr)):
        arr[i] = (arr[i] - average) / deviation
    
    return arr

def denormalizer(arr, y):
    average, deviation = calcul_deviation_average(y)

    result = []
    for value in arr:
        result.append(value * deviation + average)

    return result
