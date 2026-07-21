# 1. Bifilar Suspension — Moment of Inertia of a Rectangular Bar

!!! abstract "Module"
    Rotational Dynamics &middot; Module 1


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-bifilar){target=_blank}**

## Aim

To determine the moment of inertia of a rectangular bar about a vertical axis through its centre, using the torsional oscillations of a bifilar suspension.

## Theoretical Background

A bifilar suspension consists of a rigid horizontal bar hung from a fixed support by two parallel, inextensible threads of equal length, attached symmetrically at equal distances on either side of the bar's centre. When the bar is rotated slightly about the vertical axis through its centre and released, it executes torsional (yawing) oscillations in a horizontal plane while both threads remain taut.

As the bar twists through a small angle, each thread traces out a small cone about the vertical, and the vertical components of the thread tensions supply a restoring torque proportional to the angular displacement — so the motion is simple harmonic, exactly analogous to a torsion pendulum but with the 'spring constant' supplied entirely by gravity acting through the geometry of the suspension rather than by a twisting wire.

This makes the bifilar suspension a convenient, wire-free method for finding the moment of inertia of any object that can be clamped to the bar (aircraft and rocket engineers have historically used scaled-up versions of exactly this method to find the moment of inertia of real airframes and control surfaces about their yaw axis).

Because the restoring torque depends on the square of the half-separation *b* between the threads and inversely on the thread length *l*, both the geometry of the suspension and the object's own mass distribution enter the period — which is what allows the moment of inertia to be extracted from a purely timing measurement.

## Governing Formulas

**Period of torsional oscillation:**

$$
T = 2\pi\sqrt{\dfrac{I\,l}{M g b^{2}}}
$$

**Moment of inertia:**

$$
I = \dfrac{M g b^{2} T^{2}}{4\pi^{2} l}
$$

where $M$ is the mass of the bar, $l$ the length of each thread, $b$ the half-separation between the threads, and $T$ the period of torsional oscillation.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="105.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Rigid Support</text>
<rect x="210.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="275.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Two Parallel</text>
<text x="275.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Threads</text>
<rect x="380.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="445.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Suspended Bar</text>
<rect x="550.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="615.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Protractor</text>
<text x="615.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Scale</text>
<line x1="170.0" y1="100.0" x2="202.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="202.0,94.0 212.0,100.0 202.0,106.0" fill="#C97A27"/>
<line x1="340.0" y1="100.0" x2="372.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="372.0,94.0 382.0,100.0 372.0,106.0" fill="#C97A27"/>
<line x1="510.0" y1="100.0" x2="542.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="542.0,94.0 552.0,100.0 542.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A rigid bar suspended by two parallel vertical threads of equal length from a rigid horizontal support, free to oscillate torsionally about the vertical axis through its centre.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Thread length | l | 40 – 160 | cm |
| Half-separation of threads | b | 5 – 25 | cm |
| Mass of bar | M | 100 – 600 | g |


**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Period of oscillation | T | s |

## Procedure

1. Launch the Bifilar Suspension panel and note the default thread length, half-separation and bar mass.
2. Holding b and M fixed, vary the thread length l over its full range and record the period T shown on the readout for each setting.
3. Tabulate T² against l and verify that the points lie on a straight line through the origin, confirming T² ∝ l.
4. Now hold l fixed and vary the half-separation b; observe and note how the period changes.
5. From the slope of the T² vs l graph (at fixed b, M), calculate the moment of inertia I of the bar using the governing formula.

## Observation Table

*Table: Variation of period with thread length (b, M held constant)*

| S. No. | l (cm) | b (cm) | M (g) | Period T (s) — observed | T² (s²) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |


## Graph

Plot **T&sup2;** (y-axis) against **Thread length, l** (x-axis).

Expected trend: a straight line through the origin (T² ∝ l), since T² = (4π²I / Mgb²)·l.

*T² vs l, expected to be a straight line through the origin*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#14251C" font-family="Inter,Helvetica,sans-serif">T&sup2; vs Thread Length</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Thread length, l (cm)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">T&sup2; (s&sup2;)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. Compute the slope of the T² vs l graph: slope = 4π²I / (M g b²).
2. Rearrange to find I = slope × M g b² / 4π², using the fixed values of M and b used in that run.
3. Repeat with a different fixed b (holding l fixed while sweeping b, or using the b-sweep data) as a cross-check on I.

## Result

*Table: Moment of inertia of the bar about the vertical central axis*

| Trial | Slope of T² vs l (s²/cm) | M (g) | b (cm) | I (g·cm²) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |


## Maximum Permissible Error

I = Mgb²T²/(4π²l) is a product/quotient of measured quantities, with b and T entering squared — their fractional errors are doubled before summing.

<div class="error-calc" data-exp="bifilar-suspension"></div>

## Precautions

- Keep the angular amplitude of oscillation small so that the small-angle (simple-harmonic) approximation used in deriving the formula remains valid.
- Ensure both threads remain taut and parallel throughout the swing — a slack thread invalidates the restoring-torque derivation.
- Time a large number of oscillations (not just one) and divide, to reduce the fractional timing error.

## Self-Check Quiz

??? question "1. If the thread length l is doubled while b and M stay fixed, the period T:"
    - **A)** Doubles
    - **B)** Increases by a factor of √2
    - **C)** Halves
    - **D)** Stays the same

    **Answer: B** — T ∝ √l, so doubling l increases T by a factor of √2.


??? question "2. Doubling the half-separation b (all else fixed) causes the period T to:"
    - **A)** Double
    - **B)** Halve
    - **C)** Stay the same
    - **D)** Quadruple

    **Answer: B** — T ∝ 1/b, so doubling b halves the period — a wider suspension gives a stiffer restoring torque.


??? question "3. The restoring torque in a bifilar suspension arises fundamentally from:"
    - **A)** The elasticity of the threads
    - **B)** Gravity acting through the changing geometry of the two threads as the bar twists
    - **C)** Air resistance
    - **D)** Magnetic effects

    **Answer: B** — Unlike a torsion wire, the threads themselves do not twist elastically — the restoring torque comes purely from gravity via the geometric coupling of the two-thread suspension.



## Viva-Voce Questions

1. Why must the two threads be exactly parallel and equal in length before starting the experiment?
2. How would the period change if the bar's mass were doubled but its length (hence moment of inertia per unit mass) stayed the same?
3. Derive, in outline, why the restoring torque is proportional to the angular displacement for small twists.
4. What practical advantage does the bifilar method have over a torsional pendulum using a single twisted wire?
5. How would you extend this method to find the moment of inertia of an irregularly shaped object?
6. Why is it important to time many oscillations rather than a single one?
