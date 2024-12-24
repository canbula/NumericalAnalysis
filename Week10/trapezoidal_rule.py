def f(x: float) -> float:
    return x**2 - 2


def f_int(x: float) -> float:
    return x**3 / 3 - 2 * x


def trapezoidal_rule(func: callable, a: float, b: float, n: int) -> float:
    """
    Trapezoidal rule using n points
    :param func: function to integrate
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of points
    :return: integral
    """
    h = (b - a) / n
    s = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        s += func(a + i * h)
    return h * s


def main():
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
        a = 0.0
        b = 1.0
        print(f"{n:8d} "
              f"{trapezoidal_rule(f, a, b, n):.6f} "
              f"({abs(f_int(b) - f_int(a) - trapezoidal_rule(f, a, b, n)):8.2e})")


if __name__ == '__main__':
    main()
