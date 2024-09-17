import numpy as np


def f1(x1, x2):
    return x1**2 + x2**2


def f2(x1, x2):
    term1 = np.exp(-(x1**2 + x2**2))
    term2 = 2 * np.exp(-((x1 - 1.7) ** 2 + (x2 - 1.7) ** 2))
    return term1 + term2


def f3(x1, x2):
    term1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2)))
    term2 = -np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)))
    return term1 + term2 + 20 + np.exp(1)


def f4(x1, x2):
    term1 = x1**2 - 10 * np.cos(2 * np.pi * x1) + 10
    term2 = x2**2 - 10 * np.cos(2 * np.pi * x2) + 10
    return term1 + term2


def f5(x1, x2):
    term1 = (x1 * np.cos(x1)) / 20
    term2 = 2 * np.exp(-((x1) ** 2) - (x2 - 1) ** 2)
    term3 = 0.01 * x1 * x2
    return term1 + term2 + term3


def f6(x1, x2):
    term1 = x1 * np.sin(4 * np.pi * x1)
    term2 = x2 * np.sin((4 * np.pi * x2) + np.pi) + 1
    return term1 - term2


def f7(x1, x2):
    term1 = np.sin(x1) * np.sin(x1**2 / np.pi) ** 20
    term2 = np.sin(x2) * np.sin(x2**2 / np.pi) ** 20
    return -term1 - term2


def f8(x1, x2):
    return -(x2 + 47) * np.sin(np.sqrt(np.abs(x1 / 2 + (x2 + 47)))) - x1 * np.sin(
        np.sqrt(np.abs(x1 - (x2 + 47)))
    )
