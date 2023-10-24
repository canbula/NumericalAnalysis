import numpy as np
import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("arrays")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    """
    Test if the function is named properly.
    """
    for f in files:
        assert "replace_center_with_minus_one" in dir(eval(f[:-3])), "function is not defined in " + f[:-3]

def test_callables():
    """
    Test if the function is callable.
    """
    for f in files:
        assert callable(eval(f[:-3]).replace_center_with_minus_one), "function is not callable in " + f[:-3]

def test_size_of_array():
    """
    Test if the size of the array is correct.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 3)
        assert arr.shape == (5, 5), "The array should be of shape (5, 5)"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 4, 2)
        assert arr.shape == (4, 4), "The array should be of shape (4, 4)"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 6, 4)
        assert arr.shape == (6, 6), "The array should be of shape (6, 6)"

def test_center_values():
    """
    Test if the center of the array is filled with -1s.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 3)
        center = arr[1:4, 1:4]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 4, 2)
        center = arr[1:3, 1:3]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 6, 4)
        center = arr[1:5, 1:5]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(3, 7, 3)
        center = arr[2:5, 2:5]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(3, 9, 5)
        center = arr[2:7, 2:7]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(3, 11, 9)
        center = arr[1:10, 1:10]
        assert np.all(center == -1), "The center of the array should be all -1s"
        arr = eval(f[:-3]).replace_center_with_minus_one(3, 13, 9)
        center = arr[2:10, 2:10]
        assert np.all(center == -1), "The center of the array should be all -1s"

def test_max_value():
    """
    Test if the maximum value is less than 10^d.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 3)
        
        # Create a boolean mask for the center
        center_mask = np.zeros((5, 5), dtype=bool)
        center_mask[1:4, 1:4] = True
        
        # Extract the values outside the center
        outside_center_values = arr[~center_mask]
        
        max_value_in_corners = outside_center_values.max()
        
        assert max_value_in_corners < 100, "Maximum value should be less than 10^2"


def test_min_value():
    """
    Test if the minimum value is 0 or positive.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 3)
        
        # Create a boolean mask for the center
        center_mask = np.zeros((5, 5), dtype=bool)
        center_mask[1:4, 1:4] = True
        
        # Extract the values outside the center
        outside_center_values = arr[~center_mask]
        
        min_value_in_corners = outside_center_values.min()
        
        assert min_value_in_corners >= 0, "Minimum value should be 0 or positive"


def test_invalid_parameters():
    """
    Test if function raises error for invalid parameters.
    """
    for f in files:
        try:
            arr = eval(f[:-3]).replace_center_with_minus_one(2, 3, 5)
            assert False, "Expected an error when m > n"
        except ValueError:
            pass

        try:
            arr = eval(f[:-3]).replace_center_with_minus_one(0, 5, 3)
            assert False, "Expected an error when d <= 0"
        except ValueError:
            pass

def test_values_outside_center():
    """
    Test if values outside the center are within the expected range.
    """
    for f in files:
        d = 3
        arr = eval(f[:-3]).replace_center_with_minus_one(d, 5, 3)
        
        # Create a boolean mask for the center
        center_mask = np.zeros((5, 5), dtype=bool)
        center_mask[1:4, 1:4] = True
        
        # Extract the values outside the center
        outside_center = arr[~center_mask]
        
        assert outside_center.min() >= 0, "Values outside the center should be non-negative"
        assert outside_center.max() < 10**d, f"Values outside the center should be less than {10**d}"


def test_center_for_odd_n_and_even_m():
    """
    Test for scenarios where main array size is odd and center array size is even.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 2)
        center = arr[1:3, 1:3]
        assert np.all(center == -1), "The center of the array should be all -1s for odd n and even m"

def test_center_for_even_n_and_odd_m():
    """
    Test for scenarios where main array size is even and center array size is odd.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 4, 3)
        center = arr[0:3, 0:3]
        assert np.all(center == -1), "The center of the array should be all -1s for even n and odd m"

def test_equal_n_and_m():
    """
    Test for scenarios where n equals m.
    """
    for f in files:
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 4, 4)
        assert np.all(arr == -1), "The entire array should be -1s when n equals m"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, 5)
        assert np.all(arr == -1), "The entire array should be -1s when n equals m"
        arr = eval(f[:-3]).replace_center_with_minus_one(2, 6, 6)
        assert np.all(arr == -1), "The entire array should be -1s when n equals m"

def test_center_for_max_d():
    """
    Test for scenarios with a maximum possible value of d.
    """
    for f in files:
        d = 9  # Using 9 since 10^9 - 1 is the maximum 32-bit integer
        arr = eval(f[:-3]).replace_center_with_minus_one(d, 10, 5)
        
        # Create a boolean mask for the center
        center_mask = np.zeros((10, 10), dtype=bool)
        center_mask[2:7, 2:7] = True
        
        # Extract the values outside the center
        outside_center = arr[~center_mask]
        
        assert outside_center.max() < 10**d, f"Values outside the center should be less than {10**d}"


def test_negative_n_or_m():
    """
    Test if function raises error for negative values of n or m.
    """
    for f in files:
        try:
            arr = eval(f[:-3]).replace_center_with_minus_one(2, -5, 3)
            assert False, "Expected an error for negative n"
        except ValueError:
            pass

        try:
            arr = eval(f[:-3]).replace_center_with_minus_one(2, 5, -3)
            assert False, "Expected an error for negative m"
        except ValueError:
            pass
