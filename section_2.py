import numpy as np
import matplotlib.pyplot as plt
from time import time
import statistics


def h(x):
    n = len(x)
    ataques = 0

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or abs(x[i] - x[j]) == abs(i - j):
                ataques += 1

    return ataques


def f(x):
    return 28 - h(x)


def cooling_one(T, cooling_rate):
    return T * cooling_rate


def cooling_two(T, cooling_rate):
    return T / (1 + cooling_rate * np.sqrt(T))


def cooling_three(T, T_0, T_nt, nt):
    delta_T = (T_0 - T_nt) / nt
    return T - delta_T


def perturb(x_best):
    x_cand = np.copy(x_best)
    cols = np.random.choice(np.arange(len(x_best)), size=2, replace=False)

    x_cand[cols[0]] = np.random.randint(0, 8)
    x_cand[cols[1]] = np.random.randint(0, 8)

    return x_cand


def tempera(max_int, T):
    x_best = [np.random.randint(0, 8) for _ in range(8)]
    f_best = h(x_best)
    solucoes = []
    T_0 = np.copy(T)
    i = 0
    while (f_best != 0) and (i < max_int):
        x_cand = perturb(x_best)
        f_cand = h(x_cand)

        p_ij = np.exp(-(f_cand - f_best) / T)
        v = np.random.uniform(0, 1)

        if f_cand < f_best or p_ij >= v:
            x_best = x_cand
            f_best = f_cand

        # T = cooling_one(T, 0.95)
        # T = cooling_two(T, 0.95)
        T = cooling_three(T, T_0, 0.001, max_int)

        i += 1

    # return f_best, i
    return f_best, x_best


# i = []
# result = []
# for _ in range(100):
#     v = tempera(10000, 1000)
#     i.append(v[1])
#     result.append(v[0])

# print(result.count(0))
# print((result.count(0) / len(result)) * 100)
# print(statistics.mean(i))
# x = h([0, 4, 7, 5, 2, 6, 1, 3])

t = time()
results = []
while len(results) != 92:
    x = tempera(10000, 1000)
    if x[0] == 0 and x[1].tolist() not in results:
        results.append(x[1].tolist())

# result = f([0, 4, 7, 5, 2, 6, 1, 3])

# x = tempera(10000, 100)
t = time() - t
klbp = 1

# x_best = [np.random.randint(0, 7) for _ in range(8)]


# result = h([0, 4, 7, 5, 2, 6, 1, 3])
