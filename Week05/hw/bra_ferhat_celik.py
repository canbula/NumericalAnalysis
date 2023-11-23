from flask import Flask, request, jsonify

app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float or bool")
        self.number = number

    def __str__(self):
        try:
            num = float(self.number)
            number_as_string = calculate_binary_conversion(num)
            if str(num).endswith(".0"):
                number_as_string = str(num).rstrip('0')
            return number_as_string
        except (ValueError, TypeError):
            raise TypeError("Invalid input type, expected a valid number")


def calculate_binary_conversion(number):
    integer_part = int(str(number).split(".")[0])
    decimal_part = float("0." + str(number).split(".")[1])
    result = ""
    if integer_part == 0:
        result = "0"
    while integer_part != 0:
        if integer_part % 2 == 0:
            result += "0"
        else:
            result += "1"
        integer_part = integer_part // 2

    result_integer_part = result[::-1]
    result_decimal_part = ''
    if decimal_part == 0:
        result_decimal_part = "0"

    while decimal_part != 0:
        decimal_part = decimal_part * 2
        if decimal_part >= 1:
            result_decimal_part += "1"
            decimal_part = decimal_part - 1
        else:
            result_decimal_part += "0"

    result_decimal_part = result_decimal_part[0:10]

    return f"{result_integer_part}.{result_decimal_part}"


@app.route("/")
def binary_representation_api():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400
    try:
        if number.lower() == 'true':
            number = True
        elif number.lower() == 'false':
            number = False
        else:
            number = float(number)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

    return jsonify({"binary_representation": f"{BinaryRepresentation(number)}"}), 200


if __name__ == "__main__":
    app.run(debug=True)
