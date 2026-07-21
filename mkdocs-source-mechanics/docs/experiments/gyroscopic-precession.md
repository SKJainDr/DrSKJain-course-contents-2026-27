# 18. Gyroscopic Precession — Spin, Torque and Steady Precession

!!! abstract "Module"
    Practical Applications &middot; Experiment 18


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-gyroscope){target=_blank}**

## Aim

To study the steady precession of a rapidly spinning wheel under an applied gravitational torque, and to verify that the precession rate is inversely proportional to the spin rate.

## Theoretical Background

A rapidly spinning wheel possesses a large spin angular momentum $L = I\omega$ directed along its axle, where I is the wheel's moment of inertia about that axle and ω its spin rate. If the wheel's centre of gravity is offset by a small distance d from its pivot point, gravity exerts a torque $\tau = Mgd$ about the pivot, where M is the wheel's mass.

Naively, one might expect this torque to simply tip the wheel over, rotating its axle downward in the direction of the torque. Instead, because angular momentum is a vector and torque causes the angular momentum vector to change according to $\vec{\tau} = d\vec{L}/dt$, the axle instead sweeps around slowly in a horizontal circle — a motion called precession — while the wheel continues to spin rapidly about its own axle exactly as before. This counter-intuitive behaviour is the essence of gyroscopic motion, and for a rapidly spinning wheel with a small, steady torque, the precession settles into a steady rate

$$
\Omega = \dfrac{\tau}{L} = \dfrac{Mgd}{I\omega}
$$

For a disc-shaped wheel with $I = \tfrac{1}{2}MR^{2}$, the wheel's own mass M cancels out of this expression entirely, leaving $\Omega = 2gd/(R^{2}\omega)$ — the precession rate depends only on the wheel's radius, its spin rate, and the offset distance, not on how heavy the wheel is. This single fact — that a faster-spinning gyroscope precesses more slowly and resists tipping more strongly — is exploited in every mechanical gyrocompass, in the natural self-stability of a fast-spinning bicycle or motorcycle wheel, and in the reaction wheels used to orient spacecraft without any external thruster fuel.

## Governing Formulas

**Spin angular momentum and applied torque:**

$$
L = I\omega = \tfrac{1}{2}MR^{2}\omega, \qquad \tau = Mgd
$$

**Steady precession rate:**

$$
\Omega = \dfrac{\tau}{L} = \dfrac{2gd}{R^{2}\omega}
$$

**Precession period:**

$$
T_{\text{prec}} = \dfrac{2\pi}{\Omega}
$$

where M and R are the spinning wheel's mass and radius, ω its spin rate about its own axle, and d the offset of its centre of gravity from the pivot.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Spinning</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Wheel (M, R)</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Gimbal &amp;</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Pivot Point</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Precession-Angle</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Stopwatch/Scale</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#C97A27"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A wheel is spun up about its own axle and mounted so its centre of gravity is offset from a fixed pivot; the axle then precesses slowly around the pivot, timed with a stopwatch and angle scale.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Wheel mass | M | 100 – 500 | g |
| Wheel radius | R | 3 – 8 | cm |
| Spin rate | ω | 5 – 60 | rad/s |
| C.G. offset from pivot | d | 2 – 10 | cm |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Spin angular momentum | L | g·cm²/s |
| Precession rate | Ω | rad/s |
| Precession period | T | s |

## Procedure

1. Launch the Gyroscopic Precession panel; set the wheel mass M, radius R and offset d to fixed values.
2. Vary the spin rate ω and record the resulting precession rate Ω and precession period T from the readouts.
3. Repeat for at least five different values of ω, keeping M, R and d fixed, tabulating Ω each time.
4. Verify that the product Ω·ω remains approximately constant across your trials (since Ω ∝ 1/ω) — this is the key experimental signature of steady gyroscopic precession.
5. Repeat the whole sweep with a different wheel radius R, and confirm that Ω changes as 1/R² while the wheel mass M has no effect on Ω.

## Observation Table

*Table: Variation of precession rate with spin rate, at fixed wheel mass, radius and offset*

| S. No. | M (g) | R (cm) | d (cm) | ω (rad/s) | Ω (rad/s) | Ω·ω (check, ≈ constant) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |


## Graph

Plot **Precession rate, Ω** (y-axis) against **Spin rate, ω** (x-axis).

Expected trend: a falling, hyperbola-like curve (Ω ∝ 1/ω) — spin the wheel faster and it precesses more slowly and more steadily.

*Ω vs ω, illustrating the inverse relationship between spin and precession rates*

<div class="apparatus-3d-wrap graph-wrap" style="background:#FFFBF0;padding:10px;" markdown="1">
<div class="graph-toolbar" markdown="0">
  <span class="graph-hint">&#128203; Click the grid, then paste (Ctrl+V) a copied photo of your camera/DSO/graph trace to overlay it for tracing &mdash; nothing is uploaded, it stays on your screen only.</span>
  <span class="graph-toolbar-controls">
    <label>Overlay opacity <input type="range" class="graph-opacity" min="10" max="100" value="65"></label>
    <button type="button" class="graph-clear-btn">Clear pasted image</button>
  </span>
</div>
<div class="graph-canvas-wrap" tabindex="0" title="Click here, then press Ctrl+V to paste your camera/DSO image">
<svg viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#FFFBF0;">
<rect x="0" y="0" width="640" height="520" fill="#FFFBF0"/>
<line x1="106.67" y1="40.0" x2="106.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="143.33" y1="40.0" x2="143.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="180.00" y1="40.0" x2="180.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="216.67" y1="40.0" x2="216.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="290.00" y1="40.0" x2="290.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="326.67" y1="40.0" x2="326.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="363.33" y1="40.0" x2="363.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="400.00" y1="40.0" x2="400.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="473.33" y1="40.0" x2="473.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="510.00" y1="40.0" x2="510.00" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="546.67" y1="40.0" x2="546.67" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="583.33" y1="40.0" x2="583.33" y2="465.0" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="68.33" x2="620.0" y2="68.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="96.67" x2="620.0" y2="96.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="125.00" x2="620.0" y2="125.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="153.33" x2="620.0" y2="153.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="210.00" x2="620.0" y2="210.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="238.33" x2="620.0" y2="238.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="266.67" x2="620.0" y2="266.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="295.00" x2="620.0" y2="295.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="351.67" x2="620.0" y2="351.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="380.00" x2="620.0" y2="380.00" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="408.33" x2="620.0" y2="408.33" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.0" y1="436.67" x2="620.0" y2="436.67" stroke="#D9C9A3" stroke-width="0.6"/>
<line x1="70.00" y1="40.0" x2="70.00" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="620.00" y1="40.0" x2="620.00" y2="465.0" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="40.00" x2="620.0" y2="40.00" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="465.00" x2="620.0" y2="465.00" stroke="#1F6E43" stroke-width="1.1" stroke-opacity="0.55"/>
<rect x="70.0" y="40.0" width="550.0" height="425.0" fill="none" stroke="#14251C" stroke-width="2"/>
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Spin rate, &omega; (rad/s)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Precession rate, &Omega; (rad/s)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each trial, compute the spin angular momentum L = ½MR²ω and the applied torque τ = Mgd.
2. Compute the precession rate Ω = τ/L for each trial and compare it with the simulator's readout.
3. Verify that Ω·ω is approximately constant across your sweep of ω, confirming the inverse relationship.

## Result

*Table: Precession behaviour of the gyroscope*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

Since Ω = 2gd/(R²ω), the wheel radius R enters squared — the least-count error of whatever instrument measures R (often a vernier caliper) usually dominates the overall uncertainty in Ω.

<div class="error-calc" data-exp="gyroscopic-precession"></div>

## Precautions

- Bring the wheel up to a steady, constant spin rate before releasing it to precess — the steady-precession formula assumes ω is essentially unchanging over the timescale of one precession cycle.
- Keep the offset distance d small compared with the wheel radius R, so that the "fast-spin, slow-precession" approximation used in the governing formula remains valid.
- Support the pivot itself as friction-free as possible, since pivot friction introduces an additional torque that is not accounted for in the ideal formula.

## Self-Check Quiz

??? question "1. If the spin rate ω of the wheel is doubled (all else fixed), the precession rate Ω becomes:"
    - **A)** Doubled
    - **B)** Halved
    - **C)** Unchanged
    - **D)** Quadrupled

    **Answer: B** — Since Ω = 2gd/(R²ω), Ω is inversely proportional to ω, so doubling ω halves Ω.


??? question "2. Why does the wheel's own mass M cancel out of the precession-rate formula for a disc-shaped wheel?"
    - **A)** Because both the spin angular momentum L and the applied torque τ are directly proportional to M, so M cancels in their ratio
    - **B)** Because gravity does not act on spinning objects
    - **C)** Because the formula is only an approximation that happens to ignore mass
    - **D)** It does not actually cancel; the statement is false

    **Answer: A** — L = ½MR²ω and τ = Mgd are both proportional to M, so Ω = τ/L cancels M exactly, leaving only R, ω, d and g.


??? question "3. A fast-spinning gyroscope resists tipping over more strongly than a slow-spinning one because:"
    - **A)** It has more kinetic energy, which somehow opposes gravity directly
    - **B)** Its larger angular momentum L means the same torque produces a smaller rate of change of the angular momentum's direction (a smaller Ω)
    - **C)** Faster spinning reduces its weight
    - **D)** There is no real difference; spin rate is irrelevant to stability

    **Answer: B** — Torque changes the direction of L at a rate Ω=τ/L; a larger L (from faster spin) means the same torque redirects the angular momentum vector more slowly, i.e., the gyroscope precesses (tips) more slowly.


## Viva-Voce Questions

1. Why does an applied torque on a spinning gyroscope cause it to precess sideways rather than simply falling over in the direction of the torque?
2. Derive, in outline, why the precession rate Ω is inversely proportional to the spin rate ω.
3. Why does the wheel's mass drop out of the precession formula for a disc, and would it drop out for a different mass distribution (e.g., a hoop)?
4. Give one real engineering application where gyroscopic precession is deliberately exploited (not merely tolerated), and explain the underlying principle.
5. How would you expect the results to change if the wheel were spun in the opposite direction?
6. What would happen to the precession rate if the spin rate ω were allowed to slowly decay due to friction, over a long observation time?
