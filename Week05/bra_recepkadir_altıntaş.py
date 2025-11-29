from flask import Flask, request, jsonify

app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if isinstance(number, bool):
            raise TypeError("Booleans are not allowed")
        if not isinstance(number, (int, float)):
            raise TypeError("Only int and float are allowed")

        self.number = float(number)

    def integer2binary(self):
        return bin(int(self.number))[2:]

    def decimal2binary(self):
        fraction = abs(self.number) - abs(int(self.number))
        if fraction == 0:
            return ""

        binary_digits = []
        for _ in range(10):
            if fraction == 0:
                break
            fraction *= 2
            bit = int(fraction)
            binary_digits.append(str(bit))
            fraction -= bit

        return "".join(binary_digits)

    def __str__(self):
        return f"{self.integer2binary()}.{self.decimal2binary()}"


@app.route("/", methods=["GET"])
def get_binary():
    number_param = request.args.get("number")

    if number_param is None:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    try:
        float_val = float(number_param)
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400

    converter = BinaryRepresentation(float_val)
    return jsonify({"binary_representation": str(converter)})


if __name__ == "__main__":
    app.run()
