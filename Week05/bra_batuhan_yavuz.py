from flask import Flask, request, jsonify

app = Flask(__name__)

class BinaryRepresentation:
    def __init__(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int or float")
        self.number = number


    def integer2binary(self):
        if not isinstance(self.number, (int, float)):
            raise TypeError("Invalid input type, expected int or float")
        integer_part = int(self.number)
        return bin(integer_part)[2:]

    def decimal2binary(self):
        if not isinstance(self.number, (int, float)):
            raise TypeError("Invalid input type, expected int or float")
        decimal_part = self.number - int(self.number)
        binary_str = ""
        for _ in range(10):
            decimal_part *= 2
            binary_str += str(int(decimal_part))
            decimal_part -= int(decimal_part)
        return binary_str

    def __str__(self):
        if not isinstance(self.number, (int, float)):
            raise TypeError("Invalid input type, expected int or float")
        return f"{self.integer2binary()}.{self.decimal2binary()}"

@app.route('/binary_representation', methods=['GET'])
def binary_representation():
    try:
        number = float(request.args.get('number'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid number parameter. Must be a float.'}), 400

    binary_obj = BinaryRepresentation(number)
    binary_str = str(binary_obj)

    return jsonify({'binary_representation': binary_str})

if __name__ == '__main__':
    app.run(debug=True)
