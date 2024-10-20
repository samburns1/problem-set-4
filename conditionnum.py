# samuel burns - hw4 - october 19 2024
import numpy as np
import matplotlib.pyplot as plt
import sys


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


def plotCnandMatStruct(n):
    kmat = makeK(n)
    cnmatrix = np.zeros(n - 1)
    # passes largest kmat, uses i to create a subarray
    for i in range(2, n + 1):
        cnmatrix[i - 2] = condNum(kmat, i)
        # passes largest kmat, uses i to create a subarray

        # did this for fun!
        sys.stdout.write(f"\rSolving Eigenvalues: {int(i/n * 100)}%")
        sys.stdout.flush()
    nvals = np.arange(2, n + 1)

    # conditions number plot
    plt.figure(num="figure 1")
    plt.style.use("Solarize_Light2")
    plt.plot(nvals, cnmatrix, c="grey", linestyle="-", label="Condition Number")
    plt.title("Condition Numbers of $K_n$ versus n")
    plt.xlabel(f"n (from 2 to {n})")  # sprintf equivalent
    plt.ylabel("Condition Number")
    plt.legend(loc="upper center")

    # matrix struct plots
    fig, (sp1, sp2, sp3) = plt.subplots(1, 3)
    fig.suptitle("Matrix Structure Visualization", fontsize="20")

    sp1.matshow(makeK(10))
    sp1.set_title("$K_{10}$")
    sp1.set_xlabel("cols")
    sp1.set_ylabel("rows")

    sp2.matshow(makeK(50))
    sp2.set_title("$K_{50}$")

    sp3.matshow(makeK(100))
    sp3.set_title("$K_{100}$")

    plt.show()


plotCnandMatStruct(1000)
