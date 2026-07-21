# 6. Uniform Bending — Young's Modulus by the Elevation Method

!!! abstract "Module"
    Elasticity of Solids &middot; Module 2


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-uniform-bending){target=_blank}**

## Aim

To determine the Young's modulus of the material of a beam by the method of uniform bending, using symmetric end-loading and measuring the elevation of the midpoint.

## Theoretical Background

In uniform bending, a beam is supported symmetrically on two knife edges and loaded with equal weights hung symmetrically beyond each knife edge, at equal distances from them. Unlike the cantilever case, the bending moment between the two knife edges is now constant along the entire span — hence the name 'uniform' bending — because the two equal external couples applied beyond each support balance each other identically at every section between the supports.

A constant bending moment means the beam bends into a circular arc of constant curvature between the two knife edges. As a result, the midpoint of the beam rises (or falls, depending on the sense of loading) relative to the two supported points — an elevation that can be measured very precisely using a pin at the centre observed through a travelling microscope, exactly as in the cantilever method.

Because the curvature (and hence the elevation) depends on the elastic properties of the beam in the same way as in non-uniform bending — through the same flexural rigidity Ybd³/12 — this method provides an independent way of extracting Young's modulus, and is often preferred because a uniformly curved beam is easier to analyse exactly and is less sensitive to exactly where along the overhang the load hangers are positioned.

The elevation depends linearly on the load, and on the square of the knife-edge separation, giving two independent straight-line checks (elevation vs load, and vs the square of the separation) of the underlying theory.

## Governing Formulas

**Elevation of the midpoint:**

$$
e = \dfrac{3 M g\, a\, l^{2}}{2\, b\, d^{3}\, Y}
$$

**Young's modulus:**

$$
Y = \dfrac{3 M g\, a\, l^{2}}{2\, b\, d^{3}\, e}
$$

where $M$ is each of the two equal end loads, $a$ the distance from each knife edge to its load point (the overhang), $l$ the separation between the two knife edges, and $b$, $d$ the breadth and thickness of the beam.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="105.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Two Knife Edges</text>
<rect x="210.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="275.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Beam</text>
<rect x="380.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="445.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Symmetric End</text>
<text x="445.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Loads</text>
<rect x="550.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="615.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Travelling</text>
<text x="615.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Microscope</text>
<line x1="170.0" y1="100.0" x2="202.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="202.0,94.0 212.0,100.0 202.0,106.0" fill="#C97A27"/>
<line x1="340.0" y1="100.0" x2="372.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="372.0,94.0 382.0,100.0 372.0,106.0" fill="#C97A27"/>
<line x1="510.0" y1="100.0" x2="542.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="542.0,94.0 552.0,100.0 542.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A beam resting horizontally on two knife edges with two loop-and-hanger loading points beyond each knife edge at equal overhangs, and a pin at the exact midpoint observed through a travelling microscope to measure elevation.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Each end load | M | 50 – 500 | g |
| Overhang (knife edge to load) | a | 5 – 20 | cm |
| Knife-edge separation | l | 20 – 60 | cm |
| Beam breadth | b | 1.0 – 3.0 | cm |
| Beam thickness | d | 0.20 – 0.80 | cm |


**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Elevation of midpoint | e | mm |

## Procedure

1. Launch the Uniform Bending panel; set b, d, a and l to their default values.
2. Vary the symmetric end load M in equal steps and record the elevation e of the midpoint shown on the readout for each step.
3. Plot e against M and verify a straight line through the origin.
4. Reset M to a middle value; vary the knife-edge separation l and tabulate e for each l; verify that e ∝ l² by plotting e against l².
5. Calculate Young's modulus from the slope of the e vs M graph, using the known a, l, b, d.

## Observation Table

*Table: Elevation of the midpoint with increasing symmetric end load*

| S. No. | M (g) | a (cm) | l (cm) | Elevation e (mm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |


## Graph

Plot **Elevation, e** (y-axis) against **Each end load, M** (x-axis).

Expected trend: a straight line through the origin (e ∝ M).

*e vs M, expected to be a straight line through the origin; slope = 3gal²/(2bd³Y)*

<div class="apparatus-3d-wrap graph-wrap" style="background:#FFFBF0;padding:10px;" markdown="1">
<div class="graph-toolbar" markdown="0">
  <span class="graph-hint">&#128203; Click the grid, then paste (Ctrl+V) a copied photo of your camera/DSO/graph trace to overlay it for tracing &mdash; nothing is uploaded, it stays on your screen only.</span>
  <span class="graph-toolbar-controls">
    <label>Overlay opacity <input type="range" class="graph-opacity" min="10" max="100" value="65"></label>
    <button type="button" class="graph-clear-btn">Clear pasted image</button>
  </span>
</div>
<div class="graph-canvas-wrap" tabindex="0" title="Click here, then press Ctrl+V to paste your camera/DSO image">
<svg viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#FFFBF0;border-radius:8px;">
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Elevation vs End Load</text>
<line x1="82.22" y1="40.0" x2="82.22" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="94.44" y1="40.0" x2="94.44" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="118.89" y1="40.0" x2="118.89" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="131.11" y1="40.0" x2="131.11" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="155.56" y1="40.0" x2="155.56" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="167.78" y1="40.0" x2="167.78" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="192.22" y1="40.0" x2="192.22" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="204.44" y1="40.0" x2="204.44" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="228.89" y1="40.0" x2="228.89" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="241.11" y1="40.0" x2="241.11" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="265.56" y1="40.0" x2="265.56" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="277.78" y1="40.0" x2="277.78" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="302.22" y1="40.0" x2="302.22" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="314.44" y1="40.0" x2="314.44" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="338.89" y1="40.0" x2="338.89" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="351.11" y1="40.0" x2="351.11" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="375.56" y1="40.0" x2="375.56" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="387.78" y1="40.0" x2="387.78" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="412.22" y1="40.0" x2="412.22" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="424.44" y1="40.0" x2="424.44" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="448.89" y1="40.0" x2="448.89" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="461.11" y1="40.0" x2="461.11" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="485.56" y1="40.0" x2="485.56" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="497.78" y1="40.0" x2="497.78" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="522.22" y1="40.0" x2="522.22" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="534.44" y1="40.0" x2="534.44" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="558.89" y1="40.0" x2="558.89" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="571.11" y1="40.0" x2="571.11" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="595.56" y1="40.0" x2="595.56" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="607.78" y1="40.0" x2="607.78" y2="465.0" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="49.44" x2="620.0" y2="49.44" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="58.89" x2="620.0" y2="58.89" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="77.78" x2="620.0" y2="77.78" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="87.22" x2="620.0" y2="87.22" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="106.11" x2="620.0" y2="106.11" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="115.56" x2="620.0" y2="115.56" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="134.44" x2="620.0" y2="134.44" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="143.89" x2="620.0" y2="143.89" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="162.78" x2="620.0" y2="162.78" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="172.22" x2="620.0" y2="172.22" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="191.11" x2="620.0" y2="191.11" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="200.56" x2="620.0" y2="200.56" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="219.44" x2="620.0" y2="219.44" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="228.89" x2="620.0" y2="228.89" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="247.78" x2="620.0" y2="247.78" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="257.22" x2="620.0" y2="257.22" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="276.11" x2="620.0" y2="276.11" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="285.56" x2="620.0" y2="285.56" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="304.44" x2="620.0" y2="304.44" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="313.89" x2="620.0" y2="313.89" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="332.78" x2="620.0" y2="332.78" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="342.22" x2="620.0" y2="342.22" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="361.11" x2="620.0" y2="361.11" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="370.56" x2="620.0" y2="370.56" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="389.44" x2="620.0" y2="389.44" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="398.89" x2="620.0" y2="398.89" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="417.78" x2="620.0" y2="417.78" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="427.22" x2="620.0" y2="427.22" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="446.11" x2="620.0" y2="446.11" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.0" y1="455.56" x2="620.0" y2="455.56" stroke="#E3EBD6" stroke-width="0.35"/>
<line x1="70.00" y1="40.0" x2="70.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="106.67" y1="40.0" x2="106.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="143.33" y1="40.0" x2="143.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="180.00" y1="40.0" x2="180.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="216.67" y1="40.0" x2="216.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="290.00" y1="40.0" x2="290.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="326.67" y1="40.0" x2="326.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="363.33" y1="40.0" x2="363.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="400.00" y1="40.0" x2="400.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="473.33" y1="40.0" x2="473.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="510.00" y1="40.0" x2="510.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="546.67" y1="40.0" x2="546.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="583.33" y1="40.0" x2="583.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="620.00" y1="40.0" x2="620.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="40.00" x2="620.0" y2="40.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="68.33" x2="620.0" y2="68.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="96.67" x2="620.0" y2="96.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="125.00" x2="620.0" y2="125.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="153.33" x2="620.0" y2="153.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="210.00" x2="620.0" y2="210.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="238.33" x2="620.0" y2="238.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="266.67" x2="620.0" y2="266.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="295.00" x2="620.0" y2="295.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="351.67" x2="620.0" y2="351.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="380.00" x2="620.0" y2="380.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="408.33" x2="620.0" y2="408.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="436.67" x2="620.0" y2="436.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="465.00" x2="620.0" y2="465.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.00" y1="40.0" x2="70.00" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="620.00" y1="40.0" x2="620.00" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="40.00" x2="620.0" y2="40.00" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="465.00" x2="620.0" y2="465.00" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<rect x="70.0" y="40.0" width="550.0" height="425.0" fill="none" stroke="#14251C" stroke-width="2"/>
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Each end load, M (g)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Elevation, e (mm)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. Compute the slope of the e vs M graph: slope = 3gal²/(2bd³Y).
2. Rearrange to find Y = 3gal²/(2bd³ × slope), using the fixed a, l, b, d for that run.
3. Cross-check using the l-sweep data: from the slope of e vs l², estimate Y independently.

## Result

*Table: Young's modulus of the beam material by uniform bending*

| Trial | a (cm) | l (cm) | Slope (mm/g) | Y (dyne/cm²) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |


## Maximum Permissible Error

As in the cantilever method, the beam thickness d enters cubed, so its measurement uncertainty (via a screw gauge) usually dominates the total error.

<div class="error-calc" data-exp="uniform-bending"></div>

## Precautions

- Load the two hangers with exactly equal weights at exactly equal overhangs, to preserve the symmetric, constant-bending-moment condition the formula assumes.
- Take microscope readings only after oscillations have died out and for both loading and unloading, averaging the two.
- Ensure the beam rests freely on the knife edges (not clamped), since the derivation assumes simply-supported, not built-in, end conditions.

## Self-Check Quiz

??? question "1. The bending moment between the two knife edges in uniform bending is:"
    - **A)** Zero
    - **B)** Constant along the whole span
    - **C)** Varying linearly along the span
    - **D)** Varying as the square of the distance

    **Answer: B** — This constancy is exactly why the method is called 'uniform' bending, and is why the beam bends into a circular arc between the supports.


??? question "2. If the knife-edge separation l is doubled (all else fixed), the elevation e:"
    - **A)** Doubles
    - **B)** Increases fourfold
    - **C)** Halves
    - **D)** Stays the same

    **Answer: B** — e ∝ l², so doubling l increases e by a factor of 4.


??? question "3. Compared to non-uniform (cantilever) bending, uniform bending measures deflection:"
    - **A)** At the clamped end
    - **B)** At the free end of a single cantilever
    - **C)** At the midpoint between two symmetrically loaded supports
    - **D)** At the knife edges themselves

    **Answer: C** — The midpoint elevation, relative to the (also slightly depressed) knife-edge supports, is what is measured in uniform bending.



## Viva-Voce Questions

1. Why is the bending moment constant between the knife edges in this experiment, whereas it varies along a cantilever?
2. What experimental conditions are essential to ensure the 'uniform' bending assumption actually holds?
3. Why does the elevation depend on the square of the knife-edge separation, rather than its cube as in the cantilever case?
4. How would you check, using your own data, whether the beam is within its elastic limit throughout the range of loads used?
5. Compare the sensitivity of Y to the thickness d in this method versus the cantilever method.
6. Why is symmetric loading (equal M, equal a on both sides) essential to the validity of the formula used?
