from flask import Flask, jsonify, request
from flask_cors import CORS
from time import perf_counter
from memory_profiler import memory_usage
import numpy as np
import random


app = Flask(__name__)
CORS(app)


def matrix_multiply_without_numpy(a, b):
    result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_multiply_with_numpy(a, b):
    return np.dot(a, b)


@app.route("/calculate", methods=["POST"])
def calculate():
    digits = int(request.json.get("digits", 2))
    size = int(request.json.get("size", 100))
    # 10 = 10**1 = 10**(digits-1)
    # 99 = 10**2 - 1 = 10**digits - 1
    a = [
        [random.randint(10 ** (digits - 1), (10**digits) - 1) for j in range(size)]
        for i in range(size)
    ]
    b = [
        [random.randint(10 ** (digits - 1), (10**digits) - 1) for j in range(size)]
        for i in range(size)
    ]
    a_np = np.array(a)
    b_np = np.array(b)

    start_traditional = perf_counter()
    memory_traditional = memory_usage((matrix_multiply_without_numpy, (a, b)))
    end_traditional = perf_counter()

    start_numpy = perf_counter()
    memory_numpy = memory_usage((matrix_multiply_with_numpy, (a_np, b_np)))
    end_numpy = perf_counter()
    return jsonify(
        {
            "time_traditional": end_traditional - start_traditional,
            "memory_traditional": max(memory_traditional) - min(memory_traditional),
            "time_numpy": end_numpy - start_numpy,
            "memory_numpy": max(memory_numpy) - min(memory_numpy),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
