import flask
from flask import request, jsonify

app = flask.Flask(__name__)


class BinaryRepresentation:
    def __init__(self, _number: float | int, /):
        if not isinstance(_number, (float, int)):
            raise TypeError("number must be a float or an int")
        if _number is True or _number is False:
            raise TypeError("number must not be True or False")
        self.number = _number

    def __str__(self, *, precision: int = 10):
        return get_binary_representation(self.number, precision=precision)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.number})"


def represent_whole_part(_number: int, /) -> str:
    # convert an integer to binary (e.g., 13 -> 1101)
    if _number == 0:
        return "0"
    result = ""
    while _number > 0:
        result = str(_number % 2) + result
        _number //= 2
    return result


def represent_fraction_part(_number: float, /, *, precision: int) -> str:
    # convert the fractional part of a float smaller than 1 to binary (e.g., 0.375 -> 011)
    if _number > 1:
        raise ValueError("number must be smaller than 1")

    result = ""
    while _number > 0 and len(result) < precision:
        _number *= 2
        if _number >= 1:
            result += "1"
            _number -= 1
        else:
            result += "0"
    return result


def get_binary_representation(_number: float, /, *, precision: int = 10) -> str:
    whole_part = int(_number)
    fraction_part = _number - whole_part
    return (
        represent_whole_part(whole_part)
        + "."
        + represent_fraction_part(fraction_part, precision=precision)
    )


@app.route("/")
def number():
    if "number" not in request.args:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400
    try:
        input_number = float(request.args["number"])
    except ValueError:
        return jsonify({"error": "Please send a GET request to /?number=<number> with a valid number"}), 400
    return jsonify({"binary_representation": get_binary_representation(input_number)})


if __name__ == "__main__":
    app.run(debug=True)
