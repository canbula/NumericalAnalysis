import math, numpy
class HalfPrecision:
    def __init__(self,number:float) -> None:
        if not isinstance(number,float):
            raise TypeError("The number must be float.")
        self.number = number
        self.binary_rep = self.binary_representation()
        self.sign_bit = ""
        self.exponent = ""
        self.mantissa = ""
        self.bias = 15
        self.ieee_16_representation = ""


    def __str__(self) -> str:
        self.sign_bit_calculate()
        self.exponent_mantissa_calculate()
        self.ieee_16_calculate()
        
        return self.ieee_16_representation
        

    def binary_representation(self) -> str:
        integer_part_10based, decimal_part_10based  = int(math.modf(self.number)[1]), math.modf(self.number)[0]
        while decimal_part_10based > 1:
            decimal_part_10based = decimal_part_10based * (10**-1)
        integer_part_binary = self.integer_binary_calculate(integer_part_10based)
        decimal_part_binary = self.decimal_binary_calculate(decimal_part_10based)
        return integer_part_binary + "." + decimal_part_binary
    

    def integer_binary_calculate(self, number) -> str:
        result = ""
        while True:
            if(number % 2 == 0):
                result += "0"
            else:
                result += "1"

            number = int(number / 2)
            if(number < 2):
                result += "1"
                break
        return result[::-1]
    
    def decimal_binary_calculate(self, number) -> str:
        result = ""
        while True:
            number = number * 2
            if math.modf(number)[0] == 0:
                result += "1"
                break
            if(number > 1):
                result += "1"
                number -= 1
            else:
                result += "0"
        return result


    def sign_bit_calculate(self):
        if self.number > 0:
            self.sign_bit = "0"
        else:
            self.sign_bit = "1"


    def exponent_mantissa_calculate(self):
        scientific_representation = float(self.binary_rep)
        exponent_of_2 = 0
        while scientific_representation > 2:
            scientific_representation = scientific_representation * (10**-1)
            exponent_of_2 += 1
        self.mantissa = (str(scientific_representation).split(".")[1])[0:10]
        print("Mantissa :", self.mantissa)
        exponent_10based = exponent_of_2 + self.bias
        self.exponent = self.integer_binary_calculate(exponent_10based)

    def ieee_16_calculate(self):
        if self.number == numpy.inf or self.number == -numpy.inf or self.exponent == "00000":
            self.ieee_16_representation = self.sign_bit + "111110000000000"
        else:
            self.ieee_16_representation = self.sign_bit + self.exponent + self.mantissa
