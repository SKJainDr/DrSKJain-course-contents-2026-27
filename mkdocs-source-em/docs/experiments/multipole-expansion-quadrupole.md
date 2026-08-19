# Multipole Expansion — Linear Electric Quadrupole

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="multipole-expansion-quadrupole"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/multipole-expansion-quadrupole.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; Three collinear charges +q, −2q, +q (a linear quadrupole) with a distant field point P on the axis; the simulator isolates the pure quadrupole potential term, which falls off as 1/r³.</div>
</div>

## Aim

To compute the far-field electric potential of a linear quadrupole and verify its characteristic 1/r³ fall-off, distinguishing it from the 1/r monopole and 1/r² dipole terms of the general multipole expansion.

## Theoretical Background

The multipole expansion writes the electrostatic potential of any localized charge distribution, viewed from far away, as a sum of terms falling off as successively higher inverse powers of distance: a monopole term (∝1/r, present only if the net charge is non-zero), a dipole term (∝1/r², present if the charge has a net dipole moment even though the total charge is zero), and a quadrupole term (∝1/r³), and so on. A linear quadrupole — charges +q, −2q, +q arranged collinearly with spacing a — has zero net charge and, by symmetry, zero dipole moment, so its leading far-field term is the quadrupole contribution. This configuration models, for example, the charge distribution of a linear symmetric molecule such as CO₂, whose field at large distances is dominated by its quadrupole moment rather than any monopole or dipole term.

## Governing Formula

$$ V_{quad}(r) = \dfrac{3qa^2}{4\pi\varepsilon_0 r^3} $$

| Symbol | Meaning |
|---|---|
| V | on-axis quadrupole potential at distance r (V) |
| q | magnitude of the end charges (C) |
| a | spacing between adjacent charges (m) |
| r | distance to the field point, r ≫ a |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Multipole Expansion — Linear Electric Quadrupole** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| End charge magnitude | q | 1–30 nC | 8 nC |
| Charge spacing | a | 0.5–5 cm | 2 cm |
| Field point distance (on axis) | r | 10–100 cm | 40 cm |

## Procedure

1. Set q = 8 nC and a = 2 cm, and vary r from 10 cm to 100 cm, recording the computed quadrupole potential.
2. Plot log V versus log r and verify the slope is −3, confirming the 1/r³ quadrupole fall-off.
3. Fix r and vary a, verifying that V is proportional to a².
4. Compare the magnitude of V at a given r with what a simple dipole of moment p = qa would give at the same r, and note how much faster the quadrupole term decays.
5. Discuss why a genuinely neutral, non-polar linear molecule can still exert a long-range electrostatic influence on a nearby ion.

## Observation Table

| S. No. | r (cm) | q (nC) | a (cm) | V (×10⁻⁹ V) | log r | log V |
|---|---|---|---|---|---|---||
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## Graph

*log V vs log r (slope method)*

<div class="apparatus-3d-wrap graph-wrap" style="background:#FFFDF3;padding:10px;" markdown="1">
<div class="graph-toolbar" markdown="0">
  <span class="graph-hint">&#128203; Click the grid, then paste (Ctrl+V) a copied photo of your reading/meter trace to overlay it for tracing &mdash; nothing is uploaded, it stays on your screen only.</span>
  <span class="graph-toolbar-controls">
    <label>Overlay opacity <input type="range" class="graph-opacity" min="10" max="100" value="65"></label>
    <button type="button" class="graph-clear-btn">Clear pasted image</button>
  </span>
</div>
<div class="graph-canvas-wrap" tabindex="0" title="Click here, then press Ctrl+V to paste your image">
<svg viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#FFFDF3;border-radius:8px;">
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log V vs log r (slope method)</text>
<line x1="60.00" y1="40" x2="60.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="96.67" y1="40" x2="96.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="133.33" y1="40" x2="133.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="170.00" y1="40" x2="170.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="206.67" y1="40" x2="206.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="243.33" y1="40" x2="243.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="280.00" y1="40" x2="280.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="316.67" y1="40" x2="316.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="353.33" y1="40" x2="353.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="390.00" y1="40" x2="390.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="426.67" y1="40" x2="426.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="463.33" y1="40" x2="463.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="500.00" y1="40" x2="500.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="536.67" y1="40" x2="536.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="573.33" y1="40" x2="573.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="610.00" y1="40" x2="610.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="40.00" x2="610" y2="40.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="68.33" x2="610" y2="68.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="96.67" x2="610" y2="96.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="125.00" x2="610" y2="125.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="153.33" x2="610" y2="153.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="181.67" x2="610" y2="181.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="210.00" x2="610" y2="210.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="238.33" x2="610" y2="238.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="266.67" x2="610" y2="266.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="295.00" x2="610" y2="295.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="323.33" x2="610" y2="323.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="351.67" x2="610" y2="351.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="380.00" x2="610" y2="380.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="408.33" x2="610" y2="408.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="436.67" x2="610" y2="436.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="465.00" x2="610" y2="465.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="40" x2="60" y2="465" stroke="#0B173A" stroke-width="2"/>
<line x1="60" y1="465" x2="610" y2="465" stroke="#0B173A" stroke-width="2"/>
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log r</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">log V</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of log V vs log r | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Keep r large compared with a so the far-field (multipole) approximation remains valid.
- Ensure the two end charges are equal in magnitude so the configuration truly has zero net dipole moment.
- Take the field point strictly on the axis of the array to use the simplified on-axis formula.
- Vary one parameter at a time (q, a, or r) while tabulating.

## Maximum Permissible Error

$$ \dfrac{\Delta V}{V} = \dfrac{\Delta q}{q} + 2\dfrac{\Delta a}{a} + 3\dfrac{\Delta r}{r} $$

V ∝ qa²/r³ has a squared and r cubed, contributing factors of 2 and 3 respectively to the fractional error.

<div class="error-calc" data-exp="multipole-expansion-quadrupole"></div>

## Viva-Voce Questions

1. Define the electric quadrupole moment and give an example of a real molecule that possesses one.
2. Why does a linear array of +q, −2q, +q have zero net dipole moment?
3. Explain, in general terms, why successive multipole terms fall off with increasing powers of 1/r.
4. How would the far-field potential change if the two end charges were unequal?
5. What is the physical origin of quadrupole radiation in the time-varying (radiating) case?
