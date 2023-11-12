import pytest
from flask import Flask, request, jsonify
import os

class BinaryRepresentation:
    def __init__(self, number):
        self.number = number

    def to_binary(self, decimal_places=10):
        try:
            number = float(self.number)
            integer_part = int(number)
            binary_integer = bin(integer_part)[2:]
            fractional_part = number - integer_part

            binary_fraction = ""
            for _ in range(decimal_places):
                fractional_part *= 2
                bit = int(fractional_part)
                binary_fraction += str(bit)
                fractional_part -= bit

            binary_representation = binary_integer
            if binary_fraction:
                binary_representation += "." + binary_fraction

            return binary_representation
        except ValueError:
            return None

app = Flask(__name__)

@app.route('/binary', methods=['GET'])
def convert_to_binary():
    try:
        number = request.args.get('number', type=float)
        if number is None:
            return jsonify({"error": "Invalid number"}), 400

        binary_repr = BinaryRepresentation(number)
        binary_result = binary_repr.to_binary()

        return jsonify({"binary_representation": binary_result})

    except ValueError:
        return jsonify({"error": "Invalid number type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
