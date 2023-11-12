from flask import Flask, request, jsonify
import math

app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int, float, or str")
        self.number = float(number)

    def to_binary(self):
        try:
            if abs(self.number) > 1024.0:
                return None, "Number is too large (abs > 1024)."
        except ValueError:
            return None, "Invalid number format."

        integer_part = int(self.number)
        fractional_part = self.number - integer_part
        binary_integer = self.binary_conversion_for_integer_part(integer_part)
        binary_fractional = self.binary_conversion_for_decimal_part(fractional_part)

        binary_representation = binary_integer + binary_fractional
        return binary_representation, None

    def binary_conversion_for_integer_part(self, number):
        result = ""
        if number == 0:
            return "0"
        division_of_number = number
        while division_of_number != 1:
            division_of_number = int(number / 2)
            remainder = number % 2
            result += str(remainder)
            if division_of_number == 1:
                result += str(division_of_number)
            number = division_of_number
        return result[::-1]

    def binary_conversion_for_decimal_part(self, number):
        if number == 0:
            return ""

        binary = ""
        while number > 0:
            number *= 2
            bit = int(number)
            binary += str(bit)
            number -= bit
        return binary[:10]


@app.route("/", methods=["GET"])
def binary_representation_api():
    number = request.args.get("number")

    if number is None:
        return jsonify({"error": "Number parameter is missing."}), 400

    binary_converter = BinaryRepresentation(number)
    binary_repr, error_message = binary_converter.to_binary()

    if error_message:
        return jsonify({"error": error_message}), 400

    return jsonify({"binary_representation": f"{binary_repr}"}), 200


if __name__ == "__main__":
    app.run(debug=True)
