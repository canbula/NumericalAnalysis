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

         # Convert 16 bit float number to unsigned short number after conversion and discard '0b'
        output = bin(np.float16(value).view('H'))[2:].zfill(16) # pylint: disable=too-many-function-args
        return output
    
    

    def __str__(self):
        return self.value
        

