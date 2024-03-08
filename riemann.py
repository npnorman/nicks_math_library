#Riemann Sums
#Nicholas Norman
#8 March 2024

import nicks_handy_funcs as nhf
import math

def getInput():
    #take input (menu &eval()) --> a, b, n

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
6) y=sin(x)
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
    elif(inp == "6"):
        math.sin
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

def lRiemann(a, b, n, func, *args):
    #L-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(0, n):
        riemann += func(a+(i*dx), *args)

    return dx * riemann

def rRiemann(a, b, n, func, *args):
    #R-riemann
    dx = calculateDX(a, b, n)
    riemann = 0
    
    #add up sum
    for i in range(1, n+1):
        riemann += func(a+(i*dx), *args)

    return dx * riemann

#M-riemann
#T-riemann
#S-riemann

if __name__ == "__main__":

    #test input
    [func, a, b, n] = getInput()

    #evaluate using all methods
    print("function:",func.__name__, "(x), from {} to {}".format(a, b))
    print("Left-Hand Riemann: ",lRiemann(a, b, n, func))
    print("Right-Hand Riemann: ",rRiemann(a, b, n, func))
    
    #find closest solution
