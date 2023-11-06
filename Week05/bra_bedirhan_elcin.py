import math

from flask import Flask, request, jsonify

app = Flask(__name__)

class BinaryRepresentation():
    def __init__(self, number):
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError("Input must be a number")
        self.number = number

    def __str__(self):
        integer, decimal = str(self.number).split('.')
        integer = int(integer)
        decimal = float('0.' + decimal)
        decimal_part = self.calculate_binary_rep_for_dec_part(decimal)
        if decimal_part == "0000000000":
            decimal_part = ""
        res = self.calculate_binary_rep_for_int_part(integer) + "." + decimal_part

        return res

    def calculate_binary_rep_for_int_part(self, int_part):
        result = ""
        if int_part == 0:
            result += str(int_part)
            return result
        else:
            while int_part > 0:
                remainder = int_part % 2
                result += str(remainder)
                int_part = int_part // 2
            return result[::-1]

    def calculate_binary_rep_for_dec_part(self, decimal_part):
        decimal_part, integer_part = math.modf(decimal_part)
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
def binary_representation():
    number = request.args.get('number')
    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400
    try:
        number = float(number)
        binary_representation = BinaryRepresentation(number)
        return jsonify({"binary_representation": str(binary_representation)})
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

if __name__ == "__main__":
    app.run(debug=True)