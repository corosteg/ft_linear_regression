import sys
# import matplotlib.pyplot as plt
# import numpy as np

Alpha = 0.0000000001

def open_and_read_file(file):
    try:
        fd = open(file, "r")
    except:
        perror("ft_linear_regression a file with read permission in argument", 1)
    
    return fd.read()

def cost_function(t_0, t_1, x, y):
    result = 0

    for x_value, y_value in zip(x, y):
        result = result + (((t_0 + t_1 * x_value) - y_value)**2)

    print('result => ', result / (2 * len(x)))
    return result / (2 * len(x))

def gradient_descent(t_0, t_1, x, y):
    t_0_tmp = 0
    t_1_tmp = 0

    for x_value, y_value in zip(x, y):
        t_0_tmp = t_0_tmp + ((t_0 + t_1 * x_value) - y_value)
        t_1_tmp = t_1_tmp + (((t_0 + t_1 * x_value) - y_value)) * x_value

    t_0 = t_0 - Alpha * (t_0_tmp / len(x))
    t_1 = t_1 - Alpha * (t_1_tmp / len(y))

    return (t_0, t_1)


def normalizer(arr):
    arr_sum = 0
    arr_max = arr[0]
    arr_min = arr[0]

    for value in arr:
        arr_sum = arr_sum + value
        
        if arr_max < value:
            arr_max = value
        
        if arr_min > value:
            arr_min = value

    average = arr_sum / len(arr)
    s = arr_max - arr_min

    for i in range(len(arr)):
        arr[i] = (arr[i] - average) / s
    return (arr)


if __name__ == "__main__":
    data = open_and_read_file(sys.argv[1])
    data = data.split('\n')
    x = []
    y = []
    data.pop(0)
    for value in data:
        tmp = value.split(',')
        try:
            x.append(int(tmp[0], 10))
            y.append(int(tmp[1], 10))
        except:
            pass

    # x = [1, 2, 3, 4, 5]
    # y = [1, 2, 3, 8, 9]

    x_normalized = normalizer(x[:])
    y_normalized = normalizer(y[:])

    # print(x_normalized)
    # print(y_normalized)
    # print(x)
    # print(y)

    t_0 = 0
    t_1 = 0
    old_t_0 = None
    old_t_1 = None

    while True:
        old_t_0 = t_0
        old_t_1 = t_1
        t_0, t_1 = gradient_descent(t_0, t_1, x_normalized, y)
        
        finish_cost = ((cost_function(old_t_0, old_t_1, x_normalized, y) - cost_function(t_0, t_1, x_normalized, y))**2) / 2
        print ('finish_cost ===> {},   t_0 ===> {},     t_1 ===> {}'.format(finish_cost, t_0, t_1))
        if (finish_cost < 0.001):
            break
    


    ypred = []
    for tmp in x:
        ypred.append((t_0 + t_1 * -tmp) * -1)

    # print('t_0 ==> ', t_0)
    # print('t_1 ==> ', t_1)
    # print('5 ===> ', t_0 + t_1 * 20000)
    plt.scatter(x, y)
    plt.plot(x, ypred)

    plt.xlabel('Mile age (in km)')
    plt.ylabel('Price (in euro)')

    plt.title("Linear Regression")
    plt.show()