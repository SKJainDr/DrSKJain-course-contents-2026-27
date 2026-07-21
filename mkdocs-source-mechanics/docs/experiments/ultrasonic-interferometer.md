# 15. Ultrasonic Interferometer — Velocity of Sound and Elastic Constants of a Liquid (PG)

!!! abstract "Module"
    Oscillations, Damping & Acoustic Methods (PG) &middot; Module 4


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-ultrasonic){target=_blank}**

## Aim

To determine the velocity of ultrasonic waves in a liquid using an ultrasonic interferometer, and hence to calculate the liquid's adiabatic compressibility and bulk modulus.

## Theoretical Background

An ultrasonic interferometer generates high-frequency (megahertz-range) longitudinal sound waves in a liquid using a piezoelectric quartz crystal fixed at the base of a small measuring cell, driven by a radio-frequency oscillator. A movable, reflecting plate at the top of the liquid column can be raised or lowered very precisely using a micrometer screw, allowing the length of the liquid column between the crystal and the reflector to be adjusted continuously.

When the reflector is at a distance from the crystal equal to a whole number of half-wavelengths, the wave reflected back from it arrives in phase with the newly generated wave, setting up a stationary (standing) wave pattern in the liquid column; this resonance condition loads the crystal's electrical circuit in a way that produces a sharp, repeatable maximum in the anode (or drive) current of the oscillator, easily read off a built-in meter.

As the micrometer is turned steadily in one direction, successive current maxima occur every time the reflector moves through exactly half a wavelength, so the distance between consecutive maxima directly gives λ/2; averaging this spacing over many maxima (rather than trusting a single interval) gives a precise wavelength, and hence, since the driving frequency f is fixed and known, the velocity of sound v = fλ in the liquid.

Once v is known, and given the liquid's density ρ (measured separately, e.g. by a pyknometer), the liquid's adiabatic compressibility β = 1/(ρv²) and adiabatic bulk modulus K = ρv² follow immediately — these fundamental elastic constants, difficult to access by any purely mechanical (static) method for a liquid, are exactly what make the ultrasonic interferometer an important and widely used PG-level instrument in acoustics, chemical physics, and materials characterisation of liquids and solutions.

## Governing Formulas

**Wavelength from the spacing of successive current maxima:**

$$
\lambda = 2\,\overline{\Delta d}
$$

**Velocity of ultrasonic waves in the liquid:**

$$
v = f\lambda
$$

**Adiabatic compressibility and bulk modulus:**

$$
\beta = \dfrac{1}{\rho v^{2}}, \qquad K = \rho v^{2}
$$

where $f$ is the fixed crystal-driving frequency, $\overline{\Delta d}$ the mean spacing between successive current maxima, and $\rho$ the liquid's density.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="11.7" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="76.7" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">RF Oscillator</text>
<rect x="153.3" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="218.3" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Piezoelectric</text>
<text x="218.3" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Crystal</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Liquid Column</text>
<rect x="436.7" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="501.7" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Micrometer</text>
<text x="501.7" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Reflector</text>
<rect x="578.3" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="643.3" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Current Meter</text>
<line x1="141.7" y1="100.0" x2="145.3" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="145.3,94.0 155.3,100.0 145.3,106.0" fill="#C97A27"/>
<line x1="283.3" y1="100.0" x2="287.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="287.0,94.0 297.0,100.0 287.0,106.0" fill="#C97A27"/>
<line x1="425.0" y1="100.0" x2="428.7" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="428.7,94.0 438.7,100.0 428.7,106.0" fill="#C97A27"/>
<line x1="566.7" y1="100.0" x2="570.3" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="570.3,94.0 580.3,100.0 570.3,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A small liquid-filled measuring cell with a piezoelectric quartz crystal fixed at its base (driven by a radio-frequency oscillator) and a movable, micrometer-controlled reflector plate at the top, with a current meter reading the oscillator's anode current.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Driving frequency | f | 1.0 – 4.0 | MHz |
| Liquid selection (density) | ρ | 780 – 1300 | kg/m³ |
| Number of maxima to average over | N | 5 – 30 | — |


**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Mean spacing between successive maxima | Δd | mm |

## Procedure

1. Launch the Ultrasonic Interferometer panel; select a liquid and set the driving frequency f.
2. Turn the (virtual) micrometer steadily and note the reflector positions at which the current readout passes through successive maxima.
3. Record the total distance moved over N consecutive maxima (choosing N as large as practical) and divide by N to get the mean spacing Δd, as shown on the readout.
4. Repeat for a different driving frequency f and, separately, for a different liquid; tabulate Δd, λ = 2Δd, and v = fλ for each case.
5. Using the known liquid density ρ, calculate the adiabatic compressibility β and bulk modulus K for each liquid studied.

## Observation Table

*Table: Wavelength and velocity of ultrasonic waves for different liquids/frequencies*

| S. No. | Liquid | f (MHz) | N (maxima averaged) | Δd (mm) | λ = 2Δd (mm) | v = fλ (m/s) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |


## Graph

Plot **Total distance moved, D** (y-axis) against **Number of maxima counted, N** (x-axis).

Expected trend: a straight line through the origin, of slope Δd = λ/2, confirming a constant spacing between successive maxima.

*Total distance D vs N, expected to be a straight line through the origin; slope = Δd*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Total Distance vs Number of Maxima</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Number of maxima counted, N</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Total distance moved, D (mm)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. From the slope of the D vs N graph, obtain the mean maxima spacing Δd = λ/2, hence λ = 2Δd.
2. Compute v = fλ for each liquid/frequency combination studied.
3. Using the known density ρ of each liquid, compute the adiabatic compressibility β = 1/(ρv²) and bulk modulus K = ρv².

## Result

*Table: Velocity of sound and elastic constants of the liquid(s) studied*

| Liquid | ρ (kg/m³) | v (m/s) | β (m²/N) | K (N/m²) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |


## Maximum Permissible Error

Averaging the maxima spacing over as many resonances as practical (large N) directly reduces the fractional error in Δd, and hence in v, β and K, since micrometer positioning error is essentially fixed per reading but is divided by N when averaged this way.

<div class="error-calc" data-exp="ultrasonic-interferometer"></div>

## Precautions

- Turn the micrometer slowly and always in the same direction while approaching and passing through a current maximum, to avoid backlash error in the screw.
- Average the maxima spacing over as many resonances as conveniently possible rather than relying on just two consecutive ones, to reduce the fractional error.
- Keep the liquid free of air bubbles and at a steady temperature, since both dissolved gas and temperature noticeably affect the velocity of sound in a liquid.

## Self-Check Quiz

??? question "1. The distance between two successive current maxima in an ultrasonic interferometer corresponds to a reflector movement of:"
    - **A)** One full wavelength, λ
    - **B)** Half a wavelength, λ/2
    - **C)** A quarter wavelength, λ/4
    - **D)** Twice the wavelength, 2λ

    **Answer: B** — Consecutive resonance (standing-wave) conditions occur each time the reflector moves through λ/2, since this brings the reflected wave back into phase with the source wave once more.


??? question "2. If the driving frequency f is doubled (all else fixed), the measured wavelength λ in the same liquid:"
    - **A)** Doubles
    - **B)** Halves
    - **C)** Stays the same, since v is a material property of the liquid
    - **D)** Quadruples

    **Answer: B** — Since v = fλ and v is fixed by the liquid (at a given temperature), doubling f must halve λ to keep the product v = fλ unchanged.


??? question "3. The adiabatic bulk modulus K of the liquid is calculated from the measured velocity v and density ρ as:"
    - **A)** K = v/ρ
    - **B)** K = ρv
    - **C)** K = ρv²
    - **D)** K = v²/ρ

    **Answer: C** — K = ρv² directly, following from the general relation between the speed of a longitudinal wave in a medium and its elastic modulus and density.



## Viva-Voce Questions

1. Explain how a standing wave in the liquid column produces a sharp maximum in the crystal's drive current.
2. Why is it better to measure the total distance over many maxima (large N) and divide, rather than reading a single λ/2 spacing?
3. Derive the relations for adiabatic compressibility and bulk modulus from the measured velocity and known density.
4. Why does dissolved air or a temperature change affect the measured velocity of sound in a liquid?
5. What advantage does the ultrasonic interferometer have over other methods for finding the elastic constants of a liquid?
6. How would the observed velocity differ between a liquid and, say, air, and what does this reveal about the relative compressibility of liquids versus gases?
