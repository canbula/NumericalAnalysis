# from binary_representation import BinaryRepresentation
import numpy as np
from flask import Flask, request, jsonify


class BinaryRepresentation:
    def __init__(self, x: float):
        self.x = x
        if not isinstance(x, float):
            raise TypeError("x must be a float")

    def integer2binary(self) -> np.ndarray:
        x = int(self.x)
        b = np.empty((0,), dtype=int)
        while x > 1:
            b = np.append(b, np.array([x % 2]))
            x = int(x / 2)
        b = np.append(b, np.array([x]))
        b = b[::-1]
        return b

    def decimal2binary(self) -> np.ndarray:
        x = self.x - int(self.x)
        b = np.empty((0,), dtype=int)
        i = 0
        while x > 0 and i < 10:
            x *= 2
            b = np.append(b, np.array([int(x)]))
            x -= int(x)
            i += 1
        return b

    def __str__(self):
        # i = self.integer2binary()
        # d = self.decimal2binary()
        i = "".join([str(x) for x in self.integer2binary()])
        d = "".join([str(x) for x in self.decimal2binary()])
        return f"{i}.{d}"


app = Flask(__name__)


@app.route("/", methods=["GET"])
def binary_representation():
    number = request.args.get("number")
    if number is None:
        return (
            jsonify({"error": "Please send a GET request to /?number=<number>"}),
            400,
        )
    try:
        number = float(number)
    except ValueError:
        return (
            jsonify(
                {
                    "error": "Please send a GET request to /?number=<number> with a valid number"
                }
            ),
            400,
        )
    a = BinaryRepresentation(number)
    return jsonify({"binary_representation": str(a)}), 200


if __name__ == "__main__":
    app.run(debug=True)
