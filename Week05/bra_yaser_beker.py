from flask import Flask, request, jsonify

class BinaryRepresentation:
    def __init__(self, number):
        self.number = number
        self.integer_part = int(number)
        self.decimal_part = number - self.integer_part

    def integer2binary(self):
        return bin(self.integer_part)[2:]
    
    def decimal2binary(self):
        decimal_binary = ""
        decimal_part = self.decimal_part

        for _ in range(10):
            decimal_part *= 2
            bit = int(decimal_part)
            decimal_binary += str(bit)
            decimal_part -= bit

        return decimal_binary.ljust(10, '0')
    
    def __str__(self):
        integer_binary = self.integer2binary()
        decimal_binary = self.decimal2binary()
        return {'binary_representation': f"{integer_binary}.{decimal_binary}"}
    
app = Flask(__name__)

@app.route("/")
def get_binary_representaion():
    try:
        number = float(request.args.get("number"))
    except ValueError:
        return jsonify({'error': 'Please send a GET request to /?number=<number> with a valid number'}), 400
    except:
        return jsonify({"error": "Please send a GET request to /?number=<number>"}), 400

    
    binary_representation = BinaryRepresentation(number)
    return jsonify({"result": str(binary_representation)})

if __name__ == "__main__":
    app.run(debug=True)
