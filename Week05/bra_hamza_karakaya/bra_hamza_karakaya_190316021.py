import math

from flask import Flask, request, jsonify

app = Flask(__name__)


class NumberConverter:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        self.number = number

    def get_binary_representation(self):
        try:
            num = float(self.number)
            number_as_string = self.calculate_binary(num)
            return number_as_string
        except (ValueError, TypeError):
            raise TypeError("Invalid input type, expected a valid number")

    def calculate_binary(self, number):
        if number == int(number):  # If it's an integer
            if number >= 0:
                return bin(int(number))[2:]  # Calculate its binary representation and remove the leading "0b"
            else:
                return '-' + bin(abs(int(number)))[2:]  # If it's a negative integer, add a minus sign

        integer_part = int(abs(number))  # Get the integer part of the number (make it positive if negative)
        decimal_part = abs(number) - integer_part  # Get the decimal part of the number

        binary_integer = bin(integer_part)[2:]  # Calculate the binary representation of the integer part
        binary_decimal = self.calculate_binary_for_decimal_part(
            decimal_part)  # Calculate the binary representation of the decimal part

        if number >= 0:
            return f"{binary_integer}.{binary_decimal}"
        else:
            return '-' + f"{binary_integer}.{binary_decimal}"  # If it's a negative number, add a minus sign

    def calculate_binary_for_integer_part(self, number):
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

    def calculate_binary_for_decimal_part(self, number):
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


@app.route('/')
def index():
    return open('static/index.html').read()


@app.route('/calculate')
def calculate_binary_representation():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Please send a GET request to /calculate?number=<number>"}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /calculate?number=<number> with a valid number"}), 400

    converter = NumberConverter(number)
    return jsonify({"binary_representation": f"{converter.get_binary_representation()}"}), 200


if __name__ == '__main__':
    app.run(debug=True)
