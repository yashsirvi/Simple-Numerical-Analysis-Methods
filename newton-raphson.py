import numpy as np
import sympy as sp

x = sp.Symbol("x")
iterations = int(input("Iterations: "))
eqn = input("f(x) = ")
f = eval(eqn)
df = sp.diff(eval(eqn))
g = sp.lambdify(x, f / df)
a, b = list(map(float, input("Enter Domain of x: ").split()))
x_i = float(input("x_0 = "))
roots = [x_i]
root = x_i
for i in range(1, iterations + 1):
    root = root - g(root)
    roots.append(root)
    print(f"x_{i} = {root}")
