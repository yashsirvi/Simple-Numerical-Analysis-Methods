import numpy as np
import matplotlib.pyplot as plt

n, m = map(int, input("n, m: ").split())
iterations = int(input("Number of iterations: "))
print("Rows of Coefficient Matrix:")
array = np.array([input().strip().split() for _ in range(n)], int)
print("Answers to equations: ")
b = np.array([input().strip().split() for _ in range(n)], int)
print("Initial Guess: ")
x = np.array([input().strip().split() for _ in range(n)], float)
D = np.diag(np.diag(array))
L = np.tril(array)-D
U = np.triu(array)-D
invDL = np.linalg.inv(D+L)
G = -(invDL @ U)
H = invDL @ b
residue =[]
iter = []
for i in range(iterations):
    x = G @ x + H
    r = array@x -b
    normr = np.linalg.norm(r, ord="fro")
    residue.append(normr)
    iter.append(i+1)
    print(f"Iteration {i+1}: x = {x[0][0]}\t y = {x[1][0]}\t z = {x[2][0]}")
    if normr < 1e-10:
        break
plt.style.use('fivethirtyeight')
plt.plot(iter, residue)
plt.show()
print(x)
