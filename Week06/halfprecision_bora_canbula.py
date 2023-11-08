import numpy as np
import math


class HalfPrecision:
    def __init__(self, number: float):
        if not isinstance(number, float):
            raise TypeError("number must be a float")
        self.number = number

    def __str__(self) -> str:
        # Special cases checks
        if np.isnan(self.number):  # NaN
            return "0111111111111111"  # Using the convention for qNaN
        if np.isinf(self.number):  # Infinity
            sign = "0" if self.number > 0 else "1"
            return f"{sign}111110000000000"  # Positive or negative infinity

        # Sign bit
        sign = 0 if math.copysign(1, self.number) >= 0 else 1

        # Handle zero (positive and negative)
        if self.number == 0:
            return f"{sign}000000000000000"

        # Normalization and bias adjustment
        normalized_num = np.abs(self.number)
        exponent = 15  # The bias for 16-bit IEEE754

        # Handling Denormals
        if normalized_num < 2 ** (-14):  # Smallest normal number
            mantissa = normalized_num / 2 ** (-24)
            exponent_bits = "00000"
            mantissa_bits = format(int(mantissa), "010b")
        else:
            # Normalizing the mantissa
            while not (1 <= normalized_num < 2):
                if normalized_num >= 2:
                    normalized_num /= 2
                    exponent += 1
                else:
                    normalized_num *= 2
                    exponent -= 1

            # Rounding the mantissa to 10 bits
            mantissa = int((normalized_num - 1) * 2**10 + 0.5)

            # Check for overflow
            if exponent >= 31:
                return f"{sign}111110000000000"  # Overflow to Infinity

            # Convert exponent and mantissa to binary
            exponent_bits = f"{exponent:05b}"
            mantissa_bits = f"{mantissa:010b}"

        return f"{sign}{exponent_bits}{mantissa_bits}"


# Testing
if __name__ == "__main__":
    cases = [
        0.15625,
        13.375,
        -13.375,
        0.0,
        -0.0,
        0.1,
        -0.1,
        0.2,
        -86.954,
        397.4532 * 10**10,
        np.inf,
        -np.inf,
        np.nan,
        2 ** (-14),
        2 ** (-15),
    ]
    for case in cases:
        print(f'({case}, "{HalfPrecision(case)}")')
