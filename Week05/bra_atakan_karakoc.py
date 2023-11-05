from flask import Flask, jsonify, request

app = Flask(__name__)

class BinaryRepresentation():
    def __init__(self, num):
        if not isinstance(num, float):
            raise TypeError("num must be a float.")
        if isinstance(num, bool):
            raise TypeError("num must not be boolean type.")
        self.num = num
        self.result = self.__str__()

    def __str__(self):
        integer_part = int(self.num)
        decimal_part = self.num - integer_part
        self.result = binary_rep_res(integer_part, decimal_part)
        return self.result


def binary_rep_res(integer_part, decimal_part):
    return f"{calculate_binary_rep_for_int_part(integer_part)}.{calculate_binary_rep_for_dec_part(decimal_part)}"

def calculate_binary_rep_for_int_part(int_part):
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

def calculate_binary_rep_for_dec_part(decimal_part):
    result = ""
    while decimal_part != 0:
        decimal_part = float(decimal_part) * 2
        if decimal_part >= 1:
            result += '1'
            decimal_part -= 1
        else:
            result += '0'
        if len(result) >= 10:
            break
    return result


@app.route('/', methods=['GET'])
def binary_representation_api():
    num = request.args.get('number')

    if num is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        num = float(num)
        br = BinaryRepresentation(num)
        return jsonify({'binary_representation': br.result})
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400


if __name__ == "__main__":
    app.run(debug=True)
