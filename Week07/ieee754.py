from decimal import Decimal, getcontext


class IEEE754:
    def __init__(
        self,
        number: str = "0.0",
        precision: int = 2,
        force_length: int = None,
        force_exponent: int = None,
        force_mantissa: int = None,
    ) -> None:
        getcontext().prec = 256
        self.precision: int = precision
        length_list: list = [16, 32, 64, 128, 256]
        exponent_list: list = [5, 8, 11, 15, 19]
        mantissa_list: list = [10, 23, 52, 112, 236]
        self.__length: int = (
            force_length if force_length is not None else length_list[precision]
        )
        self.__exponent: int = (
            force_exponent if force_exponent is not None else exponent_list[precision]
        )
        self.__mantissa: int = (
            force_mantissa if force_mantissa is not None else mantissa_list[precision]
        )
        self.__bias: int = 2 ** (self.__exponent - 1) - 1
        self.__edge_case: str = None
        self.number: Decimal = self.validate_number(number)
        if self.__edge_case is None:
            self.__sign: str = self.find_sign(self.number)
            self.__scale, self.number = self.scale_up_to_integer(self.number)
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
                self.__edge_case = f"0 {'1' * self.__exponent} {'0' * self.__mantissa}"
                return Decimal("Infinity")
            self.__edge_case = f"1 {'1' * self.__exponent} {'0' * self.__mantissa}"
            return Decimal("-Infinity")
        if Decimal(number).is_nan() and Decimal(number).is_snan():
            self.__edge_case = (
                f"0 {'1' * self.__exponent} {'0' * (self.__mantissa - 1)}1"
            )
            return Decimal("NaN")
        if Decimal(number).is_nan() and Decimal(number).is_qnan():
            self.__edge_case = (
                f"0 {'1' * self.__exponent} 1{'0' * (self.__mantissa - 1)}"
            )
            return Decimal("NaN")
        if not number == number:
            self.__edge_case = f"0 {'1' * self.__exponent} {'1' * self.__mantissa}"
            return Decimal("NaN")
        if Decimal(number) == 0:
            if Decimal(number).is_signed():
                self.__edge_case = f"1 {'0' * self.__exponent} {'0' * self.__mantissa}"
            else:
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

    @staticmethod
    def scale_up_to_integer(number: Decimal) -> (int, int):
        scale = 0
        while number != int(number):
            number *= 2
            scale += 1
        return scale, int(number)

    @staticmethod
    def find_sign(number: int) -> str:
        if number < 0:
            return "1"
        return "0"

    def find_exponent(self) -> str:
        exponent = len(self.binary) - 1 + self.__bias - self.__scale
        return f"{exponent:0{self.__exponent}b}"

    def find_mantissa(self) -> str:
        mantissa = f"{self.binary[1:]:<0{self.__mantissa}}"
        if len(mantissa) > self.__mantissa:
            mantissa = f"{mantissa[: self.__mantissa - 1]}1"  # round up
        return mantissa

    def __str__(self) -> str:
        if self.__edge_case is not None:
            return self.__edge_case
        return f"{self.__sign} {self.exponent} {self.mantissa}"


if __name__ == "__main__":
    number = "0.000000000000000000000004"
    number = "4e-24"
    number = 1e-38
    number = -0
    print(f"number: {number}")
    ieee754_number = IEEE754(number=number, precision=2)
    print(f"ieee754: {ieee754_number}")
