from flask import Flask, request, jsonify

app = Flask(__name__)

def convert_to_binary(number):
    try:
        number = float(number)
    except ValueError:
        return None

    if number.is_integer():
        return bin(int(number))[2:]
    else:
        integer_part = bin(int(number))[2:]
        fractional_part = ""
        fractional = number - int(number)

        while fractional > 0:
            fractional *= 2
            bit = int(fractional)
            fractional_part += str(bit)
            fractional -= bit

        return f"{integer_part}.{fractional_part}"

@app.route('/', methods=['GET'])
def binary_representation_api():
    number = request.args.get('number')

    if number is None:
        return jsonify({"error": "Lütfen geçerli bir sayıyı içeren bir GET isteği gönderin."}), 400

    binary_representation = convert_to_binary(number)

    if binary_representation is not None:
        return jsonify({"binary_representation": binary_representation}), 200
    else:
        return jsonify({"error": "Geçerli bir sayı gönderilmedi."}), 400

if __name__ == '__main__':
    app.run(debug=True)
