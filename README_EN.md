# ZGFT — Ziqi Geometry Field Theory

[中文版 README](README.md)

**An Introduction to ZGFT: On Four-Dimensional Form, N + a May Be a**

### Abstract

ZGFT proposes a discrete-spacetime framework with a Planck-length lattice step,
complex stretch variables, and a nuclear potential built from the effective
length \(a_{\mathrm{eff}} = k^4a\). Numerical checks examine the scale relation,
a repulsive core and attractive well, and deuteron binding energy. The reported
deuteron radius and triplet scattering length differ from experiment; the
current model does not yet include spin or predict the singlet scattering length.

**Keywords:** discrete spacetime; Planck scale; complex stretch variables;
finite differences; nuclear potential; deuteron; numerical verification

## Contents

| File | Description |
|---|---|
| `README.md` | Chinese README |
| `ZGFT_CN.tex` | Chinese manuscript |
| `ZGFT_EN.tex` | English manuscript |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a.pdf` | Chinese paper (PDF) |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a (1).pdf` | Additional Chinese paper (PDF) |
| `证明_验证报告.md` | Chinese numerical verification report |
| `Verification_Report.md` | English translation of the numerical verification report |
| `ZGFT_检测.py` | Checks scales, nuclear potential, and deuteron binding |
| `ZGFT_检测.png` | Output figure |
| `ZGFT_求解.py` | Solver script |
| `ZGFT_自旋.py` | Spin-related script |

## Core equations

The framework uses forward finite differences:

    Δ₊f(x)  = (f(x+a) − f(x)) / a
    Δ₊₊f(x) = (f(x+2a) − 2f(x+a) + f(x)) / a²

The stretch variables are complex, \(k_j \in \mathbb{C}\), and are assembled
into the 4×4 matrix \(k^4\). The proposed gravitational field equation is

    Δ₊₊(Z) = Σ hₙ·k⁴ₙ·a⁴ = C ,   hₙ = χρₙ/b ,   χ = 8πG/c⁴

where the real part of \(C\) represents gravitational strength and its
imaginary part represents the quantum phase.

The proposed nuclear potential is

    V(aᵣ) = 1/(2 − k⁴a/aᵣ) · [ W·exp(−(aᵣ/(k⁴a))²)·k⁴a/aᵣ
                             − W₁·exp(−aᵣ/(2k⁴a))·k⁴a/aᵣ ]

    W ≈ 2070 MeV ,  W₁ ≈ 927 MeV ,  k⁴a = 0.5 fm

## Verification

`ZGFT_检测.py` checks:

- **Scale:** \(k^4 a_\mathrm{Planck} = 0.5\ \mathrm{fm}\) requires
  \(k^4 \approx 3.09 \times 10^{19}\).
- **Potential:** \(V(a) = +200\ \mathrm{MeV}\), with a repulsive core and a
  well minimum near 0.85 fm.
- **Deuteron:** \(E_0 = -2.224\ \mathrm{MeV}\), matching the stated
  experimental value, with a single bound state.

The comparison curve uses the Malfliet–Tjon potential
(\(V_R = 1438.7228\ \mathrm{MeV\,fm}\), \(\mu_R = 3.11\ \mathrm{fm}^{-1}\),
\(V_A = 626.8932\ \mathrm{MeV\,fm}\), \(\mu_A = 1.550\ \mathrm{fm}^{-1}\)).

## Known limitations

- Spin is not implemented, so the singlet channel cannot be produced
  (the stated experimental values are \(a_s = -23.7\ \mathrm{fm}\) and
  \(a_t = +5.42\ \mathrm{fm}\)).
- The model's deuteron radius is about 8% larger than the experimental value.
- The weak force has not yet been formulated.

## Build

Compile either manuscript with XeLaTeX:

    xelatex ZGFT_CN.tex
    xelatex ZGFT_EN.tex

## License

CC BY 4.0

## DOI

[10.5281/zenodo.24433229](https://doi.org/10.5281/zenodo.24433229) — Zenodo record

## Author

Ziqi Zhi (治梓琪), 2026
