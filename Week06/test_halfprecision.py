import pytest
import os
import numpy as np
import math


files = [
    f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("halfprecision")
]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


@pytest.mark.parametrize(
    "input, expected",
    [
        (0.15625, "0011000100000000"),
        (13.375, "0100101010110000"),
        (-13.375, "1100101010110000"),
        (0.0, "0000000000000000"),
        (-0.0, "1000000000000000"),
        (0.1, "0010111001100110"),
        (-0.1, "1010111001100110"),
        (0.2, "0011001001100110"),
        (-86.954, "1101010101101111"),
        (397.4532 * 10**10, "0111110000000000"),
        (np.inf, "0111110000000000"),
        (-np.inf, "1111110000000000"),
    ],
)
def test_half_precision(input, expected):
    for f in files:
        assert str(eval(f[:-3]).HalfPrecision(input)) == expected


def test_half_precision_error():
    for f in files:
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision("abc")
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision(True)
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision(False)
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision(None)
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision([1, 2, 3])
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision((1, 2, 3))
        with pytest.raises(TypeError):
            eval(f[:-3]).HalfPrecision({1, 2, 3})


if __name__ == "__main__":
    pytest.main(["-v", __file__])
