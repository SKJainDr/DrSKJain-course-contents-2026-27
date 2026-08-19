# Hall Effect — Carrier Density & Sign of Charge Carriers

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="hall-effect-carrier-density"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/hall-effect-carrier-density.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A current-carrying conducting slab is placed in a transverse magnetic field; the transverse Hall voltage V_H developed across the sample is measured to determine the density and sign of the majority charge carriers.</div>
</div>

## Aim

To measure the Hall voltage developed across a current-carrying conducting slab placed in a transverse magnetic field, and use it to determine the density and sign (electron or hole) of the majority charge carriers in the sample.

## Theoretical Background

When a current-carrying conductor is placed in a magnetic field perpendicular to the current, the moving charge carriers experience a sideways magnetic (Lorentz) force, which deflects them towards one edge of the sample. This charge accumulation continues until the resulting transverse electric field exerts an equal and opposite force on the carriers, establishing a steady transverse potential difference known as the Hall voltage V_H. The sign of V_H directly reveals whether the majority carriers are negative (electrons, as in most metals and n-type semiconductors) or positive (holes, as in p-type semiconductors), since the direction of the deflecting force depends on the sign of the moving charge. The magnitude of V_H is inversely proportional to the carrier density n, which is why doped semiconductors — with carrier densities many orders of magnitude lower than metals — are used in practical Hall-effect sensors and probes, giving a readily measurable voltage for a modest current and field.

## Governing Formula

$$ V_H = \dfrac{IB}{n\,e\,t} $$

| Symbol | Meaning |
|---|---|
| V_H | Hall voltage measured across the sample width (V) |
| I | current through the sample (A) |
| B | transverse magnetic flux density (T) |
| n | carrier number density (m⁻³) |
| e | elementary charge (C) |
| t | sample thickness along the field direction (m) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Hall Effect — Carrier Density & Sign of Charge Carriers** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Current through sample | I | 1–100 mA | 20 mA |
| Transverse magnetic field | B | 5–500 mT | 150 mT |
| Carrier density (doped semiconductor sample) | n | 0.5–50 ×10²⁰ m⁻³ | 5 ×10²⁰ m⁻³ |
| Sample thickness | t | 0.05–2 mm | 0.5 mm |

## Procedure

1. Fix I = 20 mA and n and t at their default values, and vary B from 5 mT to 500 mT, recording V_H.
2. Plot V_H versus B and verify a straight line through the origin, confirming V_H ∝ B.
3. Fix B and vary I, verifying V_H ∝ I.
4. Fix I and B and vary the carrier density n; verify that V_H ∝ 1/n, and note how much smaller V_H would be for a metal-like density.
5. Note the polarity of V_H for the assumed carrier sign, and discuss how reversing B or I would reverse this polarity, while reversing the carrier sign (n- vs p-type) would also reverse it independently.

## Observation Table

| S. No. | I (mA) | B (mT) | n (×10²⁰ m⁻³) | t (mm) | V_H (mV) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Hall voltage V_H vs magnetic field B*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Hall voltage V_H vs magnetic field B</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">B (mT)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">V_H (mV)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of V_H vs B (→ carrier density n) | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Ensure the magnetic field is strictly perpendicular to both the current direction and the sample's broad face.
- Use a thin sample (small t) and a low carrier density for a measurable Hall voltage, as is done with doped-semiconductor Hall probes.
- Avoid stray fields or nearby ferromagnetic objects that could add an unwanted component to B.
- Change only one variable (I, B, n, or t) at a time when tabulating.

## Maximum Permissible Error

$$ \dfrac{\Delta V_H}{V_H} = \dfrac{\Delta I}{I} + \dfrac{\Delta B}{B} + \dfrac{\Delta n}{n} + \dfrac{\Delta t}{t} $$

V_H = IB/(net) is a product/quotient of four measured quantities, so all four fractional errors add directly.

<div class="error-calc" data-exp="hall-effect-carrier-density"></div>

## Viva-Voce Questions

1. Explain the physical origin of the Hall voltage in terms of the Lorentz force on moving charge carriers.
2. How does the sign of the Hall voltage reveal whether the majority carriers are electrons or holes?
3. Why are semiconductors, rather than metals, generally used in practical Hall-effect sensors?
4. Derive the expression for the Hall coefficient R_H and relate it to the carrier density.
5. Describe one real-world application of the Hall effect (e.g. current sensing, position sensing).
