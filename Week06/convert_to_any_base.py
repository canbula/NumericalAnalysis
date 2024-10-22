import string

full_set = string.digits + string.ascii_uppercase


def convert_integer_to_any_base(number, base):
    """
    Convert an integer to any base.
    :param number: The integer to convert.
    :param base: The base to convert to.
    :return: The converted integer.
    """
    # convert the integer part
    result = ""
    while number > 0:
        # result = str(number % base) + result
        result = full_set[(number % base)] + result
        number //= base
    return result


def convert_decimal_to_any_base(number, base):
    """
    Convert a decimal number to any base.
    :param number: The decimal number to convert.
    :param base: The base to convert to.
    :return: The converted decimal number.
    """
    # convert the decimal part
    result = ""
    while number > 0:
        number *= base
        # result += str(int(number))
        result += full_set[(int(number))]
        number -= int(number)
    return result


def convert_to_any_base(number: float, base: int) -> str:
    """
    Convert a number to any base.
    :param number: The number to convert.
    :param base: The base to convert to.
    :return: The converted number.
    """
    # get the integer part
    integer = int(number)
    # get the decimal part
    decimal = number - integer
    # convert the integer part
    integer = convert_integer_to_any_base(integer, base)
    # convert the decimal part
    decimal = convert_decimal_to_any_base(decimal, base)
    # return the result
    return integer + "." + decimal


def main():
    """
    Test function.
    :return: None
    """
    print(convert_to_any_base(13.375, 2))
    print(convert_to_any_base(13.375, 4))
    print(convert_to_any_base(13.375, 8))
    print(convert_to_any_base(13.375, 16))


if __name__ == "__main__":
    print(full_set)
    main()
