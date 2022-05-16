import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

start, end = np.array(list(map(int, input("Enter range: ").split())))
precision = float(input("Precision: "))
iterations = int(input("Iterations: "))
xplot = np.linspace(start, end, num=int((end-start)/precision))
eqn = input("y = ")
y = lambda x: eval(eqn)
yplot = y(xplot)
a, b = start, end
root = end+1
roots =[]
for i in range(start, end+1):
    if y(i) == 0:
        root = i
        break
    if y(i+1) == 0:
        root = i+1
        break
    if y(i)*y(i+1)<0:
        a = i
        b = i+1
        for _ in range(iterations):
            root = (a+b)/2
            roots.append(root)
            if y(root) == 0:
                break
            if y(a)*y(root)<0:
                b = root
                root = (a+root)/2
            elif y(b)*y(root)<0:
                a = root
                root = (b+root)/2
        break
print(roots)
plt.grid(True, which='both')
plt.plot(xplot, yplot)
yroot = y(root)
plt.plot(root, yroot, marker='o', color='red')
plt.show()

