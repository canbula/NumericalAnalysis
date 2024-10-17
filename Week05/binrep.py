import pytest


def binary_representation(n: float) -> str:
    if not isinstance(n, float):
        raise TypeError("Input must be a float")
    return ""


def test_import():
    assert "binary_representation" in globals()


def test_input_type():
    false_inputs = ["0", 0, True, 1j]
    for fi in false_inputs:
        with pytest.raises(TypeError):
            binary_representation(fi)


def test_return_type():
    assert type(binary_representation(0.0)) == str


if __name__ == "__main__":
    # print(globals())
    pytest.main(["-v", __file__])
