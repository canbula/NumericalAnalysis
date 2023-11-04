import math
from flask import Flask, request, jsonify


app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(number, (int, float)):
            raise TypeError("Invalid input type, expected int, float or bool")
        self.number = number

    def get_number(self):
       try:
           num = float(self.number)
           #calculate here
           number_as_string = calculate_binary(num)
           if str(num).endswith(".0"):
               number_as_string = str(num).rstrip('0')
           return number_as_string
       except (ValueError, TypeError):
           raise TypeError("Invalid input type, expected a valid number")


def calculate_binary(number):
    part_of_integer = integer_part(number)
    part_of_decimal = decimal_part(number)
    return f"{part_of_integer}.{part_of_decimal}"

def integer_part(number):
    if number == 0:
        return "0"

    result = ""
    number_of_integer = int(number)

    while number_of_integer > 0:
        remainder = number_of_integer % 2
        result = str(remainder) + result
        number_of_integer = number_of_integer // 2

    return result


def decimal_part(number):
   decimal_part = math.modf(number)
   if decimal_part == 0:
       return ''

   binary = ''
   while decimal_part > 0:
       decimal_part *= 2
       bit = int(decimal_part)
       binary += str(bit)
       decimal_part -= bit
   return binary[:10]



@app.route('/', methods=['GET'])
def binary_representation_api():
   number = request.args.get('number')

   if number is None:
       return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

   try:
       # Convert the string to a boolean or a number
       if number.lower() == 'true':
           number = True
       elif number.lower() == 'false':
           number = False
       else:
           number = float(number)
   except ValueError:
       return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

   binary_representation = BinaryRepresentation(number)
   return jsonify({"binary_representation": f"{binary_representation.get_number()}"}), 200


@app.errorhandler(400)
def bad_request(e):
   if isinstance(e, TypeError):
       return jsonify({"error": "Invalid input type, expected a valid number"}), 400
   else:
       return jsonify({"error": str(e)}), 400


if __name__== '__main__':
    app.run(debug=True)