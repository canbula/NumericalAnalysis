class SignError(Exception):
    """
    This class is used to raise an error when the function does not change sign over the interval.
    """
    pass

class MethodError(Exception):
    """
    This class is used to raise an error when the method is not 'bisection' or 'falseposition'.
    """
    pass

class IntervalError(Exception):
    """
    This class is used to raise an error when the lower bound is greater than the upper bound.
    """
    pass

class ToleranceError(Exception):
    """
    This class is used to raise an error when the tolerance is less than or equal to 0.
    """
    pass

class IterationError(Exception):
    """
    This class is used to raise an error when the maximum number of iterations is less than or equal to 0.
    """
    pass

class FunctionError(Exception):
    """
    This class is used to raise an error when the function cannot be parsed.
    """
    pass

class InputError(Exception):
    """
    This class is used to raise an error when the input cannot be parsed.
    """
    pass

class RootFinder:
    """
    This class is used to find the root of a function using the bisection or false position method.

    Attributes:
        func: The function whose root is to be found.
        a: The lower bound of the interval.
        b: The upper bound of the interval.
        tol: The tolerance of the method.
        max_iter: The maximum number of iterations.
        method: The method to be used to find the root.
    
    Methods:
        validate_input: Validates the input for the method.
        find_root: Finds the root of the function.
    """
    def __init__(self, func: callable, a: float, b: float, tol: float = 1.e-6, max_iter: int = 100, method: str = "bisection") -> None:
        """
        The constructor for the RootFinder class.

        Parameters:
            func: The function whose root is to be found.
            a: The lower bound of the interval.
            b: The upper bound of the interval.
            tol: The tolerance of the method.
            max_iter: The maximum number of iterations.
            method: The method to be used to find the root.
        """
        self.func: callable = func
        self.a: float = a
        self.b: float = b
        self.tol: float = tol
        self.max_iter: int = max_iter
        self.method: str = method
        if self.validate_input():
            self.root, self.error, self.iter, self.flag = self.find_root()
    
    def validate_input(self) -> bool:
        """
        Validates the input for the method.

        Returns:
            True if the input is valid, False otherwise.
        """
        if any([self.func, self.a, self.b, self.tol, self.max_iter, self.method]) is None:
            raise InputError("The input cannot be empty.")
        if any([self.func, self.a, self.b, self.tol, self.max_iter, self.method]) == "":
            raise InputError("The input cannot be empty.")
        if not callable(self.func):
            raise FunctionError("The function must be callable.")
        if not isinstance(self.a, (int, float)):
            raise InputError("The lower bound must be a number.")
        if not isinstance(self.b, (int, float)):
            raise InputError("The upper bound must be a number.")
        if not isinstance(self.tol, (int, float)):
            raise InputError("The tolerance must be a number.")
        if not isinstance(self.max_iter, int):
            raise InputError("The maximum number of iterations must be an integer.")
        if not isinstance(self.method, str):
            raise InputError("The method must be a string.")
        if self.a < 0:
            raise InputError("The lower bound must be positive.")
        if self.b < 0:
            raise InputError("The upper bound must be positive.")
        if self.tol < 0:
            raise InputError("The tolerance must be positive.")
        if self.max_iter < 0:
            raise InputError("The maximum number of iterations must be positive.")
        if self.a >= self.b:
            raise IntervalError("The lower bound must be less than the upper bound.")
        if self.tol <= 0:
            raise ToleranceError("The tolerance must be greater than 0.")
        if self.max_iter <= 0:
            raise IterationError("The maximum number of iterations must be greater than 0.")
        if self.method != "bisection" and self.method != "falseposition":
            raise MethodError("The method must be either 'bisection' or 'falseposition'.")
        if self.func(self.a) * self.func(self.b) >= 0:
            raise SignError("The function must change sign over the interval.")
        return True
    
    def find_root(self) -> tuple[float, float, int, bool]:
        """
        Finds the root of the function.
        """
        for i in range(self.max_iter):
            a = self.a
            b = self.b
            if self.method == "bisection":
                c = (a + b) / 2
            else:
                c = b - (self.func(b) * (b - a)) / (self.func(b) - self.func(a))
            if abs(self.func(c)) < self.tol or abs(self.b - self.a) < self.tol:
                break
            elif self.func(a) * self.func(c) < 0:
                self.b = c
            else:
                self.a = c
        return c, self.func(c), i + 1, i + 1 >= self.max_iter


def f(x: float) -> float:
    return x ** 2 - 2


if __name__ == "__main__":
    root_finder = RootFinder(f, 0, 2, method="bisection")
    print(root_finder.root)
    print(root_finder.error)
    print(root_finder.iter)
    print(root_finder.flag)
    root_finder = RootFinder(f, 0, 2, method="falseposition")
    print(root_finder.root)
    print(root_finder.error)
    print(root_finder.iter)
    print(root_finder.flag)
