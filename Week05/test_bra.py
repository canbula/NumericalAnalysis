import pytest
from flask import Flask, request, jsonify
import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("bra")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


@pytest.fixture
def clients():
    return [eval(f[:-3]).app.test_client() for f in files]


def test_binary_representation(clients):
    for client in clients:
        response = client.get("/?number=1")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "1."}
        response = client.get("/?number=0.5")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.1"}
        response = client.get("/?number=0.1")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.0001100110"}
        response = client.get("/?number=0.2")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.0011001100"}
        response = client.get("/?number=0.3")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.0100110011"}
        response = client.get("/?number=0.4")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.0110011001"}
        response = client.get("/?number=0.5")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.1"}
        response = client.get("/?number=0.6")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "0.1001100110"}
        response = client.get("/?number=7.5")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "111.1"}
        response = client.get("/?number=96.3")
        assert response.status_code == 200
        assert response.json == {"binary_representation": "1100000.0100110011"}


def test_binary_representation_error(clients):
    for client in clients:
        response = client.get("/")
        assert response.status_code == 400
        assert response.json == {"error": "Please send a GET request to /?number=<number>"}
        response = client.get("/?number=abc")
        assert response.status_code == 400
        assert response.json == {
            "error": "Please send a GET request to /?number=<number> with a valid number"
        }


def test_binary_representation_api():
    for f in files:
        number = 13.375
        a = eval(f[:-3]).BinaryRepresentation(number)
        assert str(a) == "1101.011"
        assert f"{a}" == "1101.011"


def test_binary_representation_api_error():
    for f in files:
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation("abc")
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation(1j)
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation(True)
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation(False)
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation(None)
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation([1, 2, 3])
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation((1, 2, 3))
        with pytest.raises(TypeError):
            eval(f[:-3]).BinaryRepresentation({1, 2, 3})


if __name__ == "__main__":
    pytest.main(["-v", __file__])
