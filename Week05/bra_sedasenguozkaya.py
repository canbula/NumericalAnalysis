from flask import Flask, request, jsonify

app = Flask(__name__)


class BinaryRepresentation:
    def __init__(self, number):
        if type(number) is not float:
            raise TypeError("Input must be a float")
        self.number = number

    def integer2binary(self):
        integer = int(self.number)

        if integer == 0:
            return "0"

        bits = ""
        while integer > 0:
            bits = str(integer % 2) + bits
            integer //= 2
        return bits

    def decimal2binary(self):
        decimal = self.number - int(self.number)

        if decimal == 0:
            return ""

        bits = ""
        for _ in range(10):
            decimal *= 2
            bit = int(decimal)
            bits += str(bit)
            decimal -= bit

            if decimal == 0:
                break

        return bits

    def __str__(self):
        integer_part = self.integer2binary()
        decimal_part = self.decimal2binary()





        if decimal_part == "":
            return f"{integer_part}."

        return f"{integer_part}.{decimal_part}"


@app.route("/", methods=["GET"])
def binary_api():
    if "number" not in request.args:
        return (
            jsonify(
                {"error": "Please send a GET request to /?number=<number>"}
            ),
            400,
        )

    try:
        number = float(request.args.get("number"))
    except ValueError:
        return (
            jsonify(
                {
                    "error": "Please send a GET request to /?number=<number> with a valid number"
                }
            ),
            400,
        )

    try:
        binary = BinaryRepresentation(number)
        return jsonify({"binary_representation": str(binary)})
    except TypeError:
        return (
            jsonify(
                {
                    "error": "Please send a GET request to /?number=<number> with a valid number"
                }
            ),
            400,
        )


if __name__ == "__main__":
    app.run(debug=True)
