import numpy as np

A = 0.5
hbarc = 197.32698
mu = 469.4592
k2 = 2 * mu / hbarc ** 2

dr, rmax = 0.02, 40.0
r = np.arange(1, int(rmax / dr)) * dr
n = len(r)

VA, muA = 626.8932, 1.550
VR, muR = 1438.7228, 3.11
MT = lambda x: VR * np.exp(-muR * x) / x - VA * np.exp(-muA * x) / x

base = np.zeros((n, n))
base[np.arange(n), np.arange(n)] = 2 / dr ** 2
base[np.arange(n - 1), np.arange(1, n)] = -1 / dr ** 2
base[np.arange(1, n), np.arange(n - 1)] = -1 / dr ** 2


def Vfun(W, W1):
    d = 2.0 - A / r
    return (W * np.exp(-(r / A) ** 2) * A / r - W1 * np.exp(-r / (2 * A)) * A / r) / d


def E0(W, W1):
    v = np.where(r < A, 1e6, Vfun(W, W1))
    H = base.copy()
    H[np.arange(n), np.arange(n)] += k2 * v
    return np.linalg.eigvalsh(H)[0] / k2


def W1_for(W, target=-2.224):
    lo, hi = 100.0, 4000.0
    for _ in range(16):
        mid = 0.5 * (lo + hi)
        if E0(W, mid) < target:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def core(W, W1):
    return W * np.exp(-1.0) - W1 * np.exp(-0.5)


lo, hi = 1000.0, 5000.0
for it in range(10):
    mid = 0.5 * (lo + hi)
    w1 = W1_for(mid)
    c = core(mid, w1)
    print("it%d  W=%7.1f  W1=%7.1f  V(a)=%8.2f" % (it, mid, w1, c))
    if c < 200.0:
        lo = mid
    else:
        hi = mid

W = round(0.5 * (lo + hi), 1)
W1 = round(W1_for(W), 1)
print("\nW = %.1f MeV   W1 = %.1f MeV" % (W, W1))
print("V(a) = %+.2f MeV    E0 = %.3f MeV" % (core(W, W1), E0(W, W1)))
print("\n r(fm)    ZGFT      MT")
for x in [0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
    d = 2.0 - A / x
    v = (W * np.exp(-(x / A) ** 2) * A / x - W1 * np.exp(-x / (2 * A)) * A / x) / d
    print("%5.1f %8.1f %8.1f" % (x, v, MT(x)))
