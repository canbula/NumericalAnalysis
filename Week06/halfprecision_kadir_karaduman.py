from math import modf


class HalfPrecision:
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("Input must be a float")
        self.number = number

    def __str__(self):
        # For regular numbers
        sign_bit = "1" if self.number < 0 else "0"
        exponent, mantissa = self.calculate_exponent_and_mantissa()

        # Format the result as a 16-character binary string
        return f"{sign_bit}{exponent}{mantissa}"

    def calculate_exponent_and_mantissa(self):
        # Calculate biased exponent
        biased_exponent = 1023 + 52

        # Adjust exponent and mantissa
        if self.number != 0.0:
            exponent = format(biased_exponent, '011b')
            mantissa = self.calculate_mantissa()
        else:
            # For zero, set exponent and mantissa to zero
            exponent = "00000"
            mantissa = "0" * 10

        return exponent, mantissa

    def calculate_mantissa(self):
        abs_number = abs(self.number)
        mantissa = ""

        for _ in range(10):
            abs_number, digit = modf(abs_number * 2)
            mantissa += str(int(digit))

        return mantissa
