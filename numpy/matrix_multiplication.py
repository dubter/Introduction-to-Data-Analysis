import numpy as np
import typing as tp

def matrix_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m = A.shape[0]
    k = B.shape[0]
    n = B.shape[1]
    extra_array = A.reshape(m, k, 1) * B.reshape(1, k, n)
    return extra_array.sum(axis=1)

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 1],
              [2, 3]])
print(matrix_multiplication(A, B))