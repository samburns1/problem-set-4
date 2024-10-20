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


def eigenValues(kmat, subarr):
    eigenvals = np.linalg.eigvalsh(kmat[:subarr, :subarr])
    # eigvalsh for symmetric matrices as k matrix is symmetric - way more efficent
    return eigenvals


def condNum(kmat, subarr):
    eigenvals = eigenValues(kmat, subarr)
    min = np.min(eigenvals)
    max = np.max(eigenvals)
    cn = np.abs(max / min)
    return cn


def plotCn(n):
    kmat = makeK(n)
    cnmatrix = np.zeros(n - 1)
    for i in range(2, n + 1):
        cnmatrix[i - 2] = condNum(
            kmat, i
        )  # passes largest kmat, uses i to create a subarray
        print("Progress: ", i)
    nvals = np.arange(2, n + 1)
    print(len(nvals))
    print(len(cnmatrix))
    plt.style.use("Solarize_Light2")
    plt.plot(nvals, cnmatrix, c="grey", linestyle="-", label="Condition Number")
    plt.title("Condition Numbers of K-Matrix versus n")
    plt.xlabel(f"n (from 2 to {n})")  # sprintf equivalent
    plt.ylabel("Condition Number")
    plt.legend(loc="upper center")
    plt.show()


plotCn(1000)
