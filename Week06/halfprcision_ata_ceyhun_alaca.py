import math
import numpy as np

class HalfPrecision:
    def __init__(self, number: float) -> str:
        if not isinstance(number, float):
            raise TypeError("The given input must be a floating point number.")
        self.number = abs(number)
        self.sign_bit = 1 if math.copysign(1, number) == -1 else 0
        self.bias = 15
        self.mantissa_bit = 10
        self.exponent_bit = 5
        self.exponent = ""
        self.mantissa = ""
        self.integer_part = ""
        self.decimal_part = ""
        dec_part_last = str(number).split(".")[1] if "." in str(number) else ""
        if dec_part_last and all(char == "0" for char in dec_part_last):
            if self.number == 0.0 or self.number == -0.0:
                self.calculate()
            else:
                self.set_exponent("11111")
                self.set_mantissa("0000000000")
        elif number == np.inf:
            self.set_exponent("11111")
            self.set_mantissa("0000000000")
        elif number == -np.inf:
            self.set_exponent("11111")
            self.set_mantissa("0000000000")
        else:
            self.calculate()

    def calculate(self):
        self.integer_part = self.calc_int_section(int(self.number))
        self.decimal_part = self.calc_decimal_section(self.number - int(self.number))
        self.ieee()

    def __str__(self):
        mantissa = ""
        exponent = ""
        if len(self.exponent) < self.exponent_bit:
            for i in range(self.exponent_bit - len(self.exponent)):
                exponent += "0"
            self.set_exponent(exponent + self.exponent)
        if len(self.mantissa) < self.mantissa_bit:
            for i in range(self.mantissa_bit - len(self.mantissa)):
                mantissa += "0"
            self.set_mantissa(self.mantissa + mantissa)
        else:
            self.set_mantissa(self.mantissa[0:10])
        ieee754 = str(str(self.sign_bit) + str(self.exponent) + str(self.mantissa))
        return ieee754

    def set_exponent(self, exponent):
        self.exponent = exponent

    def set_mantissa(self, mantissa):
        self.mantissa = mantissa

    def calc_int_section(self, integer_part):
        result = ""
        if integer_part == 0:
            result += str(integer_part)
            return result
        else:
            while integer_part > 0:
                remainder = integer_part % 2
                result += str(remainder)
                integer_part = integer_part // 2
        return result[::-1]

    def calc_decimal_section(self, decimal_part):
        result = ""
        count = 0
        while decimal_part != 0:
            decimal_part *= 2
            if decimal_part >= 1:
                result += "1"
                decimal_part -= 1
                count += 1
            else:
                result += "0"
                if count != 0:
                    count += 1
            if count > 10:
                break
        return result

    def ieee(self):
        if self.integer_part == "0":
            for i in range(len(self.decimal_part)):
                if self.decimal_part[i] == '1':
                    self.set_mantissa(self.decimal_part[(i + 1):])
                    self.set_exponent(self.calc_int_section(self.bias - (i + 1)))
                    break
        else:
            self.set_exponent(self.calc_int_section((len(self.integer_part) - 1) + self.bias))
            binary_res = f"{self.integer_part}{self.decimal_part}"
            self.set_mantissa(binary_res[1:])
