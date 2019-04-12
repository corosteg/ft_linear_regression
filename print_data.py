import sys
import matplotlib.pyplot as plt
import numpy as np

def open_and_read_file(file):
    try:
        fd = open(file, "r")
    except:
        perror("n-puzzle need a file with read permission in argument", 1)
    
    return fd.read()

if __name__ == "__main__":
    data = open_and_read_file(sys.argv[1])
    data = data.split('\n')
    i = 1
    x = []
    y = []
    data_len = len(data)
    while (i < data_len - 1):
        tmp = data[i].split(',')
        x.append(tmp[0])
        y.append(tmp[1])
        i += 1
    # print (x, y)
    plt.axis([20000, 250000, 3500, 8500])
    plt.scatter(x, y)
    plt.grid(True)
    plt.xlabel('Mile age (in km)')
    plt.ylabel('Price (in euro)')

    plt.title("Data")
    plt.show()