class HalfPrecision:
    def __init__(self,number): 
        if not isinstance(number,float):
            raise TypeError("Input must be a float")
        
        self.number = number 
        self.binary = self._convert_to_half_precision()

    def _convert_to_half_precision(self):
        if self.number != self.number or self.number == float("inf") or self.number == float("-inf"):
            return self._special_cases()
        
        sign_bit = 0 
        if self.number >= 0 : 
            sign_bit = 0 
        else: 
            sign_bit = 1 
            self.number = -self.number
        
        self.number = abs(self.number)  
        
        exponent_bits = 0 
        
        mantissa_bits = self.number 
        
        if self.number < 2**(-14):
            return self._special_cases()
       
        elif self.number >= 2**(15):
            return self._special_cases()
        
        elif self.number < 2**(-1):
            while self.number < 2**(-1):
                self.number *= 2 
                exponent -= 1 
            mantissa = self.number - 1 
        
        elif self.number >= 2**(-1):
            while self.number >= 2**(-1):
                self.number /= 2 
                exponent += 1 
            mantissa = self.number - 1
        binary_representation = f"{sign_bit:01b}{exponent_bits}{mantissa_bits}"
        return binary_representation
    
    def _special_cases(self):
        if self.number != self.number:
            return "0111111111111111"  # NaN
        elif self.number == float('inf'):
            return "0111110000000000"  # Positive infinity
        else:
            return "1111110000000000"  # Negative infinity

    def __str__(self):
        return self.binary
    
