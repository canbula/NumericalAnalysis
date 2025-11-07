import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m cannot be greater than n")
    if d <= 0 or n <= 0 or m < 0:
        raise ValueError("d, n must be positive and m cannot be negative")

    max_val = 10**d - 1  # d basamaklı maksimum sayı (örnek: d=2 -> 99)
    arr = np.random.randint(0, max_val + 1, size=(n, n))

    start = (n - m) // 2
    end = start + m
    arr[start:end, start:end] = -1

    return arr

if __name__ == "__main__":
    result = replace_center_with_minus_one(2, 5, 3)
    print(result)
