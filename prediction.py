#!/usr/local/bin/python3.6

if __name__ == "__main__":
    try:
        fd = open("./values", "r")
        data = fd.read().split("\n")
        theta_0 = float(data[0])
        theta_1 = float(data[1])
    except:
        theta_0 = 0
        theta_1 = 0
    
    x = input("Enter the KM of your car: ")
    x = int(x)
    print("\nHis cost are: ", x * theta_1 + theta_0)