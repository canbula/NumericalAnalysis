import numpy as np
# import os

class HalfPrecision:
    """
    This class converting a floating point number to half precision format.
    The half precision format is a 16-bit format with 1 sign bit, 5 exponent bits, and 10 mantissa bits.
    The sign bit is 0 for positive numbers and 1 for negative numbers. 

    Attributes:
        number: float

    Raises:
        TypeError: If the input is the string, bool, list, tuple, or set.
        TypeError: If the input cannot be converted to a float.

    Returns:
        str: The half precision format of the input number.
    """
    def __init__(self,number):
        if isinstance(number,(str,bool,list,tuple,set)):
            raise TypeError(f"Invalid input {type(number)}")
        try:
            self.__number = float(number)
        except Exception as e:
            raise TypeError("Input {} cannot be converted to a float".format(e.args[0]))
            
    def __str__(self)->str:
        """
        Returns the half precision format of the input number.

        Returns:
            str: The half precision format of the input number.
        """
        return self.__calculate_precision(5,10,self.__number) #for half precision
    
    def __calculate_precision(self,exponent_length:int,mantissa_length:int,number:float)->str:
        """
        This function calculates the half precision format of the input number.
        """
        sign= False

        if number < 0 or np.signbit(number):
            sign = True
            number = -number
        
        if np.isinf(number):
            return f"{int(sign)}{'1'*exponent_length}{'0'*mantissa_length}"
        
        bias= 2**(exponent_length-1)-1
        mantissa,power = self.__calculate_mantissa(mantissa_length,number)
        
        if power == None:
            return f"{int(sign)}{'0'*exponent_length}{'0'*mantissa_length}"
        
        exponent = self.__calculate_exponent(bias,power,exponent_length)

        return f"{int(sign)}{exponent}{mantissa}"

    def __calculate_exponent(self,bias:int,power:int,exponent_length)->str:
        """
        This function calculates the exponent part of the half precision format.
        """
        binary_exponent = self.__integer_to_binary(bias+power)
        
        if len(binary_exponent) < exponent_length:
            binary_exponent = '0' * (exponent_length - len(binary_exponent)) + binary_exponent
        
        return binary_exponent

    def __calculate_mantissa(self,mantissa_length:int,number:float)->str:
        """
        This function calculates the mantissa part of the half precision format.
        """
        integer_part,decimal_part = f"{number:.20f}".split(".")
        integer_part = self.__integer_to_binary(integer_part)
        decimal_part = self.__decimal_to_binary(decimal_part)

        mantissa = f'{integer_part}.{decimal_part}'
        
        if not '1' in mantissa:
            return '0'*mantissa_length,None

        power = 0
        index1 = mantissa_length
        
        indexdot = mantissa.index(".")
        index1 = mantissa.index("1")
        mantissa = mantissa[index1+1:].replace(".","")
        power = indexdot - index1 if indexdot < index1 else indexdot - index1 -1

        if len(mantissa)< mantissa_length:
            mantissa += '0' * (mantissa_length - len(mantissa))
        elif len(mantissa)> mantissa_length:
            mantissa = mantissa[:mantissa_length-1] + '1'
          

        return mantissa,power

    def __integer_to_binary(self,number:int)->str:
        
        result = ""
        number = int(number)

        if number == 0:
            return "0"
        
        while number != 0:
            remainder = number % 2
            result += str(remainder)
            number //= 2
        
        return result[::-1]

    def __decimal_to_binary(self,number:float)->str:
        number=float(f"0.{number.split("0")[0]}")

        if number == 0:
            return ''
        
        binary = ''
        while number > 0 and len(binary) < 100:
            
            number *= 2
            if number >= 1:
                binary += '1'
                number -= 1
            else:
                binary += '0'
        
        return binary



# if __name__=="__main__":
#     os.system("pytest -v test_halfprecision.py")



