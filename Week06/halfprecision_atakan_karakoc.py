import math
import numpy as np

class HalfPrecision:
    def __init__(self, number: float) -> str:
        if not isinstance(number, float):
            raise TypeError("Input must be float")
        self.number = abs(number)
        self.sign_bit = 1 if math.copysign(1, number) == -1 else 0
        self.bias = 15
        self.mantissa_bit = 10
        self.exponent_bit = 5
        self.exponent = ""
        self.mantissa = ""
        self.int_part = ""
        self.dec_part = ""
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
        self.int_part = self.calculate_int_part(int(self.number))
        self.dec_part = self.calculate_dec_part(self.number - int(self.number))
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

    def calculate_int_part(self, int_part):
        result = ""
        if int_part == 0:
            result += str(int_part)
            return result
        else:
            while int_part > 0:
                remainder = int_part % 2
                result += str(remainder)
                int_part = int_part // 2
        return result[::-1]

    def calculate_dec_part(self, dec_part):
        result = ""
        count = 0
        while dec_part != 0:
            dec_part *= 2
            if dec_part >= 1:
                result += "1"
                dec_part -= 1
                count += 1
            else:
                result += "0"
                if count != 0:
                    count += 1
            if count > 10:
                break
        return result

    def ieee(self):
        if self.int_part == "0":
            for i in range(len(self.dec_part)):
                if self.dec_part[i] == '1':
                    self.set_mantissa(self.dec_part[(i + 1):])
                    self.set_exponent(self.calculate_int_part(self.bias - (i + 1)))
                    break
        else:
            self.set_exponent(self.calculate_int_part((len(self.int_part) - 1) + self.bias))
            binary_res = f"{self.int_part}{self.dec_part}"
            self.set_mantissa(binary_res[1:])
