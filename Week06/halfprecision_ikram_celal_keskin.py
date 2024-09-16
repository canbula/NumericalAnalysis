import numpy as np

class HalfPrecision:
    def __init__(self, value):
        if isinstance(value, float):
            self.value = self.half_precision(value)
        else:
            raise TypeError(f"Invalid input type: {type(value)}")

    def half_precision(self, value):
        if value == 0.0: #0.0 and -0.0 case
            return '0' * 16 if not np.signbit(value) else '1' + ('0' * 15)
        if value in {np.inf, -np.inf}: # positive infinite and negative infinite case
            return '0111110000000000' if value > 0 else '1111110000000000'
        if value != value:  # NaN case
            return '0111111111111111'

        # Convert the given 'value' to a 16-bit floating-point representation using np.float16.
        # Then, view the resulting value as a 16-bit unsigned integer using 'view('H')'.
        # Finally, convert the integer to a binary string representation using 'bin'.
        # Removes '0b' from the first two lines before outputting
        # Fills empty bits with 00 to complete 16 bits
        output = bin(np.float16(value).view('H'))[2:].zfill(16) # pylint: disable=too-many-function-args
        return output
    
    

    def __str__(self):
        return self.value
        

