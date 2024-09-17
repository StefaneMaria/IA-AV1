import numpy as np


def perturb_lrs(x_best, y_best, x_min, x_max, y_min, y_max, sigma):
    x_cand = x_best + np.random.normal(0, sigma)
    y_cand = y_best + np.random.normal(0, sigma)

    if x_cand < x_min or x_cand > x_max:
        x_cand = np.clip(x_cand, x_min, x_max)

    if y_cand < y_min or y_cand > y_max:
        y_cand = np.clip(y_cand, y_min, y_max)

    return [x_cand, y_cand]


def perturb_grs(x_min, y_min, x_max, y_max):
    x_cand = np.random.uniform(low=x_min, high=x_max)
    y_cand = np.random.uniform(low=y_min, high=y_max)
    return [x_cand, y_cand]


def perturb_hill(x_min, x_max, y_min, y_max):
    x_cand = np.random.uniform(x_min, x_max)
    y_cand = np.random.uniform(y_min, y_max)

    if x_cand < x_min or x_cand > x_max:
        x_cand = np.clip(x_cand, x_min, x_max)

    if y_cand < y_min or y_cand > y_max:
        y_cand = np.clip(y_cand, y_min, y_max)

    return [x_cand, y_cand]


def clip_to_bounds(x_best, e, x_l, x_u):
    x0_min = np.clip(x_best[0] - e, x_l[0], x_u[0])
    x0_max = np.clip(x_best[0] + e, x_l[0], x_u[0])
    x1_min = np.clip(x_best[1] - e, x_l[1], x_u[1])
    x1_max = np.clip(x_best[1] + e, x_l[1], x_u[1])

    return [x0_min, x0_max, x1_min, x1_max]


def local_random_search(x_l, x_u, sigma, f, patience, min, max_it=10000):
    x_best = np.random.uniform(low=x_l, high=x_u)
    f_best = f(*x_best)

    improvement = 0

    for _ in range(max_it):
        x_cand = perturb_lrs(*x_best, *[x_l[0], x_u[0]], *[x_l[1], x_u[1]], sigma)
        f_cand = f(*x_cand)

        if (min and f_cand < f_best) or (not min and f_cand > f_best):
            x_best = x_cand
            f_best = f_cand
            improvement = 0
        else:
            improvement = +1

        if improvement >= patience:
            break

    return [x_best[0], x_best[1], f_best]


def global_random_search(x_l, x_u, f, patience, min, max_it=10000):
    x_best = np.random.uniform(low=x_l, high=x_u)
    f_best = f(*x_best)

    improvement = 0

    for _ in range(max_it):
        x_cand = perturb_grs(*x_l, *x_u)
        f_cand = f(*x_cand)

        if (min and f_cand < f_best) or (not min and f_cand > f_best):
            x_best = x_cand
            f_best = f_cand
            improvement = 0
        else:
            improvement = +1

        if improvement >= patience:
            break

    return [x_best[0], x_best[1], f_best]


def hill_climbing(x_l, x_u, max_n, e, f, patience, min, max_it=10000):
    x_best = x_l
    f_best = f(*x_best)

    melhoria = True
    improvement = 0
    i = 0
    while i < max_it and melhoria:
        melhoria = False

        for j in range(max_n):
            x_cand = perturb_hill(*clip_to_bounds(x_best, e, x_l, x_u))
            f_cand = f(*x_cand)

            if (min and f_cand < f_best) or (not min and f_cand > f_best):
                x_best = x_cand
                f_best = f_cand

                melhoria = True
                improvement = 0
                break
            else:
                improvement = +1

        if improvement >= patience:
            break

        i = +1
    return [x_best[0], x_best[1], f_best]
