import numpy as np


def finite_difference(func, x, h=1e-5):
    return (func(x + h) - func(x - h))/(2*h)


def newton_raphson(func, x0, tolerance=1e-5):
    x = x0
    while np.abs(func(x)) > tolerance:
        x = x - func(x)/finite_difference(func, x)
    return x


def f(x):
    return x**2 - 2


def main():
    root = newton_raphson(f, 3)
    print('root =', root)
    print('f(root) =', f(root))


if __name__ == '__main__':
    main()
