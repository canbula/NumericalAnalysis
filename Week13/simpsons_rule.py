import math


def f(x: float) -> float:
    return x**2 - 2


def f_int(x: float) -> float:
    return x**3 / 3 - 2 * x


def simpsons_rule(func: callable, a: float, b: float, n: int) -> float:
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n, 2):
        s += 4 * func(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * func(a + i * h)
    return h / 3 * s


def main():
    for k in range(1, 12):
        n = 2 ** k
        a = 0.0
        b = 1.0
        result_numerical = simpsons_rule(f, a, b, n)
        result_analytical = f_int(b) - f_int(a)
        print(f"{n:8d} {result_analytical:.6f} {result_numerical:.6f} "
              f"({abs(result_analytical - result_numerical):8.2e})")


if __name__ == "__main__":
    main()
