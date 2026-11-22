import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

A = 0.5
W, W1 = 2072.3, 926.9
hbarc = 197.32698
mu = 469.4592
k2 = 2 * mu / hbarc ** 2

VA, muA = 626.8932, 1.550
VR, muR = 1438.7228, 3.11
MT = lambda x: VR * np.exp(-muR * x) / x - VA * np.exp(-muA * x) / x


def V(x):
    d = 2.0 - A / np.maximum(x, 1e-12)
    v = (W * np.exp(-(x / A) ** 2) * A / x - W1 * np.exp(-x / (2 * A)) * A / x) / d
    return np.where(x < A, np.nan, v)


dr, rmax = 0.02, 40.0
r = np.arange(1, int(rmax / dr)) * dr
n = len(r)
vv = np.where(r < A, 1e6, V(r))

H = np.zeros((n, n))
H[np.arange(n), np.arange(n)] = 2 / dr ** 2 + k2 * vv
H[np.arange(n - 1), np.arange(1, n)] = -1 / dr ** 2
H[np.arange(1, n), np.arange(n - 1)] = -1 / dr ** 2
e, vec = np.linalg.eigh(H)
E0 = e[0] / k2
u = vec[:, 0]
p = u ** 2
rms = np.sqrt(np.sum(p * r ** 2) / np.sum(p))

print("W=%.1f W1=%.1f" % (W, W1))
print("V(a)  = %+.2f MeV" % V(A))
print("E0    = %.3f MeV   (exp -2.224)" % E0)
print("<r2>  = %.2f fm    (exp 3.94)" % rms)
print("next level = %.2f MeV" % (e[1] / k2))

fig, ax = plt.subplots(1, 3, figsize=(16, 5))

rr = np.linspace(0.5, 3.0, 600)
ax[0].plot(rr, V(rr), "k-", lw=2.8, label="ZGFT W=2072 W1=927")
ax[0].plot(rr, MT(rr), "b--", lw=1.8, label="Malfliet-Tjon")
ax[0].axhline(0, color="gray", lw=0.8)
ax[0].axhline(-2.224, color="g", ls=":", lw=1.2, label="deuteron -2.224")
ax[0].set_xlabel("r (fm)")
ax[0].set_ylabel("V (MeV)")
ax[0].set_title("potential: repulsive core + attractive well")
ax[0].legend(fontsize=8)
ax[0].grid(alpha=0.3)

ax[1].plot(r, u, "k-", lw=2)
ax[1].set_xlim(0, 10)
ax[1].set_xlabel("r (fm)")
ax[1].set_ylabel("u(r)")
ax[1].set_title("deuteron E0=%.3f MeV, rms=%.2f fm" % (E0, rms))
ax[1].grid(alpha=0.3)

angs = np.linspace(0, 2 * np.pi, 400)
ax[2].plot(np.cos(angs) * 3.94, np.sin(angs) * 3.94, "b:", lw=1.2, label="exp 3.94 fm")
ax[2].plot(np.cos(angs) * rms, np.sin(angs) * rms, "k-", lw=2, label="ZGFT %.2f fm" % rms)
ax[2].set_aspect("equal")
ax[2].set_xlim(-6, 6)
ax[2].set_ylim(-6, 6)
ax[2].set_title("deuteron size")
ax[2].legend(fontsize=9)
ax[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(r"D:\让DeepSeek写的小说\ZGFT_检测.png", dpi=200)
print("saved")
