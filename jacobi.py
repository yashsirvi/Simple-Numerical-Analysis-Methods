import numpy as np
import matplotlib.pyplot as plt

n, m = map(int, input("n, m: ").split())
iterations = int(input("Number of iterations: "))
print("Rows of Coefficient Matrix:")
array = np.array([input().strip().split() for _ in range(n)], int)
print("Answers to equations: ")
b = np.array([input().strip().split() for _ in range(n)], int)
print("Initial Guess: ")
x = np.array([input().strip().split() for _ in range(n)], int)
D = np.diag(np.diag(array))
L = np.tril(array)-D
U = np.triu(array)-D
invD = np.linalg.inv(D)
G = -(invD @ (L+U))
H = invD @ b
residue =[]
iter = []
for i in range(iterations):
    x = G @ x + H
    r = array@x -b
    normr = np.linalg.norm(r, ord="fro")
    residue.append(normr)
    iter.append(i+1)
    if normr < 1e-10:
        break
plt.style.use('fivethirtyeight')
plt.plot(iter, residue)
plt.show()
print(x)
