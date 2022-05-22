from numpy import sin, cos, tan, pi

iterations = int(input("Iterations: "))
eqn = input("g(x) = ")
g = eval(f"lambda x: {eqn}")
a, b = list(map(float, input("Enter Domain of x: ").split()))
x_i = float(input("x_0 = "))
roots = [x_i]

for i in range(iterations):
    root = g(roots[len(roots) - 1])
    if not (a <= root <= b):
        print("Root does not converge.")
        break
    roots.append(root)
    print(f"x_{i+1}: {roots[i+1]}")
