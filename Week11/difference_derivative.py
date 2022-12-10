import math


def f(x: float) -> float:
    return math.sin(x)


def f_prime(x: float) -> float:
    return math.cos(x)


def first_forward(func: callable, x: float, h: float) -> float:
    return (func(x + h) - func(x)) / h


def first_backward(func: callable, x: float, h: float) -> float:
    return (func(x) - func(x - h)) / h


def first_central(func: callable, x: float, h: float) -> float:
    return (func(x + (h / 2)) - func(x - (h / 2))) / h


def three_point_forward(func: callable, x: float, h: float) -> float:
    return (4 * func(x + (h / 2)) - 3 * func(x) - func(x + h)) / h


def main():
    for i in range(20):
        h = 10 ** (-1 * i)
        x = 1.0
        print(f"{h:8.2e} {f_prime(x):.6f} "
              f"{first_forward(f, x, h):.6f} ({abs(f_prime(x) - first_forward(f, x, h)):8.2e}) "
              f"{first_backward(f, x, h):.6f} ({abs(f_prime(x) - first_backward(f, x, h)):8.2e}) "
              f"{first_central(f, x, h):.6f} ({abs(f_prime(x) - first_central(f, x, h)):8.2e}) "
              f"{three_point_forward(f, x, h):.6f} ({abs(f_prime(x) - three_point_forward(f, x, h)):8.2e}) ")


if __name__ == "__main__":
    main()
