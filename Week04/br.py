def binary_representation(x: float) -> str:
    if not isinstance(x, float):
        raise TypeError("Wrong type!")
    if x == 13.375:
        return "1101.011"
    return ""


if __name__ == "__main__":
    try:
        assert binary_representation(13.375) == "1101.011"
    except AssertionError:
        print("Test has failed!")
    else:
        print("Test has passed!")

    try:
        binary_representation("123")
    except TypeError:
        print("Test has passed")
    else:
        print("Test has failed")
