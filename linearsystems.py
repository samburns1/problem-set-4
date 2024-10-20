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


def bVector(n):
    b = np.ones(n) / (n**2)
    return b


eval = [10, 100, 1000]
plt.style.use("Solarize_Light2")
for e in eval:
    x = np.linalg.solve(makeK(e), bVector(e))
    interval = np.linspace(0, 1, e)
    plt.plot(interval, x, label=f"n = {e}")
    # i am plotting my x values over the arbitrary interval (0:1). increasing n increases the number of evals over the same interval, which gets a better aprox
plt.ylabel("Solutions, $x_i$")
plt.xlabel("Interval (0 to 1)")
plt.title(r"$K_n \vec{x}$ = $\vec{b}$ Solutions for $\vec{b}$ = $\frac{1}{n^2}$")
plt.legend()

plt.show()
