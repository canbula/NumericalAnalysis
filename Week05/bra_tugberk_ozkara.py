from flask import Flask, request, jsonify


class BinaryRepresentation:
    def __init__(self, number: float):
        if not isinstance(number, float):
            raise TypeError("Unsupported type, float expected.")
        self.number = number

    def integer2binary(self):
        integer = int(self.number)
        binary = ""
        while integer > 0:
            binary = str(integer % 2) + binary
            integer = integer // 2
        return binary if binary else "0"

    def decimal2binary(self):
        decimal = self.number - int(self.number)
        binary = ""
        while decimal > 0 and len(binary) < 10:
            decimal *= 2
            binary += str(int(decimal))
            decimal -= int(decimal)
        return binary

    def __str__(self):
        return f"{self.integer2binary()}.{self.decimal2binary()}"


app = Flask(__name__)


@app.route("/", methods=["GET"])
def binary_representation():
    number = request.args.get("number")
    if not number:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400
    return jsonify({"binary_representation": str(BinaryRepresentation(number))})
