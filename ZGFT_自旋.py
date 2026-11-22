import numpy as np

A = 0.5
W, W1 = 2072.0, 926.9
hbarc = 197.32698
mu = 469.4592
k2 = 2 * mu / hbarc ** 2


def V(r, lam):
    d = 2.0 - A / r
    return (W * np.exp(-(r / A) ** 2) * A / r - lam * W1 * np.exp(-r / (2 * A)) * A / r) / d


def asc(lam, rmax=120.0, dr=0.01):
    r = np.arange(1, int(rmax / dr)) * dr
    v = np.where(r < A, 1e6, V(r, lam))
    u = np.zeros(len(r))
    u[0] = dr
    u[1] = 2 * dr
    for i in range(1, len(r) - 1):
        u[i + 1] = 2 * u[i] - u[i - 1] + dr * dr * k2 * v[i] * u[i]
    m = (r > 80) & (r < 120)
    s = np.gradient(u, dr)
    return np.mean(r[m] - u[m] / s[m])


print("lam=1.0  a = %.2f fm  (triplet, exp +5.42)" % asc(1.0))

lo, hi = -5.0, 1.0
for _ in range(40):
    mid = 0.5 * (lo + hi)
    if asc(mid) > -23.7:
        hi = mid
    else:
        lo = mid
lam_s = 0.5 * (lo + hi)
print("lam_s = %.4f  -> a_s = %.2f fm (target -23.7)" % (lam_s, asc(lam_s)))

beta = (1.0 - lam_s) / 3.0
lam_t = 1.0 + beta
print("beta  = %.4f" % beta)
print("lam_t = %.4f  -> a_t = %.2f fm (exp +5.42)" % (lam_t, asc(lam_t)))
