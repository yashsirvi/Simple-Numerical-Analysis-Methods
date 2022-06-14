import numpy as np
from sympy import *
from scipy import integrate as sci_integrate

x = Symbol("x")
print("Trapezoidal rule (t) or Simpson's rule (s)?")
rule = input("t or s: ")
print("f(x) : ", end="")
func = input()
f = eval(func)
print("a, b : ", end="")
a, b = list(map(float, input().split()))
print("Number of intervals : ", end="")
n = int(input())
print("Also calculate exact value of integral (y/n): ", end="")
flagexact = input()
exact_integral = 0
if flagexact == "y":
    exact_integral = integrate(f, (x, a, b)).evalf()
    print(f"Exact value of integral: {exact_integral}")

f = lambdify(x, f)
print()
if rule == "t":
    for i in range(2, n + 1):
        print(f"For {i} subintervals: ")
        y = f(np.linspace(a, b, i + 1))
        trapz = sci_integrate.trapezoid(y, dx=(b - a) / i)
        print(f"Value : {trapz}")
        print(f"h = {(b - a) / i}")
        if flagexact == "y":
            print(f"Error: {abs(trapz - exact_integral)}")
        print()
elif rule == "s":
    for i in range(2, n + 1, 2):
        print(f"For {i} subintervals: ")
        y = f(np.linspace(a, b, i + 1))
        simpson = sci_integrate.simps(y, dx=(b - a) / i)
        print(f"Value : {simpson}")
        print(f"h = {(b - a) / i}")
        if flagexact == "y":
            print(f"Error: {abs(simpson - exact_integral)}")
        print()
