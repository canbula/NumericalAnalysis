import math

class HalfPrecision:
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("Input must be a float")
        self.number = number

    def __str__(self):
        if math.copysign(1, self.number) == -1:
            sign_bit = "1"
        else:
            sign_bit = "0"

        value = abs(self.number)

        if value == 0.0:
            return sign_bit + "00000" + "0000000000"

        if math.isinf(value):
            return sign_bit + "11111" + "0000000000"

        m, e = math.frexp(value)
        normalized_mantissa = m * 2
        exponent = e - 1
        biased_exponent = exponent + 15

        if biased_exponent >= 31:
            return sign_bit + "11111" + "0000000000"

        if biased_exponent <= 0:
            return sign_bit + "00000" + "0000000000"

        fractional_part = normalized_mantissa - 1
        mantissa_int = int(round(fractional_part * 1024))

        if mantissa_int == 1024:
            mantissa_int = 0
            biased_exponent += 1
            if biased_exponent >= 31:
                return sign_bit + "11111" + "0000000000"

        exponent_str = f"{biased_exponent:05b}"
        mantissa_str = f"{mantissa_int:010b}"

        return sign_bit + exponent_str + mantissa_str
