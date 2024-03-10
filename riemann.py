#Riemann Sums
#Nicholas Norman
#8 March 2024

import nicks_handy_funcs as nhf
import math

def getInput():
    #take input (menu &eval()) --> a, b, n
    #validate all inputs (a,b,n)
    
    #function holder
    func = None

    menu = """
Please select eqn to approximate
0) y=x
1) y=x^2
2) y=x^3
3) y=1/x
4) y=e^x
5) y=ln(x)
"""
    
    print(menu)
    
    inp = input("eqn: ")

    if(inp == "0"):
        func = nhf.y
    elif(inp == "1"):
        func = nhf.x_sq
    elif(inp == "2"):
        func = nhf.x_cb
    elif(inp == "3"):
        func = nhf.inv_x
    elif(inp == "4"):
        func = nhf.exp_e
    elif(inp == "5"):
        func = nhf.ln
    else:
        print("no function assigned, defaulted to y=x")
        func = nhf.y

    print("input bounds from a to b")
    a = float(input("a: "))
    b = float(input("b: "))
    print("input number of rectangles; n")
    n = int(input("n: "))

    return [func, a, b, n]


def calculateDX(a, b, n):
    #calculate dx
    dx = (b-a)/n

    return dx

def leftHandRiemann(a, b, n, func, *args):
    #L-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(0, n):
        riemann += func(a+(i*dx), *args)

    return dx * riemann

def rightHandRiemann(a, b, n, func, *args):
    #R-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(1, n+1):
        riemann += func(a+(i*dx), *args)

    return dx * riemann

def midpointRiemann(a, b, n, func, *args):
    #M-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(1, n+1):
        param = (a+(i*dx)) + (a+((i-1)*dx))
        param *= 1/2
        riemann += func(param, *args)

    return dx * riemann

def trapezoidalRiemann(a, b, n, func, *args):
    #T-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(0, n+1):
        if (i != 0 and i != n):
            riemann += 2 * func(a+(i*dx), *args)
        else:
            riemann += func(a+(i*dx), *args)

    return dx/2 * riemann

def simpsonsRiemann(a, b, n, func, *args):
    #S-riemann
    if(n % 2 != 0):
        n = n-1
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(0, n+1):
        if (i == 0 or i == n):
            riemann += func(a+(i*dx), *args)
        elif (i % 2 == 0):
            riemann += 2 * func(a+(i*dx), *args)
        elif (i % 2 != 0):
            riemann += 4 * func(a+(i*dx), *args)

    return dx/3 * riemann
    

if __name__ == "__main__":

    #test input
    [func, a, b, n] = getInput()

    #evaluate using all methods
    print("\nfunction:",func.__name__, "(x), from {} to {}".format(a, b), end="\n\n")
    
    print("Left-Hand:   {:+.4f} {:>5}: {}".format(leftHandRiemann(a, b, n, func), 'n', n))
    print("Right-Hand:  {:+.4f} {:>5}: {}".format(rightHandRiemann(a, b, n, func), 'n', n))
    print("Midpoint:    {:+.4f} {:>5}: {}".format(midpointRiemann(a, b, n, func), 'n', n))
    print("Trapezoidal: {:+.4f} {:>5}: {}".format(trapezoidalRiemann(a, b, n, func), 'n', n))
    print("Simpsons:    {:+.4f} {:>5}: {}".format(simpsonsRiemann(a, b, n, func), 'n', n - (0 if n % 2 == 0 else 1)))

    dummy = input()
    
