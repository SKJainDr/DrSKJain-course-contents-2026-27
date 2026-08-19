# Transmission Lines — Characteristic Impedance, Reflection & VSWR

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="transmission-line-impedance-vswr"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/transmission-line-impedance-vswr.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A transmission line of characteristic impedance Z₀ terminated in a load Z_L; any mismatch produces a reflected wave characterised by reflection coefficient Γ, which sets up a standing-wave pattern measured by the VSWR.</div>
</div>

## Aim

To compute the reflection coefficient and voltage standing-wave ratio (VSWR) on a transmission line of characteristic impedance Z₀ terminated in a mismatched load impedance Z_L, and to see how impedance matching minimises reflected power.

## Theoretical Background

A transmission line — a coaxial cable, a twin-lead, or a printed microstrip trace — has an intrinsic characteristic impedance Z₀ determined by its geometry and the dielectric between its conductors. If the line is terminated in a load whose impedance Z_L differs from Z₀, not all of the incident wave's power can be absorbed by the load; a fraction is reflected back towards the source, described by the (generally complex) reflection coefficient Γ = (Z_L−Z₀)/(Z_L+Z₀). The superposition of the incident and reflected waves sets up a standing-wave pattern along the line, with the ratio of maximum to minimum voltage amplitude called the voltage standing-wave ratio (VSWR). A perfectly matched load (Z_L = Z₀) gives Γ = 0 and VSWR = 1 (no standing wave, all power delivered to the load), while a short-circuit or open-circuit load gives |Γ| = 1 and an infinite VSWR. Minimising VSWR through careful impedance matching is a central concern in RF and microwave engineering, since a high VSWR both wastes transmitted power and can stress the source.

## Governing Formula

$$ \Gamma = \dfrac{Z_L - Z_0}{Z_L + Z_0}, \qquad VSWR = \dfrac{1+|\Gamma|}{1-|\Gamma|} $$

| Symbol | Meaning |
|---|---|
| Γ | voltage reflection coefficient (dimensionless) |
| Z₀ | line characteristic impedance (Ω) |
| Z_L | load impedance (Ω, assumed resistive here) |
| VSWR | voltage standing-wave ratio, always ≥ 1 |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Transmission Lines — Characteristic Impedance, Reflection & VSWR** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Line characteristic impedance | Z₀ | 25–150 Ω | 50 Ω |
| Load impedance (resistive) | Z_L | 5–500 Ω | 75 Ω |

## Procedure

1. Fix Z₀ = 50 Ω (a standard RF line impedance) and vary Z_L from 5 Ω to 500 Ω, recording Γ and VSWR at each step.
2. Plot VSWR versus Z_L and identify the value of Z_L giving the minimum VSWR (it should be Z_L = Z₀).
3. Verify that Z_L = 0 (short circuit) and Z_L → ∞ (open circuit) both give |Γ| = 1 and a very large VSWR.
4. Repeat for a different line impedance Z₀ (e.g. 75 Ω, as used in cable-TV systems) and note how the optimal load shifts accordingly.
5. Discuss what fraction of incident power is reflected for a given Γ (reflected power fraction = |Γ|²), and compute it for one representative mismatch.

## Observation Table

| S. No. | Z₀ (Ω) | Z_L (Ω) | Γ | VSWR | Reflected power fraction |Γ|² |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*VSWR vs load impedance Z_L*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">VSWR vs load impedance Z_L</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Z_L (Ω)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">VSWR</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Z_L giving minimum VSWR | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Treat the load as purely resistive in this simplified model; a reactive load would give a complex Γ with an additional phase angle.
- Remember VSWR is always ≥ 1, with 1 representing a perfectly matched, reflection-free termination.
- Vary Z_L over a wide enough range to clearly locate the VSWR minimum.
- Do not confuse the characteristic impedance Z₀ (a property of the line itself) with the load impedance Z_L (a property of the termination).

## Maximum Permissible Error

$$ \text{Evaluated numerically from } Z_0 \text{ and } Z_L \text{ via } \Gamma $$

VSWR is a nonlinear function of the reflection coefficient Γ, so its propagated uncertainty is best evaluated numerically by perturbing Z₀ and Z_L in turn rather than via one closed-form expression.

<div class="error-calc" data-exp="transmission-line-impedance-vswr"></div>

## Viva-Voce Questions

1. Define the reflection coefficient Γ and the voltage standing-wave ratio (VSWR).
2. Why does a matched load (Z_L = Z₀) give zero reflection?
3. What are the VSWR values for a short-circuit and an open-circuit termination, and why?
4. Explain the practical importance of minimising VSWR in an RF transmitter feed line.
5. What technique(s) can be used to match a mismatched load to a transmission line?
