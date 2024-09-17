import numpy as np
import matplotlib.pyplot as plt
import statistics
from search_algorithms import local_random_search, global_random_search, hill_climbing
import objective_functions as obj


def plot(min_val, max_val, func, lrs_points, grs_points, hill_points):
    x_axis = np.linspace(min_val, max_val, 1000)
    X, Y = np.meshgrid(x_axis, x_axis)
    Z = func(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    # ax.plot_surface(X,Y,Z,cmap='jet')
    ax.plot_surface(
        X, Y, Z, cmap="gray", alpha=0.3, edgecolor="k", rstride=30, cstride=30
    )
    ax.contour(X, Y, Z, zdir="z", offset=np.min(Z), cmap="gray")

    ax.scatter(
        [p[0] for p in lrs_points],
        [p[1] for p in lrs_points],
        [p[2] for p in lrs_points],
        color="r",
        s=50,
        marker="X",
        label="LRS Results",
    )
    ax.scatter(
        [p[0] for p in grs_points],
        [p[1] for p in grs_points],
        [p[2] for p in grs_points],
        color="g",
        s=50,
        marker=7,
        label="GRS Results",
    )
    ax.scatter(
        [p[0] for p in hill_points],
        [p[1] for p in hill_points],
        [p[2] for p in hill_points],
        color="b",
        s=50,
        marker="*",
        label="HC Results",
    )

    ax.legend()
    plt.show()


def analysis(lrs_points, grs_points, hill_points):
    lrs_results = np.round([result[2] for result in lrs_points], 3)
    grs_results = np.round([result[2] for result in grs_points], 3)
    hill_results = np.round([result[2] for result in hill_points], 3)

    lrs_mode = statistics.mode(lrs_results)
    grs_mode = statistics.mode(grs_results)
    hill_mode = statistics.mode(hill_results)

    _, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")

    table_data = [["LRS", lrs_mode], ["GRS", grs_mode], ["HC", hill_mode]]
    column_labels = ["Método de Busca", "Moda"]

    ax.table(
        cellText=table_data, colLabels=column_labels, cellLoc="center", loc="center"
    )

    plt.show()


def run_experiment(x_l, x_u, sigma, max_it, max_n, f, e, mini=True):
    points_lrs = []
    points_grs = []
    points_hill = []

    for x in range(100):
        points_lrs.append(local_random_search(x_l, x_u, sigma, f, 100, mini))
        points_grs.append(global_random_search(x_l, x_u, f, 100, mini))
        points_hill.append(hill_climbing(x_l, x_u, max_n, e, f, 100, mini))
        bp = 1

    plot(min(x_l), max(x_u), f, points_lrs, points_grs, points_hill)
    analysis(points_lrs, points_grs, points_hill)


max_it = 10000
maxi = False


# QUESTAO 1
x_l = [-100, -100]
x_u = [100, 100]
sigma = 0.5
max_n = 20
e = 0.1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f1, e)

# QUESTAO 2
x_l = [-2, -2]
x_u = [4, 5]
sigma = 0.4
max_n = 20
e = 1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f2, e, maxi)

# QUESTAO 3
x_l = [-8, -8]
x_u = [8, 8]
sigma = 0.4
max_n = 50
e = 1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f3, e)

# QUESTAO 4
x_l = [-5.12, -5.12]
x_u = [5.12, 5.12]
sigma = 0.4
max_n = 20
e = 1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f4, e)

# QUESTAO 5
x_l = [-10, -10]
x_u = [10, 10]
sigma = 0.4
max_n = 100
e = 15
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f5, e, maxi)

# QUESTAO 6
x_l = [-1, -1]
x_u = [3, 3]
sigma = 0.4
max_n = 150
e = 6
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f6, e, maxi)

# QUESTAO 7
x_l = [0, 0]
x_u = [np.pi, np.pi]
sigma = 0.4
max_n = 30
e = 1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f7, e)

# QUESTAO 8
x_l = [-200, -200]
x_u = [20, 20]
sigma = 0.4
max_n = 20
e = 1
run_experiment(x_l, x_u, sigma, max_it, max_n, obj.f8, e)
