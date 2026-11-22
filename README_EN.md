# ZGFT — Ziqi Geometry Field Theory

[中文版 README](README.md)

**An Introduction to ZGFT: On Four-Dimensional Form, N + a May Be a**

ZGFT is a proposed discrete-spacetime framework in which the lattice step is
the Planck length, the stretch variables are complex, and the strong force is
modeled through a minimum effective distance, \(a_{\mathrm{eff}} = k^4a\).

## Contents

| File | Description |
|---|---|
| `ZGFT_CN.tex` | Chinese manuscript |
| `ZGFT_EN.tex` | English manuscript |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a.pdf` | Chinese paper (PDF) |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a (1).pdf` | Additional Chinese paper (PDF) |
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
