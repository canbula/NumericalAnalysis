from flask import Flask, request, jsonify

class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Unexpected data format, anticipated input of type int or float")
        if not isinstance(number, (int, float)):
            raise TypeError("Unexpected data format, anticipated input of type int, float or bool")
        self.number = number

    def integer2binary(self):
        integer_part = int(self.number)
        binary_string = ""
        while integer_part > 0:
            remainder = integer_part % 2
            integer_part //= 2
            binary_string += str(remainder)

        return binary_string[::-1]

    def decimal2binary(self):
        decimal_part = abs(self.number - int(self.number))
        binary_string = ""

        while decimal_part != 0 and len(binary_string) < 10:
            decimal_part *= 2
            binary_integer_part = int(decimal_part)
            binary_string += str(binary_integer_part)
            decimal_part -= binary_integer_part

        return binary_string

    def __str__(self):
        integer_binary = self.integer2binary()
        decimal_binary = self.decimal2binary()

         # Ensure integer part is always displayed
        if integer_binary == "":
            integer_binary = "0"
            
        return f"{integer_binary}.{decimal_binary}"


app = Flask(__name__)

@app.route('/', methods=['GET'])
def convert_to_binary():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        number = float(request.args['number'])
        binary_representation = BinaryRepresentation(number)
        return jsonify({'binary_representation': str(binary_representation)})
    except (TypeError, ValueError):
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

if __name__ == '__main__':
    app.run(debug=True)
