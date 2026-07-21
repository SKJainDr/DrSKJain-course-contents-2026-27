# 4. Compound (Bar) Pendulum — Acceleration due to Gravity and Radius of Gyration

!!! abstract "Module"
    Rotational Dynamics &middot; Module 1


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-compound-pendulum){target=_blank}**

## Aim

To determine the acceleration due to gravity g and the radius of gyration k of a uniform bar pendulum, using the method of conjugate points.

## Theoretical Background

A compound (or physical) pendulum is any rigid body free to oscillate about a fixed horizontal axis that does not pass through its centre of gravity — unlike the idealised simple pendulum, its mass is distributed rather than concentrated at a point. A uniform metre bar with a series of holes drilled along its length, suspended from a knife edge through any one hole, is the standard laboratory realisation.

For small oscillations, the period depends on the distance h from the pivot to the centre of gravity and on the body's radius of gyration k about an axis through the centre of gravity parallel to the pivot axis. Crucially, the same period T is obtained for two different pivot points — one on each side of the centre of gravity — whenever their distances h₁ and h₂ from the centre satisfy h₁h₂ = k². These two points are called conjugate points, and the distance between them, L = h₁ + h₂, is exactly the length of the simple pendulum that would have the same period T.

This equivalence is the basis of Kater's reversible pendulum, historically one of the most accurate methods ever devised for measuring g, since L can be measured directly with a scale (avoiding the need to separately know the body's mass distribution), while g follows from the simple-pendulum formula T = 2π√(L/g).

Once g is known (or assumed from a standard value), the same data — the period as a function of pivot distance h — can be inverted to extract the radius of gyration k, characterising how the bar's mass is distributed about its centre.

## Governing Formulas

**Period about a pivot at distance h from the centre of gravity:**

$$
T = 2\pi\sqrt{\dfrac{k^{2}+h^{2}}{g h}}
$$

**Conjugate points (equal period on either side of the C.G.):**

$$
h_{1}h_{2} = k^{2}, \qquad L = h_{1}+h_{2}
$$

**Acceleration due to gravity:**

$$
g = \dfrac{4\pi^{2} L}{T^{2}}
$$

**Radius of gyration:** $k = \sqrt{h_{1}h_{2}}$

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="82.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="147.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Knife-Edge</text>
<text x="147.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Support</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Drilled Bar</text>
<rect x="507.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="572.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Stopwatch</text>
<text x="572.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Timing</text>
<line x1="212.5" y1="100.0" x2="287.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="287.0,94.0 297.0,100.0 287.0,106.0" fill="#C97A27"/>
<line x1="425.0" y1="100.0" x2="499.5" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="499.5,94.0 509.5,100.0 499.5,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A uniform metal bar with a series of equally spaced holes along its length, suspended from a fixed knife-edge support through any chosen hole so it can swing freely in a vertical plane.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Pivot distance from C.G. | h | 5 – 45 | cm |
| Bar length | l_bar | 80 – 120 | cm |


**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Period | T | s |

## Procedure

1. Launch the Compound Pendulum panel and set the bar length to its default value.
2. Sweep the pivot distance h from small values near the centre of gravity out to near the end of the bar, recording the period T at each setting.
3. Plot T against h; the curve is U-shaped with a minimum, and for any horizontal line drawn above the minimum there are two intersection points — the conjugate points.
4. Identify a pair of conjugate points (h₁ on one side, h₂ on the other) with matching periods, and compute L = h₁ + h₂.
5. Using the common period T of the conjugate points, compute g from the simple-pendulum-equivalent formula, and k from h₁h₂ = k².

## Observation Table

*Table: Period as a function of pivot distance from the centre of gravity*

| S. No. | h (cm) | Period T (s) | T² (s²) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |


## Graph

Plot **Period, T** (y-axis) against **Pivot distance, h** (x-axis).

Expected trend: a U-shaped curve with a minimum, symmetric about the true centre of gravity when h is allowed to be negative on the other side.

*T vs h — locate conjugate points as equal-T pairs on either side of the minimum*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Period vs Pivot Distance</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Pivot distance, h (cm)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Period, T (s)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. From the T vs h graph, identify at least two pairs of conjugate points with matching T.
2. For each pair, compute L = h₁ + h₂ and the corresponding g = 4π²L/T².
3. Average the values of g obtained from different conjugate pairs, and similarly compute k = √(h₁h₂) for each pair.

## Result

*Table: Acceleration due to gravity and radius of gyration*

| Conjugate pair | h₁ (cm) | h₂ (cm) | T (s) | g (cm/s²) | k (cm) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |


## Maximum Permissible Error

g = 4π²L/T² depends on T squared, so timing precision (usually via timing many oscillations) dominates the error budget more than the length measurement L.

<div class="error-calc" data-exp="compound-pendulum"></div>

## Precautions

- Ensure the knife edge is horizontal and the bar swings in a single vertical plane, without any side-to-side wobble.
- Keep the angular amplitude small (a few degrees) so the small-angle approximation underlying the SHM formula remains valid.
- Locate conjugate points carefully — the period curve is fairly flat near the minimum, so small timing errors can shift the apparent location of matching-T points significantly there; prefer pairs well away from the minimum.

## Self-Check Quiz

??? question "1. At the two conjugate points on either side of the centre of gravity, the compound pendulum has:"
    - **A)** Different periods but the same k
    - **B)** The same period, for that pair of pivot distances
    - **C)** Zero period
    - **D)** Infinite period

    **Answer: B** — Conjugate points are defined precisely as the pair of pivot distances (one on each side of the C.G.) that give the same period.


??? question "2. As the pivot approaches the centre of gravity (h → 0), the period T:"
    - **A)** Approaches zero
    - **B)** Approaches a finite minimum value
    - **C)** Diverges to infinity
    - **D)** Stays exactly constant

    **Answer: C** — T = 2π√((k²+h²)/gh) → ∞ as h → 0, because the restoring torque (∝ h) vanishes while the moment of inertia does not — physically, a pivot exactly at the C.G. gives no gravitational restoring torque at all.


??? question "3. The compound pendulum method for measuring g has a practical advantage over a simple pendulum because:"
    - **A)** It requires no timing at all
    - **B)** The equivalent length L can be measured directly and accurately as a distance along the bar, without needing to locate the pendulum's effective centre of oscillation by any other means
    - **C)** It does not obey Newton's laws
    - **D)** It is always faster to perform

    **Answer: B** — This is exactly the insight behind Kater's reversible pendulum — L is a directly measurable geometric distance, side-stepping uncertainty in the internal mass distribution.



## Viva-Voce Questions

1. Why does the compound pendulum have a minimum period at some pivot distance rather than at the centre of gravity itself?
2. What physically defines a pair of conjugate points, and why must L = h₁+h₂ equal the equivalent simple pendulum length?
3. How is Kater's reversible pendulum related to this experiment, and why was it historically important?
4. Why would timing 20 or 50 oscillations, rather than one, substantially improve the accuracy of g?
5. How would the T vs h curve change if the bar were replaced by one of the same length but different mass distribution (e.g. with added end masses)?
6. What would happen to the period if the bar were pivoted exactly at its centre of gravity?
