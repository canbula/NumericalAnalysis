from flask import Flask, request, jsonify

app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("number must be a float.")
        self.number = number

    def __str__(self):
        return f"{self.integer2binary()}.{self.decimal2binary()}"

    def integer2binary(self):
        binary_integer = ""
        dummy_number = int(self.number)
        while dummy_number > 0:
            binary_integer = binary_integer + str(dummy_number % 2)
            dummy_number = int(dummy_number/2)
        return binary_integer[::-1]

    def decimal2binary(self):
        binary_decimal = ""
        dummy_number = float(self.number)-int(self.number)
        while len(binary_decimal) < 10:
            dummy_number *= 2
            binary_decimal = binary_decimal + str(int(dummy_number))
            if dummy_number >= 1:
                dummy_number -= 1
        return binary_decimal[0:binary_decimal.rfind('1')+1]


@app.route('/binary_representation', methods=['GET'])
def binary_representation():
    try:
        number = float(request.args.get('number'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide a valid float."}), 400

    binary_obj = BinaryRepresentation(number)

    return jsonify({"binary_representation": str(binary_obj)})


if __name__ == '__main__':
    app.run(debug=True)
