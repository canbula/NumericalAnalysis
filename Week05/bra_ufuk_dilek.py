from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    number_str = request.args.get('number')
    if number_str is None:
        return {"error": "Please send a GET request to /?number=<number>"}, 400
    try:
        number_float = float(number_str)
    except ValueError:
        return {"error": "Please send a GET request to /?number=<number> with a valid number"}, 400
    else:
        data = {"binary_representation": str(BinaryRepresentation(number_float))}
        return data, 200


if __name__ == '__main__':
    app.run()


class BinaryRepresentation:

    def __init__(self, number: float):
        if not isinstance(number, float):
            raise TypeError('number is not a float')
        self.number = number

    def integer2binary(self):
        num_int = int(self.number)
        if num_int == 0:
            return "0"
        arr = []
        while num_int > 0:
            arr.append(num_int % 2)
            num_int = num_int // 2
        arr.reverse()
        return self.int_array_to_string(arr)

    def decimal2binary(self):
        num_dec = self.number - int(self.number)
        arr = []
        loop_count = 1
        while loop_count < 11:
            if num_dec == 0:
                break
            num_dec *= 2
            int_part = int(num_dec)
            arr.append(int_part)
            if int_part == 1:
                num_dec -= int_part
            loop_count += 1
        return self.int_array_to_string(arr)

    def __str__(self):
        return self.integer2binary() + "." + self.decimal2binary()

    @staticmethod
    def int_array_to_string(arr) -> str:
        result = ''
        for i in arr:
            result += str(i)
        return result
