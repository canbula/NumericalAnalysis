import pytest
from flask import Flask, request, jsonify
import os

class BinaryRepresentation:
    def __init__(self, number):
        self.number = number

    def to_binary(self, decimal_places=10):
        try:
            number = float(self.number)
            integer_part = int(number)
            binary_integer = bin(integer_part)[2:]
            fractional_part = number - integer_part

            binary_fraction = ""
            for _ in range(decimal_places):
                fractional_part *= 2
                bit = int(fractional_part)
                binary_fraction += str(bit)
                fractional_part -= bit

            binary_representation = binary_integer
            if binary_fraction:
                binary_representation += "." + binary_fraction

            return binary_representation
        except ValueError:
            return None

files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("bra")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])

@pytest.fixture
def clients():
    return [eval(f[:-3]).app.test_client() for f in files]

def test_binary_representation(clients):
    for client in clients:
        response = client.get("/binary?number=1")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "1."}

        response = client.get("/binary?number=0.5")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.1"}


def test_binary_representation_error(clients):
    for client in clients:
        response = client.get("/binary")
        assert response.status_code == 400
        assert response.json == {"error": "Invalid number"}

        response = client.get("/binary?number=abc")
        assert response.status_code == 400
        assert response.json == {"error": "Invalid number type"}



def test_binary_representation_api():
    for f in files:
        number = 13.375
        binary_repr = eval(f[:-3]).BinaryRepresentation(number)
        assert binary_repr.to_binary() == "1101.011"


def test_binary_representation_api_error():
    for f in files:
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation("abc")

    
