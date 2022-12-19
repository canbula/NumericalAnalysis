from midpoint_rule import midpoint_rule
from trapezoidal_rule import trapezoidal_rule
from simpsons_rule import simpsons_rule
import math
from scipy.integrate import quad


def f(x: float) -> float:
    return math.cos(x)


def f_int(x: float) -> float:
    return math.sin(x)


def main():
    for k in range(1, 12):
        n = 2 ** k
        a = 0.0
        b = 1.0
        result_analytical = f_int(b) - f_int(a)
        result_midpoint = midpoint_rule(f, a, b, n)
        result_trapezoidal = trapezoidal_rule(f, a, b, n)
        result_simpsons = simpsons_rule(f, a, b, n)
        result_quad = quad(f, a, b)[0]
        print(f"{n:8d} {result_analytical:.6f} "
              f"{result_midpoint:.6f} "
              f"({abs(result_analytical - result_midpoint):8.2e}) "
              f"{result_trapezoidal:.6f} "
              f"({abs(result_analytical - result_trapezoidal):8.2e}) "
              f"{result_simpsons:.6f} "
              f"({abs(result_analytical - result_simpsons):8.2e}) "
              f"{result_quad:.6f} "
              f"({abs(result_analytical - result_quad):8.2e})")


if __name__ == "__main__":
    main()
