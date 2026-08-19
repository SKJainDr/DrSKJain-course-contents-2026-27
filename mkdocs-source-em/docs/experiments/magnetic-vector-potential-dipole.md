# Magnetic Vector Potential of a Current Loop (Dipole Limit)

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="magnetic-vector-potential-dipole"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/magnetic-vector-potential-dipole.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A small circular current loop of radius a carrying current I, viewed as a magnetic dipole; the vector potential A and field B are evaluated at a distant field point specified by spherical coordinates (r, θ).</div>
</div>

## Aim

To evaluate the magnetic vector potential A of a small current loop in the far-field (magnetic dipole) approximation, and relate its spatial dependence to the resulting dipole field B = ∇ × A.

## Theoretical Background

Unlike the scalar electrostatic potential, the magnetic field is more naturally described through a vector potential A, defined by B = ∇ × A, which automatically guarantees ∇·B = 0. For a small planar current loop of radius a carrying current I, viewed from a distance r ≫ a, the vector potential has only an azimuthal component A_φ that falls off as 1/r² and depends on the polar angle θ measured from the loop's axis. This is the magnetic analogue of the electric dipole potential, and the loop's magnetic moment m = I·πa² plays the role that the electric dipole moment p plays in electrostatics. Taking the curl of A_φ reproduces the familiar magnetic dipole field pattern, with field lines emerging from one face of the loop and curving back to enter the other — identical in form to the electric dipole field lines, but without any true magnetic monopoles at the ends.

## Governing Formula

$$ A_\varphi(r,\theta) = \dfrac{\mu_0 I a^2 \sin\theta}{4 r^2} $$

| Symbol | Meaning |
|---|---|
| A_φ | azimuthal component of the vector potential (T·m) |
| I | current in the loop (A) |
| a | loop radius (m) |
| r | distance to the field point, r ≫ a |
| θ | polar angle from the loop's axis |
| μ₀ | permeability of free space |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Magnetic Vector Potential of a Current Loop (Dipole Limit)** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Loop current | I | 0.1–10 A | 2 A |
| Loop radius | a | 0.5–5 cm | 2 cm |
| Field point distance | r | 10–80 cm | 30 cm |
| Polar angle from loop axis | θ | 0–180 deg | 90 deg |

## Procedure

1. Fix I = 2 A, a = 2 cm and θ = 90° (equatorial plane), and vary r from 10 cm to 80 cm, recording A_φ.
2. Plot log A_φ versus log r and verify a slope of −2, confirming the dipole 1/r² fall-off.
3. Fix r and vary θ from 0° to 180°, and verify that A_φ follows a sinθ dependence, vanishing on-axis (θ = 0° or 180°).
4. Vary the loop current I and confirm A_φ ∝ I.
5. Compute the loop's magnetic moment m = Iπa² and compare the measured A_φ(r,90°) with the standard dipole formula A = μ₀m/(4πr²).

## Observation Table

| S. No. | r (cm) | θ (deg) | I (A) | A_φ (×10⁻⁶ T·cm) | log r | log A_φ |
|---|---|---|---|---|---|---||
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## Graph

*log A_φ vs log r (slope method)*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log A_φ vs log r (slope method)</text>
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
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">log A_φ</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of log A_φ vs log r | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Keep r large compared with a to remain within the dipole (far-field) approximation.
- Vary only one of I, a, r, θ at a time while tabulating other quantities.
- Remember A_φ vanishes exactly on the loop's axis (θ = 0°, 180°) — do not mistake this for an error.
- Keep the current direction consistent so that the sign of A_φ has a well-defined meaning.

## Maximum Permissible Error

$$ \dfrac{\Delta A}{A} = \dfrac{\Delta I}{I} + 2\dfrac{\Delta a}{a} + 2\dfrac{\Delta r}{r} $$

A_φ ∝ Ia²/r² has a and r both squared, each contributing a factor of 2 to the fractional error.

<div class="error-calc" data-exp="magnetic-vector-potential-dipole"></div>

## Viva-Voce Questions

1. Why is the magnetic field described using a vector potential rather than a scalar potential?
2. Define the magnetic dipole moment of a current loop and state its units.
3. Show qualitatively how B = ∇ × A reproduces the dipole field pattern from A_φ.
4. Compare the r-dependence and angular dependence of A_φ with the electric dipole potential V.
5. Why does A_φ vanish on the axis of the loop even though B does not?
