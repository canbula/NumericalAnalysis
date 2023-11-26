import numpy as np
def calculate_binary_integer_part(number):
    result = ""
    if number == 0:
        result += "0"

    while number != 0:
        result = str(number % 2) + result
        number = number // 2

    return result


def calculate_binary_decimal_part(number):
    result = ''
    while number != 0 and len(result) < 16:
        number = number * 2
        result += str(int(number))
        number = number - int(number)

    return result


def exponent_calculation(position_of_first_one, position_of_dot):
    if position_of_first_one != -1:
        if position_of_first_one < position_of_dot:
            exponent_decimal = position_of_dot - position_of_first_one + 14
        else:
            exponent_decimal = position_of_dot - position_of_first_one + 15
        if exponent_decimal > 31:
            print("An overflow error has occurred. The number is too large to be represented in half precision.")
            return "11111"
        binary_exponent = calculate_binary_integer_part(exponent_decimal)
        if len(binary_exponent) < 5:
            binary_exponent = "0" * (5 - len(binary_exponent)) + binary_exponent
    else:
        binary_exponent = "0" * 5
    return binary_exponent


def mantissa_calculation(mantissa_part):
    mantissa = ""
    if len(mantissa_part) > 10:
        mantissa_part = mantissa_part[:10]
    if mantissa_part != "0" * len(mantissa_part):
        if len(mantissa_part) <= 10:
            mantissa = mantissa_part + "0" * (10 - len(mantissa_part))
        elif len(mantissa_part) > 10:
            mantissa = mantissa_part[:10]
    else:
        mantissa = "0" * 10
    return mantissa


class HalfPrecision:
    def __init__(self, input_number):
        if isinstance(input_number, bool):
            raise TypeError("Input must be float")
        if not isinstance(input_number, (int, float)):
            raise TypeError("Input must be float")
        self.inputNumber = str(input_number)

    def __str__(self):
        if self.inputNumber == "inf":
            return "0111110000000000"
        elif self.inputNumber == "-inf":
            return "1111110000000000"

        if self.inputNumber[0] != "-":
            sign = "0"
        else:
            sign = "1"
            self.inputNumber = self.inputNumber[1:]

        input_integer = int(self.inputNumber.split(".")[0])
        input_decimal = float("0." + self.inputNumber.split(".")[1])
        binary_converted = f"{calculate_binary_integer_part(input_integer)}.{calculate_binary_decimal_part(input_decimal)}"
        position_of_first_one = binary_converted.find("1")
        position_of_dot = binary_converted.find(".")
        exponent = exponent_calculation(position_of_first_one, position_of_dot)
        if exponent == "11111":
            return f"{sign}{exponent}0000000000"
        #dot sliding
        if position_of_first_one != -1:
            dummy_binary_converted = binary_converted.replace(".", "")
            new_position_of_first_one = dummy_binary_converted.find("1")
            dummy_binary_converted = dummy_binary_converted[new_position_of_first_one + 1:]
            slided_binary = "1." + dummy_binary_converted
        else:
            slided_binary = binary_converted
        mantissa = mantissa_calculation(slided_binary.split(".")[1])
        return f"{sign}{exponent}{mantissa}"


if __name__ == "__main__":
    print(HalfPrecision(397.4532 * 10**10))
    print(HalfPrecision(np.inf))
    print(HalfPrecision(-np.inf))