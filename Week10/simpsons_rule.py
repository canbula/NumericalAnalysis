def f(x: float) -> float:
    return x**2 - 2


def f_int(x: float) -> float:
    return x**3 / 3 - 2 * x


def simpsons_rule(func: callable, a: float, b: float, n: int) -> float:
    """
    Simpson's rule using n points
    :param func: function to integrate
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of points
    :return: integral
    """
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n, 2):
        s += 4 * func(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * func(a + i * h)
    return h / 3 * s


def main():
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
        a = 0.0
        b = 1.0
        print(f"{n:8d} "
              f"{simpsons_rule(f, a, b, n):.6f} "
              f"({abs(f_int(b) - f_int(a) - simpsons_rule(f, a, b, n)):8.2e})")


if __name__ == '__main__':
    main()
