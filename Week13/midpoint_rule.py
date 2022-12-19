def f(x: float) -> float:
    return x**2 - 2


def f_int(x: float) -> float:
    return x**3 / 3 - 2 * x


def midpoint_rule(func: callable, a: float, b: float, n: int) -> float:
    h = (b - a) / n
    s = 0.0
    for i in range(n):
        s += func(a + (i + 0.5) * h)
    return h * s


def main():
    for k in range(1, 12):
        n = 2 ** k
        a = 0.0
        b = 1.0
        result_numerical = midpoint_rule(f, a, b, n)
        result_analytical = f_int(b) - f_int(a)
        print(f"{n:8d} {result_analytical:.6f} {result_numerical:.6f} "
              f"({abs(result_analytical - result_numerical):8.2e})")


if __name__ == "__main__":
    main()
