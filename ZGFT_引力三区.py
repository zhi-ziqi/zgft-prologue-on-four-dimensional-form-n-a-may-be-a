import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

a = 1.616e-35
G = 6.674e-11
c = 2.998e8
Msun = 1.989e30
Rs = 2 * G * Msun / c ** 2

rr = np.logspace(np.log10(a), 12, 800)
kg = 2 * Rs / rr ** 3
kz = 2 * Rs / (rr * (rr + a) * (rr + 2 * a))

fig, ax = plt.subplots(1, 3, figsize=(16, 4.8))
for i, (lo, hi, lab) in enumerate([(1e10, 1e12, "ordinary: r ~ 1 AU"),
                                   (1e4, 1e5, "strong: r ~ 10 km"),
                                   (1e-35, 1e-33, "singularity: r ~ a")]):
    m = (rr >= lo) & (rr <= hi)
    ax[i].loglog(rr[m], kg[m], "b--", lw=1.8, label="GR")
    ax[i].loglog(rr[m], kz[m], "k-", lw=2.6, label="ZGFT")
    ax[i].set_xlabel("r (m)")
    ax[i].set_ylabel("K (1/m^2)")
    ax[i].set_title(lab)
    ax[i].legend(fontsize=7)
    ax[i].grid(alpha=0.3, which="both")
plt.tight_layout()
plt.savefig(r"D:\让DeepSeek写的小说\ZGFT_引力三区对比.png", dpi=170)
print("saved gravity figure")
