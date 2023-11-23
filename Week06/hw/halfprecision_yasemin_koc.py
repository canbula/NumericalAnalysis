import math

import numpy


class HalfPrecision:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int, float, or bool")
        self.number = number
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        self.number = number
    def __str__(self):
        try:
            num = float(self.number)
            if num == 0 and str(self.number)[0] == "-":
                return '1'+'0'*15
            if num == 0:
                return '0'*16
            if math.isinf(num):
                return '0'+'1'*5+'0'*10 if num > 0 else '1' +'1'*5+'0'*10
            elif math.isnan(num):
                return '0'+'1'*15
            else:
                result = get_scientific_notation(calculate_binary_conversion(num))
                print(calculate_binary_conversion(num))
                return get_IEEE754_format(num, result[0], result[2][:10])
        except (ValueError, TypeError):
            raise TypeError("Invalid input type or value, expected a valid number")
    def get_number(self):
        try:
            num = float(self.number)
            if math.isinf(num) or math.isnan(num):
                raise TypeError("Invalid input type or value, expected a valid number")
            result = get_scientific_notation(calculate_binary_conversion(num))
            print(result)
            return get_IEEE754_format(num, result[0], result[2][:10])
        except (ValueError, TypeError):
            raise TypeError("Invalid input type or value, expected a valid number")
def calculate_binary_conversion(number):
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number
    part_of_integer = calculate_binary_conversion_for_integer_part(number)
    part_of_decimal = calculate_binary_conversion_for_decimal_part(number)
    binary = f"{part_of_integer}.{part_of_decimal}"
    if is_negative:
        binary = '-' + binary
    return binary
def calculate_binary_conversion_for_integer_part(number):
    result = ""
    number_of_integer = abs(int(str(number).split(".")[0]))
    if number_of_integer == 0:
        return "0"
    while number_of_integer != 0:
        remainder = number_of_integer % 2
        result += str(remainder)
        number_of_integer //= 2
    return result[::-1]
def calculate_binary_conversion_for_decimal_part(number):
    decimal_part, integer_part = math.modf(number)
    if decimal_part == 0:
        return ''
    binary = ''
    while decimal_part > 0:
        decimal_part *= 2
        bit = int(decimal_part)
        binary += str(bit)
        decimal_part -= bit
    return binary
def get_scientific_notation(binary_string):
    if binary_string[-1] == '.':
        return [0, 2 ** 0 * (float(binary_string+"0"*10)), "0"*10]
    index_of_comma = binary_string.index(".") - 1
    index_of_one = binary_string.index('1') - 1
    result = index_of_comma - index_of_one
    if result > 0:
        result -= 1
    mantissa = binary_string[index_of_one + 2::1].replace('.', '')
    concatenated_data = binary_string[index_of_one + 1] + "." + mantissa
    return [result, 2 ** (result) * float(concatenated_data), mantissa]
def get_IEEE754_format(float_input, exponential_part, mantissa):
    ieee_754_format = ""
    if float_input < 0:
        ieee_754_format += "1"
    else:
        ieee_754_format += "0"
    print(float_input)
    if float_input < 2**16 -1:
        bias_result = (2 ** 5 - 2) / 2 + exponential_part
    else:
        bias_result = (2 ** 6 - 2) / 2 + exponential_part
    print(bias_result)
    converted_binary_bias = calculate_binary_conversion(bias_result).replace('.', '').replace('-', '')
    ieee_754_format += "{:0>{}}".format(converted_binary_bias, 5)
    ieee_754_format += "{:0<10}".format(mantissa[:10])
    return ieee_754_format

