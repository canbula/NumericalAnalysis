from decimal import Decimal, getcontext


class IEEE754:
    def __init__(
        self,
        number: str = "0.0",
        precision: int = 2,
        force_exponent: int = None,
        force_mantissa: int = None,
    ) -> None:
        getcontext().prec = 256
        self.precision: int = precision
        exponent_list: list[int] = [5, 8, 11, 15, 19]
        mantissa_list: list[int] = [10, 23, 52, 112, 236]
        self.__exponent: int = (
            force_exponent
            if force_exponent is not None
            else exponent_list[self.precision]
        )
        self.__mantissa: int = (
            force_mantissa
            if force_mantissa is not None
            else mantissa_list[self.precision]
        )
        self.__bias: int = 2 ** (self.__exponent - 1) - 1
        self.__edge_case: str = None
        self.number: Decimal = self.validate_number(number)
        if self.__edge_case is None:
            self.sign: str = self.find_sign()
            self.__scale, self.number = self.scale_up_to_integer(self.number, 2)
            self.binary: str = f"{self.number:b}"
            self.binary_output: str = (
                f"{self.binary[:-self.__scale]}.{self.binary[-self.__scale:]}"
            )
            self.exponent = self.find_exponent()
            self.mantissa = self.find_mantissa()

    def validate_number(self, number: str) -> Decimal:
        if number == "":
            number = "0.0"
        if Decimal(number).is_infinite():
            if Decimal(number) > 0:
                # +inf: 0 11111111 00000000000000000000000
                self.__edge_case = f"0 {'1' * self.__exponent} {'0' * self.__mantissa}"
                return Decimal("Infinity")
            # -inf: 1 11111111 00000000000000000000000
            self.__edge_case = f"1 {'1' * self.__exponent} {'0' * self.__mantissa}"
            return Decimal("-Infinity")
        if Decimal(number).is_nan() and Decimal(number).is_snan():
            # snan: 0 11111111 00000000000000000000001
            self.__edge_case = (
                f"0 {'1' * self.__exponent} {'0' * (self.__mantissa - 1)}1"
            )
            return Decimal("NaN")
        if Decimal(number).is_nan() and Decimal(number).is_qnan():
            # qnan: 0 11111111 10000000000000000000000
            self.__edge_case = (
                f"0 {'1' * self.__exponent} 1{'0' * (self.__mantissa - 1)}"
            )
            return Decimal("NaN")
        if not number == number:
            # nan: 0 11111111 11111111111111111111111
            self.__edge_case = f"0 {'1' * self.__exponent} {'1' * self.__mantissa}"
            return Decimal("NaN")
        if Decimal(number) == 0:
            if Decimal(number).is_signed():
                # -0: 1 00000000 00000000000000000000000
                self.__edge_case = f"1 {'0' * self.__exponent} {'0' * self.__mantissa}"
            else:
                # +0: 0 00000000 00000000000000000000000
                self.__edge_case = f"0 {'0' * self.__exponent} {'0' * self.__mantissa}"
            return Decimal("0")
        if isinstance(number, int):
            number = f"{number}.0"
        if not isinstance(number, str):
            number = str(number)
        try:
            number = Decimal(number)
        except:
            raise ValueError(f"Invalid number: {number}")
        denormalized_range = self.calculate_denormalized_range(
            self.__exponent, self.__mantissa
        )
        if Decimal(number) < Decimal(denormalized_range[0]):
            raise ValueError(
                f"Number is too small, must be larger than {denormalized_range[0]}, we lost both exponent and mantissa, please increase precision."
            )
        if Decimal(number) < Decimal(denormalized_range[1]):
            raise ValueError(
                f"Number is too small, must be larger than {denormalized_range[1]}, we lost exponent, please increase precision."
            )
        return number

    @staticmethod
    def calculate_denormalized_range(exponent_bits: int, mantissa_bits: int) -> tuple:
        bias = 2 ** (exponent_bits - 1) - 1
        smallest_normalized = 2 ** -(bias - 1)
        smallest_denormalized = smallest_normalized * 2**-mantissa_bits
        largest_denormalized = smallest_normalized - 2 ** -(bias + mantissa_bits - 1)

        return (smallest_denormalized, largest_denormalized)

    def find_sign(self) -> str:
        if self.number < 0:
            return "1"
        return "0"

    @staticmethod
    def scale_up_to_integer(number: Decimal, base: int) -> (int, int):
        scale = 0
        while number != int(number):
            number *= base
            scale += 1
        return scale, int(number)

    def find_exponent(self) -> str:
        exponent = len(self.binary) - 1 + self.__bias - self.__scale
        # fill with leading zeros if necessary
        return f"{exponent:0{self.__exponent}b}"

    def find_mantissa(self) -> str:
        # fill with trailing zeros if necessary
        mantissa = f"{self.binary[1:]:<0{self.__mantissa}}"
        if len(mantissa) > self.__mantissa:
            # round up if mantissa is too long
            mantissa = f"{mantissa[: self.__mantissa - 1]}1"
        return mantissa

    def __str__(self) -> str:
        if self.__edge_case is not None:
            return self.__edge_case
        return f"{self.sign} {self.exponent} {self.mantissa}"

    def hex(self) -> str:
        h = ""
        s = str(self).replace(" ", "")
        limit = len(s) - (len(s) % 4)
        for i in range(0, limit, 4):
            ss = s[i : i + 4]
            si = 0
            for j in range(4):
                si += int(ss[j]) * (2 ** (3 - j))
            sh = hex(si)
            h += sh[2]
        return h.upper()

    def json(self) -> dict:
        return {
            "exponent-bits": self.__exponent,
            "mantissa-bits": self.__mantissa,
            "bias": self.__bias,
            "sign": self.sign,
            "exponent": self.exponent,
            "mantissa": self.mantissa,
            "binary": self.binary,
            "binary_output": self.binary_output,
            "hex": self.hex(),
            "up scaled number": self.number,
            "scale": self.__scale,
            "number": self.number / (2**self.__scale),
        }

    def __repr__(self) -> str:
        return self.__str__()


def half(x: str) -> IEEE754:
    return IEEE754(x, 0)


def single(x: str) -> IEEE754:
    return IEEE754(x, 1)


def double(x: str) -> IEEE754:
    return IEEE754(x, 2)


def quadruple(x: str) -> IEEE754:
    return IEEE754(x, 3)


def octuple(x: str) -> IEEE754:
    return IEEE754(x, 4)


if __name__ == "__main__":
    # with default options (Double Precision)
    x = 13.375
    a = IEEE754(x)
    # you should call the instance as a string
    print(a)
    print(str(a))
    print(f"{a}")
    # you can get the hexadecimal presentation like this
    print(a.hex())
    # or you can specify a precision
    for p in range(5):
        a = IEEE754(x, p)
        print("x = %f | b = %s | h = %s" % (13.375, a, a.hex()))
    # or you can use your own custom precision
    a = IEEE754(x, force_exponent=6, force_mantissa=12)
    print(f"{a}")
    # you can get more details with json
    print(a.json())

    # you can also call the precision functions
    x = 13.375
    print(half(x))
    print(single(x))
    print(double(x))
    print(quadruple(x))
    print(octuple(x))
