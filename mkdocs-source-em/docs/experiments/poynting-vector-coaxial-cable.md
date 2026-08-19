# Poynting Vector & Power Flow in a Coaxial Cable

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="poynting-vector-coaxial-cable"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/poynting-vector-coaxial-cable.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; Cross-section of a coaxial cable carrying DC power between inner and outer conductors; the Poynting vector S = E × H, evaluated in the annular dielectric region, points axially and its integral gives the transmitted power VI.</div>
</div>

## Aim

To compute the Poynting vector S = E × H in the dielectric region between the inner and outer conductors of a coaxial cable carrying DC power, and to verify that its integral over the annular cross-section reproduces the transmitted electrical power P = VI.

## Theoretical Background

It is a common misconception that electrical power flows through the metal of a wire; in fact, according to Poynting's theorem, electromagnetic power flows through the space (the dielectric or vacuum) surrounding the conductors, described by the Poynting vector S = E × H, with the conductors merely guiding the fields. In a coaxial cable carrying a steady current I at voltage V, the radial electric field E between the inner conductor (radius a) and outer shield (radius b) is set up by the charge on the conductors, while the azimuthal magnetic field H circles the inner conductor according to Ampere's law. Their cross product S = E × H points purely in the axial direction, along the cable, and integrating S over the annular cross-sectional area between a and b reproduces exactly the transmitted power P = VI — a striking and non-obvious confirmation that the field-based picture of energy flow is fully consistent with the familiar circuit-theory result.

## Governing Formula

$$ S(r) = \dfrac{VI}{2\pi r^2 \ln(b/a)} $$

| Symbol | Meaning |
|---|---|
| S(r) | axial Poynting flux at radius r (W/m²) |
| V | voltage between inner and outer conductors (V) |
| I | current carried by the conductors (A) |
| a | inner-conductor radius (m) |
| b | outer-conductor (shield) radius (m) |
| r | field-point radius, a < r < b |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Poynting Vector & Power Flow in a Coaxial Cable** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Conductor voltage | V | 1–400 V | 100 V |
| Conductor current | I | 0.1–20 A | 5 A |
| Inner-conductor radius | a | 0.3–5 mm | 1 mm |
| Outer-conductor (shield) radius | b | 2–20 mm | 5 mm |
| Field point radius (a<r<b) | r | 1–19 mm | 2.5 mm |

## Procedure

1. Fix V, I, a, b at their default values and vary the field-point radius r from just above a to just below b, recording S(r) at each step.
2. Plot S versus r and verify the expected 1/r² fall-off across the annular gap.
3. Numerically (or graphically) integrate S(r) over the annular cross-section (2πr·dr from a to b) and compare the result with the transmitted power P = VI.
4. Vary V and I in turn and verify that S(r) at any fixed r scales linearly with each.
5. Discuss why S is zero for r < a or r > b (inside the inner conductor or outside the shield).

## Observation Table

| S. No. | r (mm) | V (V) | I (A) | S(r) (kW/m²) |
|---|---|---|---|---||
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Graph

*Poynting flux S vs radius r*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Poynting flux S vs radius r</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">r (mm)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">S (kW/m²)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | ∫ S · dA over annulus (→ compare with VI) | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Only evaluate S(r) strictly between the inner and outer conductors (a < r < b); the field, and hence S, is zero elsewhere in an ideal coaxial cable.
- Keep the current steady (DC) so the simple electrostatic-plus-magnetostatic picture applies without radiation effects.
- Use consistent SI units when integrating S(r) over the annular area to compare with VI.
- Vary only one of V, I, a, b, r at a time while tabulating.

## Maximum Permissible Error

$$ \dfrac{\Delta S}{S} = \dfrac{\Delta V}{V} + \dfrac{\Delta I}{I} + 2\dfrac{\Delta r}{r} $$

S(r) ∝ VI/r² has r squared in the denominator, contributing a factor of 2 to the fractional error.

<div class="error-calc" data-exp="poynting-vector-coaxial-cable"></div>

## Viva-Voce Questions

1. State Poynting's theorem and define the Poynting vector.
2. Explain the common misconception that power flows 'through the wire', and how the Poynting-vector picture corrects it.
3. Why does S point purely axially in a coaxial cable carrying steady current?
4. Show that integrating S over the annular cross-section reproduces P = VI.
5. How would the picture change for an AC (time-varying) signal instead of DC?
