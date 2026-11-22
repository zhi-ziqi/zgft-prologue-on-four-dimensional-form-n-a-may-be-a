# ZGFT Numerical Verification Report

This report records numerical checks of three central claims made by ZGFT
(Ziqi Geometry Field Theory). The reported numbers can be reproduced with
`ZGFT_检测.py`; no external data tables are used by the script.

---

## 1. Claims examined

1. **Scale:** The effective lattice spacing \(a_{\mathrm{eff}} = k^4 a\) can
   reach the nuclear-force scale of 0.5 fm.
2. **Nuclear potential:** The potential in Section 8, \(V(a_r)\), produces
   both a repulsive core and an attractive well, and binds the deuteron.
3. **Predictions:** The model's calculated quantities (radius and scattering
   lengths) can be compared with experiment to assess their deviations.

## 2. Method and parameters

- Planck length: \(a = 1.616255 \times 10^{-20}\ \mathrm{fm}\)
- Effective nuclear-force scale: \(a_{\mathrm{eff}} = 0.5\ \mathrm{fm}\)
- Potential:

  \[
  V(a_r) = \frac{1}{2-k^4a/a_r}
  \left[
  W e^{-(a_r/(k^4a))^2}\frac{k^4a}{a_r}
  - W_1 e^{-a_r/(2k^4a)}\frac{k^4a}{a_r}
  \right]
  \]

- Deuteron: solve the radial equation
  \(-(\hbar^2/2\mu)u'' + Vu = Eu\), with
  \(\mu = 469.4592\ \mathrm{MeV}\) and
  \(\hbar c = 197.32698\ \mathrm{MeV\,fm}\).
- Scattering length: zero-energy solution,
  \(a = \lim_{r\to\infty}(r-u/u')\).
- Comparison model: Malfliet–Tjon, with
  \(V_R = 1438.7228\ \mathrm{MeV\,fm}\), \(\mu_R = 3.11\ \mathrm{fm}^{-1}\),
  \(V_A = 626.8932\ \mathrm{MeV\,fm}\), and
  \(\mu_A = 1.550\ \mathrm{fm}^{-1}\).

## 3. Check 1: scale

| Quantity | Value |
|---|---:|
| Planck length \(a\) | \(1.616 \times 10^{-20}\ \mathrm{fm}\) |
| Required \(a_{\mathrm{eff}}\) | \(0.5\ \mathrm{fm}\) |
| Implied \(k^4\) | **\(3.094 \times 10^{19}\)** |

**Conclusion in the source report: satisfied.** \(k^4\) is dimensionless, and
its magnitude is comparable to the ratio of the Planck and hadronic scales.

## 4. Check 2: nuclear potential and deuteron

The parameters were determined to satisfy \(V(a)=+200\ \mathrm{MeV}\)
(repulsive core) and \(E_0=-2.224\ \mathrm{MeV}\) (deuteron).

| Quantity | Value |
|---|---:|
| \(W\) | **2072.3 MeV** |
| \(W_1\) | **926.9 MeV** |
| \(V(a)\) | **+200.16 MeV** |
| \(E_0\) | **−2.224 MeV** |
| Next energy level | +0.35 MeV (> 0; one bound state) |

Pointwise potential values:

| \(r\) (fm) | ZGFT (MeV) | MT (MeV) |
|---:|---:|---:|
| 0.5 | +200.2 | +30.1 |
| 0.6 | −12.6 | −41.2 |
| 0.7 | −93.5 | −69.6 |
| 0.8 | −116.5 | −77.4 |
| 1.0 | −101.0 | −68.9 |
| 1.5 | −41.3 | −31.8 |
| 2.0 | −17.9 | −12.7 |
| 3.0 | −4.2 | −2.0 |

**Conclusion in the source report: satisfied.** The potential has a repulsive
core and an attractive well, and reproduces the deuteron binding energy.
Differences from the MT potential are concentrated at 0.5–1.2 fm (+170 to
−40 MeV). The report attributes this to MT being a soft-core model: at 0.5 fm
it gives about +30 MeV, whereas AV18 is stated to give values of order
+500 MeV.

## 5. Check 3: quantities not used in fitting

The parameters \(W\) and \(W_1\) were fitted only to \(V(a)\) and \(E_0\).
The following quantities were not used in that fit:

| Quantity | ZGFT | Experiment | Deviation |
|---|---:|---:|---:|
| Deuteron rms radius \(\langle r^2\rangle^{1/2}\) | **4.27 fm** | 3.94 fm | +8.4% |
| Triplet scattering length \(a_t\) | **+6.05 fm** | +5.42 fm | +11.6% |
| Singlet scattering length \(a_s\) | **Not available** | −23.7 fm | — |

**Conclusion in the source report: partially satisfied.** The radius and
triplet scattering length are within about 10% of the stated experimental
values. The singlet value cannot be predicted because the potential has no
spin dependence; the report identifies this as a structural omission, not a
precision issue.

## 6. Summary

| Claim | Conclusion in the source report |
|---|---|
| \(k^4a\) can reach 0.5 fm | Satisfied |
| Potential has a repulsive core and attractive well | Satisfied |
| Deuteron \(E_0=-2.224\ \mathrm{MeV}\) | Satisfied (exact fit) |
| Deuteron radius | Within 8% |
| Triplet scattering length | Within 12% |
| Singlet scattering length | **Not satisfied (spin dependence missing)** |

## 7. Reproduction

```text
python ZGFT_检测.py
```

The script outputs \(V(a)\), \(E_0\), and \(\langle r^2\rangle^{1/2}\), and
generates `ZGFT_检测.png`.

The parameter solver is `ZGFT_求解.py`: it bisects on \(W\), and for each
\(W\), bisects on \(W_1\) to obtain \(E_0=-2.224\).

## 8. Notes

- The manuscript's \(W \approx 2070\ \mathrm{MeV}\) differs from the computed
  2072.3 MeV by 0.1%; the source report considers this rounding.
- The potential has a pole at \(a_r=k^4a/2\), where the denominator
  \(2-k^4a/a_r\) approaches zero. The code applies a hard wall for
  \(r<a_{\mathrm{eff}}\); without this treatment the potential diverges there.
- A spin term (\(\sigma_1\cdot\sigma_2\)) has not been implemented, so the
  singlet channel cannot be predicted. The report notes that adding spin
  would require separate strengths \(W_{1,t}\) and \(W_{1,s}\).

---

Ziqi Zhi, 2026
