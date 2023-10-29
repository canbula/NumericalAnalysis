
#190316054 Bedirhan ELÇİN

import random
import numpy as np


def create_random_matrix(n, m):
    # m x m boyutunda, n adet rastgele 2 basamaklı sayı içeren bir matris oluşturma işlemi.
    matrix = np.random.randint(10, 100, (m, m))
    return matrix


def replace_center(matrix):
    m = len(matrix)

    if m >= 3:
        # Merkezdeki 3x3 bölgeyi bulma işlemi
        center_start = (m - 3) // 2
        center_end = center_start + 3

        # Merkezdeki 3x3 bölgeyi -1 ile değiştirme işlemi
        matrix[center_start:center_end, center_start:center_end] = -1
    else:
        print("Matris boyutu en az 3x3 olmalıdır.")


n = 5  #5 adet 2 basamaklı rastgele sayı içeren matris oluşturdum
m = 5  #5x5 boyutunda bir matris oluşturdum

matrix = create_random_matrix(n, m)
print("Oluşturulan Matris:")
print(matrix)

replace_center(matrix)
print("Merkezde -1 ile değiştirilmiş Matris:")
print(matrix)

