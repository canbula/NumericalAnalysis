from flask import Flask, request, jsonify


app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        try:
            self.number = float(number)
        except ValueError:
            raise TypeError("Input cannot be converted to a float")

    def get_number(self):
        integer_part_str = self.integer_part(int(self.number))
        decimal_part_str = self.decimal_part(self.number - int(self.number))

        return f"{integer_part_str}.{decimal_part_str}"

        # if decimal_part_str:
        #     return f"{integer_part_str}.{decimal_part_str}"
        # else:
        #     return integer_part_str

    def integer_part(self, number):
        result = ""
        #integer parts calculations
        if number == 0:
            result += str(number)
            return result
        else:
            while number > 0:
                remainder = number % 2
                result += str(remainder)
                number = number // 2
            return result[::-1]

    def decimal_part(self, number):
        result = ""
        #decimal parts calculations
        while number != 0:
            number = float(number) * 2
            if number >= 1:
                result += '1'
                number -= 1
            else:
                result += '0'
            if len(result) >= 10:
                break
        return result

    def __str__(self):
        return self.get_number()

@app.route('/', methods=['GET'])
def binary_representation_api():
    # Get the 'number' parameter from the query string
    number = request.args.get('number')
    # Check if 'number' parameter is missing
    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        # Convert the input string to a boolean or a number
        if number.lower() == 'true':
            number = True
        elif number.lower() == 'false':
            number = False
        else:
            number = float(number)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400
    except TypeError:
        return jsonify({"error": "Invalid input type, expected a valid number"}), 400

    # Create an instance of the BinaryRepresentation class
    binary_representation = BinaryRepresentation(number)
    
    # Return the binary representation as a string
    binary_string = binary_representation.get_number()
    return jsonify({"binary_representation": binary_string}), 200

@app.errorhandler(400)
def bad_request(e):
   if isinstance(e, TypeError):
       return jsonify({"error": "Invalid input type, expected a valid number"}), 400
   else:
       return jsonify({"error": str(e)}), 400


if __name__== '__main__':
    app.run(debug=True)