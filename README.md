# ZGFT — Ziqi Geometry Field Theory

[English README](README_EN.md)

**ZGFT（治梓琪几何场论）引论：在四维形上 N+a 或许为 a**

### 摘要

ZGFT（治梓琪几何场论）提出一种基于离散时空、有限差分和复数伸缩变量的理论框架。
仓库收录 v4.8 中英文论文稿与 v4.9 文字版，涉及引力场方程、引力三区对比，以及由
单纯形程序拟合的多项核力势和氘核相关数值。文中数值为作者提出的模型结果，并不代表
已由独立研究验证。

**关键词：** 离散时空；有限差分；复数伸缩变量；引力场方程；引力三区；核力势；氘核

**English summary:** ZGFT (Ziqi Geometry Field Theory) proposes a framework based on
discrete spacetime, finite differences, and complex stretch variables. This
repository includes the v4.8 Chinese and English manuscripts and a v4.9 text
edition, covering a proposed gravitational field equation, comparisons across
three gravitational regimes, and a multi-term nuclear potential with
simplex-fitted deuteron-related calculations. Numerical results are claims of
the proposed model and have not been independently validated.

---

## Contents

| File | Description |
|---|---|
| `README_EN.md` | English README |
| `ZGFT_CN.tex` | v4.8 中文论文稿 |
| `ZGFT_EN.tex` | v4.8 English manuscript |
| `ZGFT_文字版.txt` | v4.9 文字版 |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a (3).pdf` | 新版论文 PDF |
| `ZG_治梓琪几何_引论_在四维形上N_a或许为a (2).pdf` | 附加论文 PDF |
| `ZGFT_引力三区.py` | 引力三区计算与绘图脚本 |
| `ZGFT_引力三区对比.png` | 引力三区对比图 |
| `ZGFT_单纯形.py` | 核力参数单纯形拟合脚本 |
| `ZGFT_CN.pdf` | 中文版 PDF |
| `ZGFT_EN.pdf` | English PDF |
| `证明_验证报告.md` | 中文数值检验报告 |
| `Verification_Report.md` | English translation of the numerical verification report |
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

## Zenodo 版本

| 版本 | 说明 | DOI |
|---|---|---|
| **v4.9（新版，2026-11-28）** | 当前版本 | [10.5281/zenodo.24615368](https://doi.org/10.5281/zenodo.24615368) |
| **v4.5（旧版，2026-11-22）** | 早期版本 | [10.5281/zenodo.24433229](https://doi.org/10.5281/zenodo.24433229) |

**概念 DOI（引用该项目及其最新版本）：** [10.5281/zenodo.23914598](https://doi.org/10.5281/zenodo.23914598)

## Author

Ziqi Zhi (治梓琪), 2026
