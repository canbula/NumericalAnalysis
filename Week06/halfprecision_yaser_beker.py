class HalfPrecision:
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("Input must be a float.")
        self.number = number

    def __str__(self):
        # Check for special cases: NaN and infinity
        if self.number != self.number or self.number == float('inf') or self.number == float('-inf'):
            # Special case: infinity
            if self.number == float('inf'):
                return "0111110000000000"
            # Special case: negative infinity
            elif self.number == float('-inf'):
                return "1111110000000000"
            # Special case: NaN
            else:
                return "0111111000000000"

        # Check for zero
        if self.number == 0.0:
            # Check for negative zero
            if str(self.number)[0] == '-':
                return "1000000000000000"
            else:
                return "0000000000000000"

        # Get the sign bit
        sign_bit = '0' if self.number >= 0 else '1'

        # Convert the number to positive for simplicity
        number = abs(self.number)

        # Check for large numbers
        if number >= 65536.0:
            return "0111110000000000"

        # Calculate the exponent and adjust the number
        exponent = 0
        while number >= 2.0:
            number /= 2.0
            exponent += 1
        while number < 1.0:
            number *= 2.0
            exponent -= 1

        # Convert the exponent to biased representation
        exponent += 15
        exponent_bits = format(exponent, '05b')

        # Convert the mantissa
        mantissa = format(int((number - 1.0) * 2**10), '010b')

        # Combine the bits
        binary_string = sign_bit + exponent_bits + mantissa

        return binary_string
    

test_cases = [
    (0.15625, "0011000100000000"),
    (13.375, "0100101010110000"),
    (-13.375, "1100101010110000"),
    (0.0, "0000000000000000"),
    (-0.0, "1000000000000000"),
    (0.1, "0010111001100110"),
    (-0.1, "1010111001100110"),
    (0.2, "0011001001100110"),
    (-86.954, "1101010101101111"),
    (3974532000000.0, "0111110000000000"),
    (float('inf'), "0111110000000000"),
    (float('-inf'), "1111110000000000")
]

for number, expected_output in test_cases:
    half_precision = HalfPrecision(number)
    binary_string = str(half_precision)
    print(f"Input: {number}, Expected: {expected_output}, Output: {binary_string}")
