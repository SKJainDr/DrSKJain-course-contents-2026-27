# 17. Rolling Race on an Incline — Moment of Inertia and Rolling Efficiency

!!! abstract "Module"
    Practical Applications &middot; Experiment 17


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-rolling-race){target=_blank}**

## Aim

To study how the mass distribution of a rolling body (characterized by its moment-of-inertia factor k) governs its acceleration down an incline, and to verify the theoretical prediction that a solid disc or sphere always outpaces a ring or hoop released from rest at the same height.

## Theoretical Background

When a rigid body of mass m and radius r rolls without slipping down an incline of angle θ, gravity does work on its centre of mass, and that work is shared between translational kinetic energy of the centre of mass and rotational kinetic energy about the body's own axis. Writing the moment of inertia as $I = kmr^{2}$, where k is a dimensionless shape factor (k=1 for a thin ring/hoop, k=½ for a solid disc or cylinder, k=⅖ for a solid sphere, k=⅔ for a thin hollow sphere), energy conservation for rolling without slipping gives an acceleration down the slope of

$$
a = \dfrac{g\sin\theta}{1+k}
$$

Crucially, this acceleration does not depend on the body's mass or radius at all — only on its shape, through k. A larger k means more of the body's mass sits farther from the rolling axis (as in a hoop, where essentially all the mass is at the rim), so a larger fraction of the released potential energy is diverted into spinning rather than forward motion, and the body accelerates more slowly.

This is exactly why, in the classic demonstration of releasing a solid ball and a hoop from the top of a ramp at the same instant, the solid ball always wins the race — regardless of their individual masses or sizes — a fact with real engineering consequences: flywheels, vehicle wheels, and rotating drums are deliberately designed with specific mass distributions (k values) to trade off rotational inertia (useful for energy storage or smoothing) against translational responsiveness (useful for acceleration and fuel efficiency).

## Governing Formulas

**Rolling acceleration down the incline:**

$$
a = \dfrac{g\sin\theta}{1+k}, \qquad I = kmr^{2}
$$

**Time to travel a distance L along the slope, starting from rest:**

$$
t = \sqrt{\dfrac{2L}{a}}
$$

**Speed on reaching the bottom:**

$$
v = at = \sqrt{\dfrac{2gh}{1+k}}, \qquad h = L\sin\theta
$$

where θ is the incline angle, L the distance travelled along the slope, and k the shape factor of the rolling body (1 for a ring, ½ for a disc/cylinder, ⅖ for a solid sphere, ⅔ for a hollow sphere).

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Adjustable</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Incline (θ)</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Ring / Disc /</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Sphere Set</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Photogate /</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Stopwatch</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#C97A27"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). An incline of adjustable angle, a set of interchangeable rolling bodies (ring, disc, solid sphere, hollow sphere) of similar overall size, and a timer to record the descent.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Shape (moment-of-inertia factor) | k | {1, 0.5, 0.4, 0.667} | — |
| Incline angle | θ | 10 – 40 | ° |
| Incline length (along slope) | L | 50 – 200 | cm |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Acceleration | a | cm/s² |
| Time to reach bottom | t | s |
| Speed at bottom | v | cm/s |

## Procedure

1. Launch the Rolling Race panel; select a shape (ring, disc/cylinder, solid sphere, or hollow sphere) and set the incline angle θ and slope length L.
2. Record the time to reach the bottom, t, shown on the readout.
3. Repeat for at least five different incline angles θ, keeping the shape and L fixed, tabulating t each time.
4. Repeat the whole sweep for a second, different shape, and compare the two sets of times at the same angles — the shape with the larger k should consistently take longer.
5. For each trial, compute a = 2L/t² from your timed data, then compare this experimental k (from a = g sinθ/(1+k)) against the theoretical value for that shape.

## Observation Table

*Table: Variation of descent time with incline angle, for a fixed rolling shape*

| S. No. | Shape (k) | θ (°) | L (cm) | t (s) | a = 2L/t² (cm/s²) | k (experimental) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |


## Graph

Plot **Time to reach bottom, t** (y-axis) against **Incline angle, θ** (x-axis).

Expected trend: a decreasing curve for every shape — steeper inclines shorten the descent — with the ring/hoop's curve lying consistently above the disc's or sphere's curve at every angle.

*t vs θ, compared across at least two different rolling shapes*

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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Incline angle, &theta; (&deg;)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Time to reach bottom, t (s)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each trial, compute the experimental acceleration a = 2L/t² from your timed data.
2. From a = g sinθ/(1+k), solve for the experimental k and compare it with the theoretical value for that shape.
3. Compute the percentage deviation between your experimental and theoretical k for each shape tested.

## Result

*Table: Experimental moment-of-inertia factor k for each rolling shape tested*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

The moment-of-inertia factor k is inferred from the measured acceleration a = g sinθ/(1+k); since a is obtained from the timed run (a = 2L/t²), the fall time t enters squared and usually dominates the error budget.

<div class="error-calc" data-exp="rolling-race-incline"></div>

## Precautions

- Release each rolling body from rest with no initial push, and from exactly the same starting point on the incline for every trial.
- Ensure genuine rolling without slipping throughout — a very smooth/oily incline surface can let the body slide rather than roll, invalidating the energy-conservation formula used here.
- Use rolling bodies of similar overall size so that air resistance and rolling friction remain comparably small across the shapes being compared.

## Self-Check Quiz

??? question "1. Between a solid sphere and a solid disc released from the same height on the same incline, which reaches the bottom first?"
    - **A)** The disc
    - **B)** The sphere
    - **C)** They arrive at exactly the same time
    - **D)** It depends on their masses

    **Answer: B** — The sphere has the smaller k (⅖ vs ½), so more of its energy goes into translation and less into rotation, giving it a larger acceleration.


??? question "2. Why does the rolling acceleration a = g sinθ/(1+k) not depend on the mass or radius of the rolling body?"
    - **A)** Because mass and radius cancel out of the energy-conservation equation when I is written as kmr²
    - **B)** Because gravity does not act on rotating bodies
    - **C)** Because friction exactly cancels the effect of mass
    - **D)** It does depend on them; the formula is only approximate

    **Answer: A** — Both the translational and rotational kinetic energy terms are proportional to m (and, via I=kmr², to r² as well), so these factors cancel completely, leaving a that depends only on θ and the shape factor k.


??? question "3. A hollow cylinder (thin pipe) and a solid cylinder of the same outer radius are released together. Which one reaches the bottom first?"
    - **A)** The hollow cylinder
    - **B)** The solid cylinder
    - **C)** Both arrive together
    - **D)** Neither moves

    **Answer: B** — The hollow cylinder has all its mass concentrated near the rim (higher k, closer to that of a ring), so more of its energy is diverted into rotation, making it slower than the solid cylinder (k=½).


## Viva-Voce Questions

1. Why is "rolling without slipping" essential to the formula used here, and what would go wrong if the body slid instead?
2. Explain, in terms of energy sharing, why a hoop always loses a rolling race to a solid disc of the same mass and radius.
3. How could you experimentally verify that a given ball is solid rather than hollow, using only this incline and a stopwatch?
4. Why is the mass of the rolling body absent from the final formula for acceleration, even though gravity clearly depends on mass?
5. Name one piece of real machinery (a flywheel, a vehicle wheel, an industrial roller) where the designer's choice of k has a genuine practical consequence, and explain why.
6. How would rolling friction (a small resistive torque at the contact point) bias your experimentally determined k — too high or too low?
