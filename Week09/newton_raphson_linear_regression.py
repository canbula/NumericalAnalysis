import numpy as np
import matplotlib.pyplot as plt


def first_forward(f, x, h):
    return (f(x + h) - f(x)) / h


def mse(a, b, x, y):
    return np.mean((y - (a * x + b)) ** 2)


def newton_raphson(f, x0, tol=1.0e-6, max_iter=100000, patience=1000):
    x = x0
    fx = np.inf
    best_x = x
    for i in range(max_iter):
        x = x - f(x) / first_forward(f, x, 1.0e-6)
        print(f"i={i} x={x:.6f} f(x)={f(x):.6f}")
        if f(x) < fx:
            fx = f(x)
            best_x = x
        else:
            patience -= 1
            if patience < 0:
                break
        if abs(f(x)) < tol:
            return x
    return best_x


if __name__ == "__main__":
    np.random.seed(7)
    a0 = 2.0
    b0 = 1.0
    x = np.linspace(0, 10, 100)
    y = a0 * x + b0 + np.random.normal(0, 1, 100)

    a = np.linspace(0, 4, 100)
    b = np.linspace(-2, 4, 100)

    plt.plot(a, np.array([mse(a_val, b0, x, y) for a_val in a]), label="MSE(a, b0)")
    plt.plot(a, np.array([mse(a_val, 2.0, x, y) for a_val in a]), label="MSE(a, b0=2)")
    plt.plot(a, np.array([mse(a_val, 3.0, x, y) for a_val in a]), label="MSE(a, b0=3)")
    plt.plot(b, np.array([mse(a0, b_val, x, y) for b_val in b]), label="MSE(a0, b)")
    plt.legend()
    plt.show()

    mse_values = np.array([[mse(a_val, b_val, x, y) for b_val in b] for a_val in a])
    plt.contourf(a, b, mse_values, levels=20)
    plt.colorbar()
    plt.xlabel("a")
    plt.ylabel("b")
    plt.show()

    f = lambda a: mse(a, b0, x, y)
    a_optimal = newton_raphson(f, a0, patience=1000)
    f = lambda b: mse(a_optimal, b, x, y)
    b_optimal = newton_raphson(f, b0, patience=1000)
    print(f"Optimal a: {a_optimal}")
    print(f"Optimal b: {b_optimal}")
    print(f"Optimal MSE: {mse(a_optimal, b_optimal, x, y)}")
    plt.scatter(x, y)
    plt.plot(x, a_optimal * x + b_optimal, color="red")
    plt.show()
