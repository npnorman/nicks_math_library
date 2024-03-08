#Standard Math Functions in python
#Nicholas Norman
#7 March 2023

#This is a library of math functions to use in other math libraries.

import math

#test function
def __testFunc__(func, a, b, *args):
    print(func.__name__)
    for i in range(a, b+1):
        print("x={}, y={}".format(i, func(i, *args)))
    print("")

#standard functions
def y(x):
    #y=x
    return x

def x_sq(x):
    #y=x^2
    return x**2

def x_cb(x):
    #y=x^3
    return x**3

def inv_x(x):
    #y=1/x
    return 1/x

def exp_e(x):
    #y=e^x
    return math.e**x

def exp(x, base):
    #y=base^x
    return base**x

def log_b(x, b):
    #y=log base (x)
    return math.log(x, b)

def ln(x):
    #y=ln(x)
    return math.log(x)

#if used as main
if __name__ == "__main__":
    #test of functions
    __testFunc__(y, -2, 2)
    __testFunc__(x_sq, -2, 2)
    __testFunc__(x_cb, -2, 2)
    __testFunc__(inv_x, 1, 4)
    __testFunc__(exp_e, -2, 2)
    __testFunc__(exp, 0, 5, 2)
    __testFunc__(log_b, 1, 5, 10)
    __testFunc__(ln, 1, 5)


    dummy = input()
