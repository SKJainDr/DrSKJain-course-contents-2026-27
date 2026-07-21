# 16. Laser Doppler Vibrometry

!!! abstract "Module"
    Practical Applications

!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-vibrometry){target=_blank}**

## Aim

To study how the Doppler shift imposed on a laser beam reflected from a vibrating surface encodes the surface's instantaneous velocity, and to see why this makes possible a completely non-contact vibration sensor.

## Theoretical Background

When a laser beam reflects from a surface that is moving toward or away from the source, the reflected light is Doppler-shifted in frequency by an amount proportional to the surface's velocity component along the beam direction. For a surface vibrating sinusoidally, this shift is not constant but itself oscillates in time, tracking the surface's instantaneous velocity rather than its displacement.

A **Laser Doppler Vibrometer (LDV)** exploits this by splitting a laser beam into a reference arm and a measurement arm that reflects off the vibrating target; recombining (heterodyning) the two beams at a photodetector produces a beat signal whose instantaneous frequency is the Doppler shift itself. Demodulating that beat signal recovers the target's velocity waveform in real time, without the sensor ever touching the surface.

Because it measures velocity rather than displacement directly, an LDV is intrinsically well-suited to studying fast, delicate, or hard-to-reach vibrating structures — turbine blades, aircraft skin panels, MEMS resonators, loudspeaker diaphragms, or the soundboards of musical instruments — anywhere a contact accelerometer's own mass and stiffness would perturb the very vibration being measured, or where the surface is simply inaccessible.

## Governing Formulas

**Doppler shift for a beam reflecting from a surface moving with velocity v, at angle of incidence θ:**

$$
f_D = \dfrac{2v\cos\theta}{\lambda}
$$

**For a surface vibrating as $x(t) = A\sin(\omega t)$, the instantaneous velocity and its peak value:**

$$
v(t) = A\omega\cos(\omega t), \qquad v_{max} = A\omega
$$

**Hence the peak Doppler shift:**

$$
f_{D,max} = \dfrac{2v_{max}\cos\theta}{\lambda} = \dfrac{2A\omega\cos\theta}{\lambda}
$$

where A is the vibration amplitude, ω = 2πf the angular frequency of vibration, λ the laser wavelength, and θ the angle of incidence of the probe beam.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#a8452f" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">He-Ne Laser</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Source</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#a8452f" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Vibrating Test</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Surface</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#2ec4c6" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Photodetector /</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Demodulator</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#a8452f" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#a8452f"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#2ec4c6" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#2ec4c6"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). A stabilized laser is reflected off a vibrating surface; heterodyning the Doppler-shifted return beam against a reference recovers the surface's velocity as a beat frequency.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Vibration frequency | f | 10 – 500 | Hz |
| Vibration amplitude | A | 1 – 50 | µm |
| Angle of incidence | θ | 0 – 30 | ° |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Peak surface velocity | v_max | mm/s |
| Peak Doppler shift | f_D,max | kHz |
| Instantaneous Doppler shift | f_D(t) | kHz |

## Procedure

1. Launch the Laser Doppler Vibrometry panel; set the angle of incidence θ to a fixed small value.
2. Vary the vibration frequency f, holding the amplitude A fixed, and record the resulting peak Doppler shift f_D,max.
3. Repeat for at least five different frequencies, tabulating f_D,max each time.
4. Repeat the whole sweep at a second, different fixed amplitude A, and compare the two sets of readings.
5. Plot f_D,max against f for each amplitude and verify the predicted straight-line (proportional) relationship.

## Observation Table

*Table: Variation of peak Doppler shift with vibration frequency, at fixed amplitude and angle of incidence*

| S. No. | A (µm) | θ (°) | f (Hz) | v_max = Aω (mm/s) | f_D,max (kHz) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |


## Graph

Plot **Peak Doppler shift, f_D,max** (y-axis) against **Vibration frequency, f** (x-axis).

Expected trend: a straight line through the origin, since f_D,max = (4πA cosθ/λ)·f is directly proportional to f at fixed amplitude.

*f_D,max vs f, at two different fixed amplitudes for comparison*

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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Vibration frequency, f (Hz)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Peak Doppler shift, f&#8320;,max (kHz)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each trial, compute the peak surface velocity v_max = Aω = A(2πf).
2. Compute the peak Doppler shift f_D,max = 2v_max cosθ/λ and compare it with the simulator's readout.
3. From the slope of your f_D,max vs f graph, verify that it equals 4πA cosθ/λ for the amplitude used.

## Result

*Table: Doppler-vibrometry behaviour of the simulated vibrating surface*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

v_max = Aω = A(2πf) is a simple product of the vibration amplitude and (angular) frequency, so their fractional errors simply add.

<div class="error-calc" data-exp="laser-doppler-vibrometry"></div>

## Precautions

- Keep the angle of incidence θ small and well-characterized, since the measured Doppler shift always scales with cosθ, not the true surface-normal velocity.
- Ensure the reference and measurement beams are recombined coherently (heterodyne detection) so that the beat frequency, not just intensity, carries the velocity information.
- Isolate the setup from stray environmental vibration (footsteps, HVAC, benchtop resonances), which would otherwise be indistinguishable from the target's own vibration.

## Self-Check Quiz

??? question "1. A laser Doppler vibrometer directly measures which quantity of the target surface?"
    - **A)** Displacement
    - **B)** Velocity
    - **C)** Acceleration
    - **D)** Temperature

    **Answer: B** — The Doppler shift is proportional to the instantaneous velocity of the surface along the beam direction, not its displacement.


??? question "2. If the vibration frequency f is doubled while the amplitude A is halved, the peak Doppler shift f_D,max:"
    - **A)** Doubles
    - **B)** Halves
    - **C)** Stays the same
    - **D)** Quadruples

    **Answer: C** — f_D,max ∝ Aω ∝ Af, so doubling f while halving A leaves the product unchanged.


??? question "3. Why is a non-contact vibration sensor like an LDV preferred over a contact accelerometer for measuring a lightweight MEMS resonator?"
    - **A)** LDVs are always cheaper
    - **B)** A contact sensor's own mass and stiffness would load and change the very vibration being measured
    - **C)** Contact sensors cannot measure any vibration at all
    - **D)** LDVs work only on metals

    **Answer: B** — For very light or delicate structures, even a small accelerometer's added mass can significantly perturb the resonance being studied; a laser beam adds essentially zero mass or stiffness.


## Viva-Voce Questions

1. Why does the Doppler shift depend on cosθ rather than simply on the surface's speed?
2. Explain why heterodyne (beat-frequency) detection, rather than simply measuring reflected intensity, is necessary to recover the Doppler shift.
3. How would the measured signal change if the surface vibrated with two superposed frequencies instead of one pure tone?
4. Why is velocity, rather than displacement, the more natural quantity for this technique to measure directly?
5. Give one practical application where a contact sensor would be unsuitable but an LDV would work well, and explain why.
6. What would happen to the recovered signal if the target surface were optically rough versus mirror-smooth?
