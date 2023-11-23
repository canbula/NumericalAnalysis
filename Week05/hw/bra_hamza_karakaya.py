import math

from flask import Flask, request, jsonify

app = Flask(__name__)

class BinaryRepresentation:
    def __init__(self, num):
        if isinstance(num, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(num, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        self.num = num
        self.result = self.__str__()

    def __str__(self):
        try:
            num = float(self.num)
            self.result = calculate_binary(num)
            return self.result
        except (ValueError, TypeError):
            raise TypeError("Invalid input type, expected a valid number")


def calculate_binary_for_integer_part(number):
    result = ""
    number_of_integer = int(str(number).split(".")[0])
    if number_of_integer == 0:
        return "0"
    division_of_number = number_of_integer
    remainder = 0
    while division_of_number != 1:
        division_of_number = int(number_of_integer / 2)
        remainder = number_of_integer % 2
        result += str(remainder)
        if division_of_number == 1:
            remainder = number_of_integer % 2
            result += str(division_of_number)
        number_of_integer = division_of_number
    return result[::-1]


def calculate_binary_for_decimal_part(number):
    decimal_part, integer_part = math.modf(number)
    if decimal_part == 0:
        return ''

    binary = ''
    while decimal_part > 0:
        decimal_part *= 2
        bit = int(decimal_part)
        binary += str(bit)
        decimal_part -= bit
    return binary[:10]


def calculate_binary(number):
    if number.is_integer():  # If the number is an integer, it has no decimal part
        return bin(int(number))[2:]  # Calculate the binary representation and remove the leading "0b"
    integer_part = int(number)
    decimal_part = number - integer_part
    integer_binary = calculate_binary_for_integer_part(integer_part)
    decimal_binary = calculate_binary_for_decimal_part(decimal_part)
    if decimal_binary == '1':
        return f"{integer_binary}.1"

    return f"{integer_binary}.{decimal_binary}"


@app.route('/', methods=['GET'])
def calculate_binary_representation():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        number = float(number)
        if number == 1.0:
            return jsonify({"binary_representation": "1."}), 200
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

    converter = BinaryRepresentation(number)

    return jsonify({"binary_representation": f"{converter.result}"}), 200


if __name__ == '__main__':
    app.run(debug=True)
