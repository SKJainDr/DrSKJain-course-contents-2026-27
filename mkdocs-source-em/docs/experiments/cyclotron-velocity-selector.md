# Crossed E & B Fields — Velocity Selector & Cyclotron Motion

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="cyclotron-velocity-selector"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/cyclotron-velocity-selector.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A charged particle enters a region of crossed uniform electric and magnetic fields; only particles with speed v = E/B pass through undeflected and then curve into a circular cyclotron orbit in the pure magnetic field beyond.</div>
</div>

## Aim

To determine the velocity selected (undeflected) by a region of crossed uniform electric and magnetic fields, and to compute the cyclotron radius of the selected charged particle once it enters a pure magnetic field region.

## Theoretical Background

In a velocity selector, a charged particle moving through a region containing perpendicular uniform electric and magnetic fields experiences an electric force qE and a magnetic force qv×B. For a particle moving perpendicular to both fields, these forces are exactly balanced (and the particle travels in a straight line undeflected) only when qE = qvB, i.e. when its speed equals v = E/B, independent of the particle's charge or mass. This makes the velocity selector a clean way to prepare a beam of particles with a single, precisely known speed, which is the first stage of instruments such as the mass spectrometer. Once the selected beam leaves the crossed-field region and enters a region containing only the magnetic field, the magnetic force alone provides the centripetal force for circular (cyclotron) motion, with radius r_c = mv/(qB) — a radius that now does depend on the particle's mass-to-charge ratio, which is exactly how a mass spectrometer distinguishes between different ions.

## Governing Formula

$$ v = \dfrac{E}{B}, \qquad r_c = \dfrac{mv}{qB} $$

| Symbol | Meaning |
|---|---|
| v | selected (undeflected) particle speed (m/s) |
| E | electric field in the selector region (V/m) |
| B | magnetic flux density (T) |
| r_c | cyclotron radius in the pure magnetic-field region (m) |
| m/q | mass-to-charge ratio of the particle |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Crossed E & B Fields — Velocity Selector & Cyclotron Motion** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Electric field | E | 1–50 kV/m | 10 kV/m |
| Magnetic flux density | B | 1–100 mT | 20 mT |
| Mass-to-charge ratio (×10⁻⁸ kg/C) | m/q | 0.5–20  | 5.7  |

## Procedure

1. Set E = 10 kV/m and vary B from 1 mT to 100 mT, recording the selected velocity v = E/B at each setting.
2. Plot v versus 1/B and verify a straight line through the origin, confirming v ∝ 1/B at fixed E.
3. Fix B and vary E, verifying v ∝ E.
4. For a fixed selected velocity, compute and tabulate the cyclotron radius r_c for several values of m/q, and verify r_c ∝ (m/q).
5. Discuss how this arrangement could be used to separate ions of two different isotopes with the same charge but slightly different mass.

## Observation Table

| S. No. | E (kV/m) | B (mT) | v = E/B (km/s) | m/q (×10⁻⁸ kg/C) | r_c (m) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Selected velocity v vs 1/B*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Selected velocity v vs 1/B</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">1/B (1/mT)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">v (km/s)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of v vs 1/B | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Ensure E and B are strictly perpendicular to each other and both perpendicular to the initial particle velocity.
- Only particles at exactly v = E/B pass through undeflected; note that this condition is independent of the particle's charge sign as long as forces are computed with correct signs.
- Change only one field at a time when verifying the individual E and B dependences.
- Keep the particle's speed non-relativistic (v ≪ c) so the classical formulas remain valid.

## Maximum Permissible Error

$$ \dfrac{\Delta v}{v} = \dfrac{\Delta E}{E} + \dfrac{\Delta B}{B} $$

v = E/B is a simple quotient of two measured quantities, so their fractional errors add directly.

<div class="error-calc" data-exp="cyclotron-velocity-selector"></div>

## Viva-Voce Questions

1. Derive the velocity-selection condition v = E/B from the balance of electric and magnetic forces.
2. Why is the selected velocity independent of the particle's mass and charge?
3. Derive the cyclotron radius formula r_c = mv/(qB) from Newton's second law for circular motion.
4. How is a velocity selector used as the first stage of a mass spectrometer?
5. What happens to the trajectory if the particle's speed does not exactly equal E/B?
