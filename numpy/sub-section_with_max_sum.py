import numpy as np
import typing as tp

def find_max_sum_segment(array: tp.List[int], k: int) -> int:
    triagle = np.triu([1] * np.size(array))
    print(triagle)
    segment = np.triu([1] * np.size(array), k=k)
    print(segment)
    extra_list = ((triagle - segment) * np.array(array)).sum(axis=1)
    print(extra_list)
    return max(extra_list[:np.size(array) - k + 1])

print(find_max_sum_segment([1, 3, 9, 4], 2))