# ! /usr/local/bin/python3.6

import sys
import matplotlib.pyplot as plt
from src.linear_regression import linear_regression
from src.scaling import normalizer, denormalizer

def open_and_read_file(argv):
    if len(argv) != 2:
        print("train:")
        print("Usage: train <data.csv>")
        sys.exit(1)

    try:
        fd = open(argv[1], "r")
    except:
        print("ft_linear_regression a file with read permission in argument")
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

if __name__ == "__main__":
    data = open_and_read_file(sys.argv)
    (x, y) = stock_data(data)
    x_norm = normalizer(x[:])
    y_norm = normalizer(y[:])

    theta_0, theta_1 = linear_regression(x_norm, y_norm)

    ypred = []
    for value in x_norm:
        ypred.append(theta_0 + theta_1 * value)
    y_finalpred = []
    y_finalpred = denormalizer(ypred, y)

    theta_1 = (y_finalpred[1] - y_finalpred[0]) / (x[1] - x[0])
    theta_0 = y_finalpred[0] - x[0] * theta_1
    
    file = open("values", "w")
    file.write(str(theta_0))
    file.write("\n")
    file.write(str(theta_1))

    print_graph = input("Do you want to see graph of linear regression (y/n)? ")

    if print_graph == "y" or print_graph == "yes":
        plt.scatter(x, y)
        plt.plot(x, y_finalpred)

        plt.xlabel('Mile age (in km)')
        plt.ylabel('Price (in euro)')
        plt.title("Linear Regression")
        plt.show()
