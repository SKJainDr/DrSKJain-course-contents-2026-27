# 16. Ballistic Pendulum — Measuring an Unknown Launch Speed

!!! abstract "Module"
    Practical Applications &middot; Experiment 16


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-ballistic-pendulum){target=_blank}**

## Aim

To determine the launch speed of a projectile (ball) using a ballistic pendulum, by combining conservation of momentum during the (inelastic) impact with conservation of energy during the subsequent swing.

## Theoretical Background

A ballistic pendulum is a simple but historically important device (originally used to measure musket-ball speeds) for finding the speed of a fast-moving projectile that is too quick to time directly over a short distance. A projectile of mass m, moving horizontally with speed v, embeds itself in a much larger stationary pendulum block of mass M suspended by a light rod or string of length L. The collision is perfectly inelastic — the combined mass (M+m) moves off together immediately after impact — so only momentum, not kinetic energy, is conserved during the collision itself.

Once the combined mass is moving, the problem becomes an ordinary energy-conservation one: the kinetic energy of the combined mass immediately after impact is entirely converted into gravitational potential energy as the pendulum swings up through some maximum angle θ, momentarily coming to rest at the top of its swing before falling back. This two-stage analysis — momentum conservation for the sudden, violent collision, followed by energy conservation for the comparatively gentle swing — is a classic technique that appears throughout mechanics whenever a fast, irreversible interaction is followed by a slower, conservative one, from vehicle-crash reconstruction to the recoil analysis of firearms.

Because the rise height h (or, equivalently, the swing angle θ) can be measured far more easily and precisely than a very short time-of-flight, the ballistic pendulum converts a hard "how fast?" measurement into an easy "how high?" one.

## Governing Formulas

**Momentum conservation during impact (perfectly inelastic collision):**

$$
mv = (M+m)v'
$$

**Energy conservation during the swing (v′ is the speed immediately after impact):**

$$
\tfrac{1}{2}(M+m)v'^{2} = (M+m)gh \quad\Rightarrow\quad v' = \sqrt{2gh}
$$

**Combining both stages, the launch speed in terms of directly measurable quantities:**

$$
v = \dfrac{M+m}{m}\sqrt{2gh}, \qquad 1-\cos\theta = \dfrac{m^{2}v^{2}}{2gL(M+m)^{2}}
$$

where $m$ is the projectile mass, $M$ the pendulum block mass, $h$ the vertical rise of the block after impact, $L$ the pendulum length, and $\theta$ the maximum swing angle (so that $h = L(1-\cos\theta)$).

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Spring-Gun</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Launcher</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Suspended</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Block (M)</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Angle Scale</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">/ Ratchet Pawl</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#C97A27"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A spring-loaded launcher fires a small ball horizontally into a suspended, catching pendulum block; a ratchet pawl holds the block at its maximum swing angle for reading off an angle scale.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Launch speed | v | 2 – 8 | m/s |
| Ball (projectile) mass | m | 5 – 50 | g |
| Pendulum block mass | M | 200 – 1000 | g |
| Pendulum length | L | 20 – 60 | cm |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Maximum swing angle | θ_max | ° |
| Rise height | h | cm |
| Reconstructed launch speed (check) | v (calc) | m/s |

## Procedure

1. Launch the Ballistic Pendulum panel; set the ball mass m, block mass M and pendulum length L to fixed values for a given trial series.
2. Adjust the launch speed slider v (representing a different spring-gun setting or cartridge) and record the resulting swing angle θ_max and rise height h.
3. Repeat for at least five different values of the ball mass m, holding M, L and v fixed, tabulating h each time.
4. For each trial, reconstruct the launch speed from your recorded h using the governing formula and compare it with the slider's actual value — this is the built-in consistency check for the method.
5. Note how h changes as you vary each control in turn, to build physical intuition for the formula's dependence on m, M and L.

## Observation Table

*Table: Variation of rise height with ball mass, at fixed launch speed v, block mass M and length L*

| S. No. | m (g) | M (g) | L (cm) | θ_max (°) | h (cm) | Reconstructed v (m/s) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |


## Graph

Plot **Rise height, h** (y-axis) against **Ball mass, m** (x-axis).

Expected trend: an increasing, slightly curved trend — a heavier ball carries more momentum at the same launch speed, so it swings the block-plus-ball combination higher, though the effect saturates once m becomes comparable to M.

*h vs m, used to visualize how momentum transfer scales with projectile mass*

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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Ball mass, m (g)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Rise height, h (cm)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each trial, compute h from the observed swing angle θ_max using $h = L(1-\cos\theta_{max})$.
2. Using h, m, M and L, compute the reconstructed launch speed v from the governing formula.
3. Compare the reconstructed v with the slider's actual value in each trial and compute the percentage discrepancy.

## Result

*Table: Launch speed determined by the ballistic pendulum method*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

v = [(M+m)/m]·√(2gh) depends on h only through a square root, so h contributes half its fractional error, while the mass ratio (M+m)/m contributes its own fractional errors directly.

<div class="error-calc" data-exp="ballistic-pendulum"></div>

## Precautions

- Ensure the ball embeds fully and instantaneously in the block (a perfectly inelastic collision) rather than bouncing off or passing through.
- Read the maximum swing angle at the highest point of the very first swing, before any energy is lost to air resistance or pivot friction on subsequent swings.
- Keep the pendulum's initial position exactly vertical (θ=0) before each trial, and make sure the ball's velocity is horizontal at the moment of impact.

## Self-Check Quiz

??? question "1. During the collision between the ball and the block, which quantity is conserved?"
    - **A)** Kinetic energy only
    - **B)** Momentum only
    - **C)** Both momentum and kinetic energy
    - **D)** Neither

    **Answer: B** — The collision is perfectly inelastic (the ball embeds in the block), so kinetic energy is lost to deformation/heat, but momentum is always conserved in any collision, inelastic or not.


??? question "2. If the pendulum block's mass M is made very much larger than the ball's mass m (all else fixed), the rise height h will:"
    - **A)** Increase without bound
    - **B)** Approach zero
    - **C)** Stay exactly the same
    - **D)** Become negative

    **Answer: B** — As M→∞ with m and v fixed, v′=mv/(M+m)→0, so essentially none of the ball's kinetic energy is transferred to the (now nearly immovable) block, and h→0.


??? question "3. Why is a ballistic pendulum useful for measuring speeds that are too fast to time directly?"
    - **A)** It converts a hard "how fast" measurement into an easier "how high" (or "what angle") measurement
    - **B)** It stops time itself
    - **C)** It only works for slow projectiles
    - **D)** It measures speed using a stopwatch on the ball's flight

    **Answer: A** — The swing height/angle can be read at leisure after the ball has already stopped moving relative to the block, unlike the projectile's original brief flight.


## Viva-Voce Questions

1. Why must momentum conservation and energy conservation be applied in two separate stages here, rather than one energy-conservation equation for the whole process?
2. What physically happens to the "missing" kinetic energy that is not accounted for by energy conservation during the collision itself?
3. How would the result change if the ball only partially embedded and continued moving after passing through the block?
4. Why is it important to release the ball with a purely horizontal velocity, exactly at the pendulum's rest height?
5. Give one real-world application of the general technique (fast-collision-then-observe-the-slow-aftermath) used here.
6. How would friction at the pendulum's pivot bias your calculated launch speed — would it read too high or too low?
