# Meissner Effect — Flux Expulsion in a Superconductor

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="meissner-effect-flux-expulsion"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/meissner-effect-flux-expulsion.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A superconducting sample below its critical temperature expels an externally applied magnetic field from its interior; the field decays exponentially within a thin surface layer characterised by the London penetration depth λ.</div>
</div>

## Aim

To model the exponential decay of an applied magnetic field with depth inside a superconductor below its critical temperature, characterised by the London penetration depth λ, demonstrating the Meissner effect.

## Theoretical Background

A superconductor below its critical temperature T_c does more than simply lose electrical resistance: it actively expels magnetic flux from its interior, a phenomenon known as the Meissner effect, which is distinct from (and cannot be explained by) the property of perfect conductivity alone. Screening (persistent) surface currents are set up spontaneously so as to cancel the applied field within the bulk of the material. These currents are not confined to an infinitesimally thin surface layer but decay over a characteristic length scale λ, the London penetration depth (typically tens to a few hundred nanometres), so the field itself decays exponentially with depth x below the surface rather than dropping to zero discontinuously. This exponential screening is captured by the London equations and is one of the defining experimental signatures distinguishing a true superconductor from a hypothetical 'perfect conductor'.

## Governing Formula

$$ B(x) = B_0\, e^{-x/\lambda} $$

| Symbol | Meaning |
|---|---|
| B(x) | field remaining at depth x inside the superconductor (T) |
| B₀ | applied field at the surface (T) |
| x | depth measured from the surface (m) |
| λ | London penetration depth (m) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Meissner Effect — Flux Expulsion in a Superconductor** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Applied surface field | B₀ | 1–50 mT | 10 mT |
| London penetration depth | λ | 20–200 nm | 80 nm |
| Depth into superconductor | x | 0–400 nm | 100 nm |

## Procedure

1. Fix B₀ = 10 mT and λ = 80 nm, and vary the depth x from 0 to 400 nm, recording the remaining field B(x).
2. Plot ln B versus x and verify a straight line whose slope equals −1/λ.
3. Repeat for a different value of λ and confirm the slope changes accordingly.
4. Estimate the depth at which the field has fallen to 1/e (≈ 37%) of its surface value, and compare with λ.
5. Discuss qualitatively why a real (imperfect) superconductor with a finite λ still behaves, for most practical purposes, as if it excluded flux completely.

## Observation Table

| S. No. | x (nm) | B₀ (mT) | λ (nm) | B(x) (mT) | ln B(x) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*ln B(x) vs depth x*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">ln B(x) vs depth x</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">x (nm)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">ln B(x)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | −(Slope) of ln B vs x  (→ 1/λ) | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Remember this exponential model applies strictly to depths measured from a flat surface, well away from corners or edges of the sample.
- Keep the applied field well below the superconductor's critical field B_c, above which superconductivity itself breaks down.
- Change only one of B₀, λ, x at a time while tabulating.
- Distinguish clearly between the Meissner effect (active flux expulsion) and simple perfect conductivity (flux freezing).

## Maximum Permissible Error

$$ \dfrac{\Delta B}{B} = \dfrac{\Delta B_0}{B_0} + \dfrac{x}{\lambda}\cdot\dfrac{\Delta\lambda}{\lambda} + \dfrac{\Delta x}{\lambda} $$

B(x) = B₀ e^(−x/λ) is exponential in x/λ, so its logarithmic derivative brings down a factor of x/λ for the λ term.

<div class="error-calc" data-exp="meissner-effect-flux-expulsion"></div>

## Viva-Voce Questions

1. Distinguish between the Meissner effect and simple perfect conductivity (zero resistance).
2. Define the London penetration depth and give its typical order of magnitude.
3. Why do screening currents flow in a thin surface layer rather than as an infinitesimally thin sheet?
4. What happens to superconductivity if the applied field exceeds the critical field B_c?
5. Name one practical application that relies on the Meissner effect (e.g. magnetic levitation).
