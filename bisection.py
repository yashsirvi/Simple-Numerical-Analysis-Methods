import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, pi
from matplotlib.animation import FuncAnimation, PillowWriter

iterations = int(input("Iterations: "))
start, end = np.array(list(map(int, input("Enter domain of x: ").split())))
precision = 0.001
xplot = np.linspace(start, end, num=int((end - start) / precision))
eqn = input("y = ")
y = lambda x: eval(eqn)
yplot = y(xplot)
a, b = start, end
As = [a]
Bs = [b]
root = end + 1
roots = [(a + b) / 2]
for i in range(start, end + 1):
    if y(i) == 0:
        root = i
        roots.append(root)
        break
    if y(i + 1) == 0:
        root = i + 1
        roots.append(root)
        break
    if y(i) * y(i + 1) < 0:
        a = i
        b = i + 1
        As.append(a)
        Bs.append(b)
        for _ in range(iterations):
            root = (a + b) / 2
            roots.append(root)
            if y(root) == 0:
                roots.append(root)
                break
            if y(a) * y(root) < 0:
                b = root
                root = (a + root) / 2
                As.append(a)
                Bs.append(b)
            elif y(b) * y(root) < 0:
                a = root
                root = (b + root) / 2
                As.append(a)
                Bs.append(b)
        break

As_y = list(map(y, As))
Bs_y = list(map(y, Bs))
root_y = list(map(y, roots))

for i in range(1, len(roots)):
    print(f"Iteration {i}: {roots[i]}")
plt.style.use("fivethirtyeight")
fig = plt.figure()
plt.grid(True, which="both", zorder=1)
plt.plot(xplot, yplot, zorder=2)
(a_points,) = plt.plot([], [], "o", color="blue", zorder=3, ms=10)
(b_points,) = plt.plot([], [], "o", color="green", zorder=4, ms=10)
(root_points,) = plt.plot([], [], "o", color="red", zorder=5, ms=10)


def animatePoints(i):
    a_points.set_data(As[i : i + 1], As_y[i : i + 1])
    b_points.set_data(Bs[i : i + 1], Bs_y[i : i + 1])
    root_points.set_data(roots[i : i + 1], root_y[i : i + 1])
    return a_points, b_points, root_points


ani = FuncAnimation(
    fig, animatePoints, frames=iterations, interval=500, blit=True, repeat=False
)


plt.show()
# ani.save("gifs/bisection.gif", dpi=300, writer=PillowWriter(fps=2))
