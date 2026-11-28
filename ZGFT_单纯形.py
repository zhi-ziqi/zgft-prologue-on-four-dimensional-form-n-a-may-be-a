import numpy as np

hbarc = 197.32698
M_N = 938.919
mu_r = M_N / 2
kin = hbarc ** 2 / (2 * mu_r)
A = 0.5
R_W = 0.30
R_2PI = 0.70
R_PI = 1.41
R_CUT = 0.55
C_DD = -2.0
C_SD = np.sqrt(8.0)
C_LS = -3.0

dr, rmax = 0.05, 20.0
r = np.arange(1, int(rmax / dr) + 1) * dr
n = len(r)

T2 = np.zeros((n, n))
T2[np.arange(n), np.arange(n)] = 2 / dr ** 2
T2[np.arange(n - 1), np.arange(1, n)] = -1 / dr ** 2
T2[np.arange(1, n), np.arange(n - 1)] = -1 / dr ** 2
TK = kin * T2
TD = kin * (T2 + np.diag(6.0 / r ** 2))

OM = np.where(r < A, 0.0, np.exp(-r / R_W) / r)
P2 = np.where(r < A, 0.0, np.exp(-r / R_2PI) / r)
xp = r / R_PI
TPI = np.where(r < A, 0.0, (1.0 + 3.0 / xp + 3.0 / xp ** 2) * np.exp(-xp) / xp)
CUT = 1.0 - np.exp(-(r / R_CUT) ** 2)
TEN = TPI * CUT
LS = np.where(r < A, 0.0, np.exp(-r / R_2PI))

TGT = np.array([-2.224, 5.42, 0.058, 0.2859])
SCL = np.array([2.224, 5.42, 0.058, 0.2859])


def measure(p):
    ww, w2, wT, wV = p
    vc = np.where(r < A, 1e6, ww * OM - w2 * P2)
    H = np.zeros((2 * n, 2 * n))
    H[:n, :n] = TK + np.diag(vc)
    H[n:, n:] = TD + np.diag(vc + C_DD * wT * TEN + C_LS * wV * LS)
    off = C_SD * wT * TEN
    H[:n, n:] = np.diag(off)
    H[n:, :n] = np.diag(off)
    e, vec = np.linalg.eigh(H)
    v = vec[:, 0]
    us, ud = v[:n], v[n:]
    nrm = np.sum(us ** 2 + ud ** 2) * dr
    us, ud = us / np.sqrt(nrm), ud / np.sqrt(nrm)
    PD = np.sum(ud ** 2) * dr
    Q = np.sum(r ** 2 * (us * ud - ud ** 2 / (2 * np.sqrt(2)))) * dr / np.sqrt(50)
    Rm = 120.0
    rr = np.arange(1, int(Rm / dr)) * dr
    vv = np.where(rr < A, 1e6, np.interp(rr, r, vc))
    u = np.zeros(len(rr))
    u[0], u[1] = dr, 2 * dr
    for i in range(1, len(rr) - 1):
        u[i + 1] = 2 * u[i] - u[i - 1] + dr * dr * 2 * kin * vv[i] * u[i]
    msk = (rr > 90) & (rr < 120)
    s = np.gradient(u, dr)
    at = np.mean(rr[msk] - u[msk] / s[msk])
    return np.array([e[0], at, PD, Q])


def chi(p):
    obs = measure(p)
    if not np.isfinite(obs).all():
        return 1e6
    return float(np.sum(((obs - TGT) / SCL) ** 2))


def nelder(simplex, max_iter=120):
    simplex = np.array(simplex, dtype=float)
    vals = np.array([chi(s) for s in simplex])
    for it in range(max_iter):
        idx = np.argsort(vals)
        simplex, vals = simplex[idx], vals[idx]
        if vals[0] < 1e-8:
            break
        cen = simplex[:-1].mean(axis=0)
        xr = cen + (cen - simplex[-1])
        fr = chi(xr)
        if fr < vals[0]:
            xe = cen + 2 * (cen - simplex[-1])
            fe = chi(xe)
            simplex[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            simplex[-1], vals[-1] = xr, fr
        else:
            xc = cen + 0.5 * (simplex[-1] - cen)
            fc = chi(xc)
            if fc < vals[-1]:
                simplex[-1], vals[-1] = xc, fc
            else:
                simplex[1:] = simplex[0] + 0.5 * (simplex[1:] - simplex[0])
                vals[1:] = [chi(s) for s in simplex[1:]]
    idx = np.argsort(vals)
    return simplex[idx[0]], vals[idx[0]]


p0 = np.array([3150.0, 485.0, -10.0, 4.9])
simp = [p0, p0 + [400, 0, 0, 0], p0 + [0, 150, 0, 0], p0 + [0, 0, 2, 0], p0 + [0, 0, 0, 2]]
best, val = nelder(simp)
obs = measure(best)
dev = 100 * (obs - TGT) / SCL
print("chi=%.6f" % val)
print("w_omega=%.2f w_2pi=%.2f w_T=%.3f w_V=%.3f" % tuple(best))
print("E0=%.4f a_t=%.3f P_D=%.3f%% Q=%.5f" % (obs[0], obs[1], 100 * obs[2], obs[3]))
print("dev%% E0=%+.2f a_t=%+.2f P_D=%+.2f Q=%+.2f" % tuple(dev))
