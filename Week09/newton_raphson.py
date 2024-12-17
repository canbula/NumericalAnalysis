def first_forward(f, x, h):
    return (f(x + h) - f(x)) / h


def fn(x):
    return x**2 - 2


def newton_raphson(f, x0, tol=1.0e-6, max_iter=100):
    x = x0
    prev_x = x
    for i in range(max_iter):
        fx = f(x)
        fprimex = first_forward(f, x, tol)
        x = x - fx / fprimex
        print(f"i={i} x={x:.6f} f(x)={fx:.6e}")
        if abs(fx) < tol or abs(prev_x - x) < tol:
            return x
        prev_x = x


if __name__ == "__main__":
    x0 = 100000.0
    print(newton_raphson(fn, x0))
