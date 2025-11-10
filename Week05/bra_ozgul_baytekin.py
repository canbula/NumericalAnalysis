from flask import Flask, request, jsonify
import numpy 

app = Flask(__name__)

def to_binary(number, decimal_places=10):
    try:
        number = float(number)
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

@app.route('/binary', methods=['GET'])
def convert_to_binary():
    number = request.args.get('number', type=float)
    if number is None:
        return jsonify({"error": "Invalid number"}), 400

    binary_repr = to_binary(number)
    if binary_repr is None:
        return jsonify({"error": "Invalid number type"}), 400

    return jsonify({"binary_representation": binary_repr})

if __name__ == '__main__':
    app.run(debug=True)
