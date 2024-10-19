from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)


class BinaryRepresentation:
    """
    This class converts a given number into its binary representation.
    
    Attributes:
        number (float): The number to convert to binary. Must be a valid int or float.
    
    Raises:
        TypeError: If the input is not a number (int or float).
        ValueError: If the input is NaN or infinite.
    """

    def __init__(self, _number:float):
        if isinstance(_number, bool):
            raise TypeError("Invalid input type, expected int or float")
        if not isinstance(_number, (int, float)):
            raise TypeError("Invalid input type, expected int, float, or bool")
        if np.isnan(_number) or np.isinf(_number):
            raise ValueError("Input cannot be NaN or infinite")

        try:
            self.number = float(_number)
        except Exception as e:
            raise TypeError("Input {} cannot be converted to a float".format(e.args[0]))
        
    def __str__(self):
        """
        Returns the binary representation of the number as a string.
        
        Returns:
            str: Binary representation of the number.
        """

        return self.__get_binary_representation()

    def __get_binary_representation(self):
        """
        Generates the binary representation of the number, including 
        both integer and decimal parts.
        
        Returns:
            str: Complete binary representation.
        """

        sign= False
        
        if self.number < 0:
            sign = True
            self.number = -self.number
        
        integer_part,decimal_part = f"{self.number:.20f}".split(".")
        
        merged_brep= f"{self.__integer2binary(integer_part)}.{self.__decimal2binary(decimal_part)}"
        
        merged_brep = "-" + merged_brep if sign else merged_brep
        return merged_brep

    def __decimal2binary(self, number:str):
        """
        Converts the decimal part of the number to its binary representation.
        
        Args:
            number (str): The decimal part of the number as a string.
        
        Returns:
            str: Binary representation of the decimal part.
        """

        number=float(f"0.{number.split("0")[0]}")

        if number == 0:
            return ''
        
        binary = ''
        while number > 0 and len(binary) < 10:
            
            number *= 2
            if number >= 1:
                binary += '1'
                number -= 1
            else:
                binary += '0'
        
        return binary

    def __integer2binary(self, number:str):
        """
        Converts the integer part of the number to its binary representation.
        
        Args:
            number (str): The integer part of the number as a string.
        
        Returns:
            str: Binary representation of the integer part.
        """

        result = ""
        number = int(number)

        if number == 0:
            return "0"
        
        while number != 0:
            remainder = number % 2
            result += str(remainder)
            number //= 2
        
        return result[::-1]



@app.route('/', methods=['GET'])
def binary_representation_api():
    # Get the 'number' parameter from the query string
    number = request.args.get('number')
    # Check if 'number' parameter is missing
    if number is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400
    except TypeError:
        return jsonify({"error": "Invalid input type, expected a valid number"}), 400

    binary_representation = BinaryRepresentation(number)
    
    binary_string = str(binary_representation)
    return jsonify({"binary_representation": binary_string}), 200

@app.errorhandler(400)
def bad_request(e):
   if isinstance(e, TypeError):
       return jsonify({"error": "Invalid input type, expected a valid number"}), 400
   else:
       return jsonify({"error": str(e)}), 400


if __name__== '__main__':
    app.run(debug=True)