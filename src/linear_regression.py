
ALPHA = 0.01

def cost_function(t_0, t_1, x, y):
    result = 0

    for x_value, y_value in zip(x, y):
        result = result + (((t_0 + t_1 * x_value) - y_value)**2)

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
    