def falseposition(func: callable, a: float, b: float, tol: float = 1.e-6, max_iter: int = 100) -> float:
    """
    Finds the root of a function using the false position method.

    Parameters:
        func: The function whose root is to be found.
        a: The lower bound of the interval.
        b: The upper bound of the interval.
        tol: The tolerance of the method.
        max_iter: The maximum number of iterations.

    Returns:
        The root.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("The function must change sign over the interval.")
    for i in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        if abs(func(c)) < tol or abs(b - a) < tol:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c


def f(x: float) -> float:
    return x ** 2 - 2


if __name__ == "__main__":
    print(falseposition(f, 0, 2))
