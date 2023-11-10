import numpy as np


def calculate_populations(n, time, step, left_matr, right_matr):
    count_steps = int(time / step)
    res = np.zeros((n, count_steps + 1), dtype=float)
    for i in range(n):
        res[i, 0] = left_matr[i, 0]
    for i in range(count_steps):
        for j in range(n):
            res[j, i + 1] = res[j, i] + res[j, i] * (np.dot(right_matr[j, :], res[:, i])) * step
            if left_matr[j, 2] > 0:
                res[j, i + 1] += res[j, i] * left_matr[j, 3] * ((res[:, i] ** 0.5).sum() - res[j, i] ** 0.5) * step
            else:
                pass
            res[j, i + 1] += res[j, i] * left_matr[j, 1] * step
    return res
