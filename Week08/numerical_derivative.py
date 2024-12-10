import math
import random


def first_forward(f, x, h):
    return (f(x + h) - f(x)) / h


def fn(x):
    return math.sin(x)


if __name__ == "__main__":
    x = random.random() * math.pi
    for h in [1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5, 1.0e-6]:
        print(
            f"""
            x={x:.3f} 
            h={h:.1e}
            sin(x)={fn(x):.3f} 
            f'(x)={first_forward(fn, x, h)}
        """
        )
