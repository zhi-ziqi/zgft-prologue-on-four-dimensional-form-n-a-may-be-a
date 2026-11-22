# ZGFT — Ziqi Geometry Field Theory

[English README](README_EN.md)

**ZGFT（治梓琪几何场论）引论：在四维形上 N+a 或许为 a**

A discrete spacetime framework in which the lattice step is the Planck length,
the stretch variable k is complex, and the strong force follows from a minimum
distance a_eff = k⁴a.

---

## Contents

| File | Description |
|---|---|
| `ZGFT_CN.tex` | 中文版（XeLaTeX / pdfLaTeX + ctex） |
| `ZGFT_EN.tex` | English version |
| `ZGFT_CN.pdf` | 中文版 PDF |
| `ZGFT_EN.pdf` | English PDF |
| `ZGFT_检测.py` | Verification: scale, nuclear potential, deuteron binding |
| `ZGFT_检测.png` | Output figure |

## Core equations

Differentiation is forward:

    Δ₊f(x)  = (f(x+a) − f(x)) / a
    Δ₊₊f(x) = (f(x+2a) − 2f(x+a) + f(x)) / a²

Stretch variables are complex, kⱼ ∈ C, assembled into the 4×4 matrix k⁴.
The gravitational field equation is

    Δ₊₊(Z) = Σ hₙ·k⁴ₙ·a⁴ = C ,   hₙ = χρₙ/b ,   χ = 8πG/c⁴

with the real part of C the gravitational strength and the imaginary part the
quantum phase.

The nuclear potential is

    V(aᵣ) = 1/(2 − k⁴a/aᵣ) · [ W·exp(−(aᵣ/(k⁴a))²)·k⁴a/aᵣ
                             − W₁·exp(−aᵣ/(2k⁴a))·k⁴a/aᵣ ]

    W ≈ 2070 MeV ,  W₁ ≈ 927 MeV ,  k⁴a = 0.5 fm

## Verification

`ZGFT_检测.py` checks three things:

- scale: k⁴·a_Planck = 0.5 fm requires k⁴ ≈ 3.09×10¹⁹
- potential: V(a) = +200 MeV (repulsive core), well minimum near 0.85 fm
- deuteron: E₀ = −2.224 MeV (experimental value), single bound state

Comparison curve: Malfliet–Tjon potential
(V_R = 1438.7228 MeV·fm, μ_R = 3.11 fm⁻¹, V_A = 626.8932 MeV·fm, μ_A = 1.550 fm⁻¹).

## Known limitations

- Spin is not implemented: the singlet channel cannot be produced
  (experiment gives a_s = −23.7 fm, a_t = +5.42 fm).
- Deuteron radius from the model is about 8% larger than experiment.
- Weak force is not written yet.

## Build

    xelatex ZGFT_CN.tex
    xelatex ZGFT_EN.tex

## License

CC BY 4.0

## DOI

https://doi.org/10.5281/zenodo.24433229

## Author

Ziqi Zhi (治梓琪), 2026
