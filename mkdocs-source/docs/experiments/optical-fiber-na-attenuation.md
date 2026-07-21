# 17. Optical Fiber — Numerical Aperture & Attenuation

!!! abstract "Module"
    Practical Applications

!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-fiberoptic){target=_blank}**

## Aim

To determine the Numerical Aperture and acceptance angle of a step-index optical fiber from its core and cladding refractive indices, and to study how signal power decays exponentially with distance due to fiber attenuation.

## Theoretical Background

A step-index optical fiber guides light along its core by total internal reflection at the core-cladding boundary. For total internal reflection to occur at all, light must be launched into the fiber's end-face within a limited cone of angles — the **acceptance cone** — outside of which the ray strikes the core-cladding interface at too shallow an angle and escapes into the cladding instead of being guided.

The **Numerical Aperture (NA)** quantifies the size of this acceptance cone in terms of the core and cladding refractive indices, n₁ and n₂ respectively (with n₁ slightly greater than n₂, so that total internal reflection is possible at all). A larger NA means the fiber can accept light launched over a wider range of angles — useful for coupling light in efficiently from an incoherent or poorly-collimated source — but a larger core-cladding index contrast typically also supports more distinct guided modes, which travel at slightly different effective speeds and so worsens modal dispersion (pulse spreading) over long distances.

Independently of how the light is launched, once guided, the signal's power decreases exponentially with the distance travelled, characterized by the fiber's **attenuation coefficient**, usually quoted in decibels per kilometre (dB/km). This attenuation, not NA, is what ultimately limits how far a signal can travel down a real telecommunications fiber before it must be optically or electronically amplified/regenerated.

## Governing Formulas

**Numerical Aperture and acceptance angle (light launched from air, n₀=1):**

$$
\text{NA} = \sqrt{n_1^{2}-n_2^{2}} = n_0\sin\theta_a
$$

**Power attenuation over a fiber of length L, with attenuation coefficient α (dB/km):**

$$
P_{out} = P_{in}\times 10^{-\alpha L/10}
$$

where n₁ and n₂ are the core and cladding refractive indices, θ_a the acceptance angle in air, and α L the total attenuation in decibels.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#a8452f" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Laser Diode</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Source</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#2ec4c6" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Fiber Under Test</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">(Core + Cladding)</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#2ec4c6" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Optical Power</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Meter</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#a8452f" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#a8452f"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#2ec4c6" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#2ec4c6"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). Light from a laser diode is launched into a fiber of known core/cladding index and length, and the transmitted power is measured at the far end with a calibrated power meter.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Core refractive index | n₁ | 1.44 – 1.50 | — |
| Cladding refractive index | n₂ | 1.40 – 1.49 | — |
| Fiber length | L | 0.5 – 50 | km |
| Attenuation coefficient | α | 0.2 – 3 | dB/km |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Numerical Aperture | NA | — |
| Acceptance angle | θ_a | ° |
| Output power (1 mW input) | P_out | µW |

## Procedure

1. Launch the Optical Fiber panel; set the core index n₁ and cladding index n₂ to represent a chosen fiber type, and note the computed NA and acceptance angle.
2. Repeat for at least five different (n₁, n₂) combinations, holding the difference n₁−n₂ deliberately varied, and tabulate NA each time.
3. Fix n₁ and n₂, then vary the fiber length L at a fixed attenuation coefficient α, recording the output power P_out for a 1 mW input at each length.
4. Repeat the length sweep for a second, larger value of α (representing a poorer-quality or multimode fiber) and compare the two power-decay curves.
5. Plot P_out against L on a logarithmic vertical scale and verify that it forms a straight line, confirming the exponential (dB-linear) nature of the attenuation.

## Observation Table

*Table: Variation of output power with fiber length, at fixed core/cladding indices and attenuation coefficient*

| S. No. | n₁ | n₂ | NA | α (dB/km) | L (km) | P_out (µW, 1 mW input) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |


## Graph

Plot **Output power, P_out** (y-axis, logarithmic scale) against **Fiber length, L** (x-axis).

Expected trend: a straight line on a log-power axis, since P_out(dB) decreases linearly with L at rate α — the defining signature of exponential attenuation.

*log(P_out) vs L, at two different attenuation coefficients for comparison*

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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Fiber length, L (km)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Output power, P&#8320;ᵤₜ (&micro;W, log scale)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each (n₁, n₂) pair, compute NA = √(n₁²−n₂²) and the acceptance angle θ_a = sin⁻¹(NA).
2. For each length L, compute the output power P_out = P_in × 10^(−αL/10) for a 1 mW input.
3. From the slope of your log(P_out) vs L graph, verify that it equals the attenuation coefficient α used.

## Result

*Table: Numerical Aperture and attenuation behaviour of the simulated fiber*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

NA = √(n₁²−n₂²); since NA is a square root of a difference of squares, its absolute error is dominated by whichever refractive index (core or cladding) carries the larger measurement uncertainty, weighted by that index's own value.

<div class="error-calc" data-exp="optical-fiber-na-attenuation"></div>

## Precautions

- Keep n₁ strictly greater than n₂ at all times — if the core index ever falls below (or equal to) the cladding index, total internal reflection is impossible and the fiber cannot guide light at all.
- Ensure the launch spot is well-centred on the fiber core; light launched partly into the cladding is lost immediately and does not represent the fiber's true NA.
- When comparing attenuation at different lengths, keep the same launch conditions (spot size, angle, alignment) so that only the fiber length itself is being varied.

## Self-Check Quiz

??? question "1. What happens to a ray launched at an angle greater than the fiber's acceptance angle θ_a?"
    - **A)** It is guided down the fiber core as usual
    - **B)** It escapes into the cladding and is lost
    - **C)** It reverses direction and exits back out the input face
    - **D)** It travels faster than rays within the acceptance cone

    **Answer: B** — Rays outside the acceptance cone strike the core-cladding boundary at too shallow an angle for total internal reflection, so they refract out into the cladding instead of being guided.


??? question "2. Increasing the core-cladding index difference (n₁−n₂) while keeping n₁ fixed will:"
    - **A)** Decrease the Numerical Aperture
    - **B)** Increase the Numerical Aperture
    - **C)** Leave the Numerical Aperture unchanged
    - **D)** Make total internal reflection impossible

    **Answer: B** — NA = √(n₁²−n₂²) increases as n₂ decreases (with n₁ fixed), widening the acceptance cone.


??? question "3. If a fiber has an attenuation coefficient of 3 dB/km, what fraction of the input power remains after 10 km?"
    - **A)** About 50%
    - **B)** About 10%
    - **C)** About 0.1%
    - **D)** 100% (no loss)

    **Answer: C** — 3 dB/km × 10 km = 30 dB of total loss, and 10^(−30/10) = 10⁻³ = 0.1% of the input power remains.


## Viva-Voce Questions

1. Why must the core refractive index always exceed the cladding index for a fiber to guide light at all?
2. Explain the trade-off between a large Numerical Aperture (easy light-launching) and modal dispersion in a real multimode fiber.
3. Why is fiber attenuation conventionally expressed in decibels per kilometre rather than as a simple fraction lost per kilometre?
4. From the formula P_out = P_in·10^(−αL/10), derive the fiber length at which exactly half the input power remains, in terms of α.
5. Give one practical reason why single-mode fibers (very small core, small NA) are preferred over multimode fibers for very long-distance telecommunications links.
6. How would you expect the attenuation coefficient α to depend on the wavelength of light used, physically?
