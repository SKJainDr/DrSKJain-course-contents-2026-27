# Method of Images — Charge Near a Grounded Conducting Plane

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="image-charge-grounded-plane"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/image-charge-grounded-plane.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A point charge +q is held at height d above an infinite grounded conducting plane; the induced surface charge distribution and the attractive force are exactly equivalent to those of an image charge −q placed a mirrored distance d below the plane.</div>
</div>

## Aim

To use the method of images to compute the attractive force between a point charge and a nearby infinite grounded conducting plane, and to show that this force equals that between the real charge and an equal-and-opposite image charge at the mirror position.

## Theoretical Background

When a point charge q is placed near a grounded conducting plane, the plane's free electrons rearrange themselves so that the plane remains at zero potential everywhere on its surface. Solving this boundary-value problem directly is difficult, but the method of images gives an elegant shortcut: for the region above the plane, the actual field is identical to the field that would be produced by the real charge q together with a fictitious image charge −q placed at the mirror-image position, with the conducting plane removed entirely. Because both configurations satisfy Laplace's equation above the plane and both give V = 0 on the plane, the uniqueness theorem guarantees they produce the same field in that region. The charge is therefore attracted towards the plane exactly as it would be attracted towards a real charge −q at distance 2d, even though no such charge physically exists — the attraction is due entirely to the induced surface charge on the plane.

## Governing Formula

$$ F = \dfrac{q^2}{4\pi\varepsilon_0 (2d)^2} $$

| Symbol | Meaning |
|---|---|
| F | attractive force on the charge towards the plane (N) |
| q | magnitude of the point charge (C) |
| d | perpendicular height of the charge above the plane (m) |
| ε₀ | permittivity of free space |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Method of Images — Charge Near a Grounded Conducting Plane** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Point charge | q | 1–50 nC | 12 nC |
| Height above the grounded plane | d | 1–20 cm | 5 cm |

## Procedure

1. Set the charge q = 12 nC and vary the height d from 1 cm to 20 cm in steps of 1 cm, recording the computed attractive force F at each step.
2. Plot log F versus log d; the slope should equal −2, confirming the inverse-square dependence on d (equivalently on the image separation 2d).
3. Fix d = 5 cm and vary q from 5 nC to 50 nC, verifying that F is proportional to q².
4. Compare the force at a given d with the force computed from Coulomb's law between two real charges q and −q separated by 2d, and confirm they are numerically identical.
5. Discuss what happens to the induced surface charge density directly beneath the point charge as d is decreased.

## Observation Table

| S. No. | Height d (cm) | Charge q (nC) | Force F (×10⁻⁹ N) | log d | log F |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*log F vs log d (slope method)*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log F vs log d (slope method)</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log d</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">log F</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of log F vs log d | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Treat the plane as a genuinely infinite, grounded conductor — the image-charge method fails near the edges of a finite plane.
- Keep the point charge's physical size much smaller than d, so it may be treated as a true point charge.
- Vary only one parameter (q or d) at a time when tabulating results.
- Remember that the image charge is a mathematical construct valid only in the region above the plane, not below it.

## Maximum Permissible Error

$$ \dfrac{\Delta F}{F} = 2\dfrac{\Delta q}{q} + 2\dfrac{\Delta d}{d} $$

F ∝ q²/d², so both q and d enter squared and each contributes a factor of 2 to the fractional error.

<div class="error-calc" data-exp="image-charge-grounded-plane"></div>

## Viva-Voce Questions

1. State the method of images and explain why it is valid only in the region containing the real charge.
2. Derive the expression for the force of attraction between the charge and the grounded plane.
3. How does the induced surface charge density vary with lateral distance from the point directly below the charge?
4. What would change if the plane were held at a fixed non-zero potential instead of being grounded?
5. Extend the method of images to the case of a charge between two perpendicular grounded planes.
