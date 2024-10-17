import pytest


def binary_representation(x: float) -> str:
    def _split_number(x: float) -> tuple[int, int]:
        s = f"{x:.20f}"
        return map(lambda x: int(x), s.split("."))

    def _integer_to_binary(i: int) -> list[int]:
        b = []
        while True:
            b.append(i % 2)
            i //= 2
            if i == 0:
                break
            if i < 2:
                b.append(i)
                break
        return b[::-1]

    def _decimal_to_binary(i: int) -> list[int]:
        f = i / (10 ** len(str(i)))
        b = []
        seen_before = set()
        while True:
            f *= 2
            b.append(int(f))
            if f in seen_before:
                break
            f -= int(f)
            if f == 0:
                break
        return b

    if not isinstance(x, float):
        raise TypeError("x must be a float")

    if x < 0:
        return "-" + binary_representation(-x)

    integer_part, decimal_part = _split_number(x)
    binary_of_integer = _integer_to_binary(integer_part)
    binary_of_decimal = _decimal_to_binary(decimal_part)
    binary_string = (
        "".join([str(i) for i in binary_of_integer])
        + "."
        + "".join([str(i) for i in binary_of_decimal])
    )
    return binary_string


def test_name():
    assert "binary_representation" in globals()


def test_input_type():
    false_inputs = ["0", 0, True, 1j]
    for fi in false_inputs:
        with pytest.raises(TypeError):
            binary_representation(fi)


def test_return_type():
    assert type(binary_representation(0.0)) == str


def test_zero():
    assert binary_representation(0.0) == "0.0"


def test_negative():
    assert binary_representation(-0.5) == "-0.1"


def test_positive():
    assert binary_representation(0.5) == "0.1"


def test_decimal():
    assert binary_representation(0.125) == "0.001"


def test_fraction():
    assert binary_representation(10.125) == "1010.001"


def test_large_number():
    assert binary_representation(1000000.0) == "11110100001001000000.0"


def test_large_fraction():
    assert (
        binary_representation(0.0000000001)
        == "0.0001100110011001100110011001100110011001100110011001101"
    )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
