# ! /usr/local/bin/python3.6

import sys
import matplotlib.pyplot as plt

ALPHA = 0.01

def open_and_read_file(argv):
    if len(argv) != 2:
        print("train:")
        print("Usage: train <data.csv>")
        sys.exit(1)

    try:
        fd = open(argv[1], "r")
    except:
        print('ft_linear_regression a file with read permission in argument')
        sys.exit(1)

    return fd.read()

def stock_data(data):
    data = data.split('\n')
    data.pop(0)
    x = []
    y = []

    for value in data:
        tmp = value.split(',')
        try:
            x.append(int(tmp[0], 10))
            y.append(int(tmp[1], 10))
        except:
            pass

    return (x, y)

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

    t_0 = t_0 - ALPHA * (t_0_tmp / len(x))
    t_1 = t_1 - ALPHA * (t_1_tmp / len(y))

    return (t_0, t_1)

def linear_regression(x, y):
    theta_0 = 0
    theta_1 = 0
    old_theta_0 = None
    old_theta_1 = None

    while old_theta_0 == None or cost_function(old_theta_0, old_theta_1, x, y) - cost_function(theta_0, theta_1, x, y) > 0.000000001:
        old_theta_0 = theta_0
        old_theta_1 = theta_1
        theta_0, theta_1 = gradient_descent(theta_0, theta_1, x, y)
    
    return (theta_0, theta_1)

if __name__ == "__main__":
    data = open_and_read_file(sys.argv)
    (x, y) = stock_data(data)
    x_copy = x[:]
    y_copy = y[:]
    x = normalizer(x[:])
    y = normalizer(y[:])


    # x = [1, 2, 3, 4, 5] # for tests
    # y = [1, 2, 3, 4, 5] # for tests

    (theta_0, theta_1) = linear_regression(x, y)
    # print(theta_0, theta_1)

    ypred = []
    for value in x:
        ypred.append(theta_0 + theta_1 * value)

    arr_sum = 0
    arr_max = ypred[0]
    arr_min = ypred[0]
    for value in y_copy:
        arr_sum = arr_sum + value
        
        if arr_max < value:
            arr_max = value
        
        if arr_min > value:
            arr_min = value

    average = arr_sum / len(ypred)
    s = arr_max - arr_min
   
    print((x[0] * theta_1 + theta_0) * s + average)

    y_finalpred = []
    for value in ypred:
        y_finalpred.append(value * s + average)

    print(y_finalpred)

    # theta_1 = (y_finalpred[1] - y_finalpred[0]) / (x_copy[1] - x_copy[0])
    # theta_0 = y_finalpred[0] - x_copy[0] * theta_1

    print(theta_0, theta_1)

    plt.scatter(x, y)
    plt.plot(x, ypred)

    plt.xlabel('Mile age (in km)')
    plt.ylabel('Price (in euro)')

    plt.title("Linear Regression")
    plt.show()

    # ypred = []
    # for tmp in x:
    #     ypred.append((theta_0 + theta_1 * tmp))

    # arr_sum = 0
    # arr_max = ypred[0]
    # arr_min = ypred[0]
    # for value in y_copy:
    #     arr_sum = arr_sum + value
        
    #     if arr_max < value:
    #         arr_max = value
        
    #     if arr_min > value:
    #         arr_min = value

    # average = arr_sum / len(ypred)
    # s = arr_max - arr_min

    # print(theta_0)
    # print(theta_1)
    # y_finalpred = []
    # for value in ypred:
    #     y_finalpred.append(value * s + arr_min)
    
    # print(y_finalpred)
    # print(ypred)
    # plt.scatter(x_copy, y_copy)
    # plt.plot(x_copy, y_finalpred)

    # plt.xlabel('Mile age (in km)')
    # plt.ylabel('Price (in euro)')

    # plt.title("Linear Regression")
    # plt.show()

    # print(theta_0, theta_1)
