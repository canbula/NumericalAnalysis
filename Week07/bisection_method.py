import math


def bisection(f, a, b, tol):
    if a > b:
        raise ValueError("b must be larger than a")
    i = 0
    while True:
        if i > 1.0e6:
            raise ValueError("Could not find the solution with the desired accuracy")
        i += 1
        fa = f(a)
        fb = f(b)
        if fa * fb > 0:
            raise ValueError("This interval does not contain a root")
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol or abs(b - a) < tol:
            return c
        else:
            if fa * fc < 0:
                b = c
            else:
                a = c
        print(f"i={i:6d} a={a:.7f} | b={b:.7f} | c={c:.7f}")


def f(x):
    return math.sin(x) / x


if __name__ == "__main__":
    a_ = 1
    b_ = 4
    tol_ = 1.0e-6
    try:
        root = bisection(f, a_, b_, tol_)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Root: {root}")
    finally:
        print("End")
