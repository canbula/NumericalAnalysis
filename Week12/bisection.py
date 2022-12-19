import numpy as np


def bisection(func, a, b, tolerance=1e-5):
    fa = func(a)
    fb = func(b)
    if np.sign(fa) == np.sign(fb):
        raise ValueError(f"f(a) and f(b) must have opposite signs")
    m = (a + b)/2
    fm = func(m)
    if np.abs(func(m)) < tolerance:
        return m
    if np.sign(fa) == np.sign(fm):
        return bisection(func, m, b, tolerance)
    if np.sign(fb) == np.sign(fm):
        return bisection(func, a, m, tolerance)


def f(x):
    return x**2 - 2


if __name__ == '__main__':
    root = bisection(f, 0, 10)
    print('root =', root)
    print('f(root) =', f(root))
