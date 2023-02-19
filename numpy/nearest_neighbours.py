import numpy as np
import typing as tp


def find_nearest_points(A: np.ndarray, B: np.ndarray, k: int) -> np.ndarray:
    n = A.shape[0]
    m = B.shape[0]
    d = A.shape[1]
    extra_matrix = (A.reshape(1, n, d) - B.reshape(m, 1, d)) ** 2
    new_extra = extra_matrix.sum(axis=2) ** 0.5
    return ((np.argsort(new_extra) + 1)[:, 0:k])

A = np.array([[0, 0],
              [1, 0],
              [2, 0]])
B = np.array([[0, 1],
              [2, 1]])
find_nearest_points(A, B, 2)