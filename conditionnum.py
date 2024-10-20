# samuel burns - hw4 - october 19 2024
import numpy as np
import matplotlib.pyplot as plt


def makeK(n):
    kmat = np.zeros((n, n))
    for i in range(n):
        if i == 0:
            kmat[i, i] = 2
        else:
            kmat[i, i] = 2
            kmat[i - 1, i] = -1
            kmat[i, i - 1] = -1
    # print(kmat)
    return kmat


def eigenValues(n):
    eigenvals = np.zeros(n)
    kmat = makeK(n)
    eigenvals, _ = np.linalg.eig(kmat)
    # print(eigenvals)
    return eigenvals


def condNum(n):
    eigenvals = eigenValues(n)
    min = np.min(eigenvals)
    max = np.max(eigenvals)
    cn = np.abs(max / min)
    return cn


def plotCn(n):
    cnmatrix = np.zeros(n - 1)
    for i in range(2, n + 1):
        cnmatrix[i - 2] = condNum(i)
    nvals = np.arange(2, n + 1)
    print(len(nvals))
    print(len(cnmatrix))
    plt.plot(nvals, cnmatrix)
    plt.show()


plotCn(1000)
