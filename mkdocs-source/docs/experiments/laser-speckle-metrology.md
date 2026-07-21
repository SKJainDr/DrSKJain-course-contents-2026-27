# 18. Laser Speckle Metrology — Non-Contact Surface Roughness

!!! abstract "Module"
    Practical Applications

!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-speckle){target=_blank}**

## Aim

To study how the grain size and contrast of a laser speckle pattern depend on the illumination geometry and on the roughness of the scattering surface, and to see how this forms the basis of a non-contact surface-finish inspection technique.

## Theoretical Background

When coherent laser light illuminates an optically rough surface — one whose height variations are comparable to or larger than the wavelength of light — each illuminated point scatters light with a random phase determined by its exact height. Downstream, these many randomly-phased spherical wavelets interfere with one another, producing a grainy, random intensity pattern known as **laser speckle**, rather than a smooth, uniform reflection.

Two statistical properties of this speckle pattern are of practical interest. The **grain size** (the characteristic size of the bright/dark blobs) is set purely by the illumination geometry — the beam diameter D and the distance z to the observation screen — independent of the surface roughness itself, following a diffraction-limited relation analogous to the resolution limit of an aperture. The **speckle contrast**, on the other hand, depends strongly on the surface roughness relative to the wavelength: a surface much smoother than the wavelength (σ ≪ λ) reflects almost specularly, producing low-contrast (nearly uniform) speckle, while a surface with roughness comparable to or greater than the wavelength (σ ≳ λ) produces fully-developed, high-contrast speckle.

This roughness-dependence of speckle contrast is exploited directly in industrial **laser speckle profilometers**, which grade the surface finish of machined parts, semiconductor wafers, and rolled sheet metal on a production line by measuring speckle statistics — entirely without touching the part, unlike a stylus profilometer, which must physically drag a fine needle across the surface and risks scratching delicate finishes.

## Governing Formulas

**Objective speckle grain size, for a beam of diameter D observed at distance z:**

$$
s \approx 1.22\dfrac{\lambda z}{D}
$$

**Approximate speckle contrast as a function of RMS surface roughness σ (relative to wavelength λ):**

$$
C \approx 1-\exp\!\left[-\left(\dfrac{2\pi\sigma}{\lambda}\right)^{2}\right]
$$

where λ is the laser wavelength, D the illuminated beam/aperture diameter, z the distance to the observation screen, and σ the RMS height variation of the scattering surface.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#a8452f" stroke-width="2.2"/>
<text x="115.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">He-Ne Laser</text>
<text x="115.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Source</text>
<rect x="240.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#a8452f" stroke-width="2.2"/>
<text x="315.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Test Surface</text>
<text x="315.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">(Roughness σ)</text>
<rect x="440.0" y="65.0" width="150" height="70" rx="10" fill="#F3E7CE" stroke="#2ec4c6" stroke-width="2.2"/>
<text x="515.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Observation</text>
<text x="515.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Screen (dist. z)</text>
<line x1="190.0" y1="100.0" x2="222.0" y2="100.0" stroke="#a8452f" stroke-width="2.5"/>
<polygon points="222.0,94.0 232.0,100.0 222.0,106.0" fill="#a8452f"/>
<line x1="390.0" y1="100.0" x2="422.0" y2="100.0" stroke="#2ec4c6" stroke-width="2.5"/>
<polygon points="422.0,94.0 432.0,100.0 422.0,106.0" fill="#2ec4c6"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). Coherent laser light illuminates the test surface; the scattered speckle pattern is observed on a screen a set distance away.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| RMS surface roughness | σ | 5 – 2000 | nm |
| Illuminated beam diameter | D | 0.5 – 5 | mm |
| Screen distance | z | 10 – 100 | cm |

**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Speckle grain size | s | µm |
| Speckle contrast | C | (0–1) |
| Surface regime | — | (qualitative) |

## Procedure

1. Launch the Laser Speckle Metrology panel; set the beam diameter D and screen distance z to fixed values.
2. Vary the RMS surface roughness σ and record the resulting speckle contrast C at each value.
3. Repeat for at least six different values of σ spanning from well below to well above the laser wavelength (632.8 nm), tabulating C each time.
4. Fix σ, then vary the beam diameter D and record the speckle grain size s at each value, verifying the inverse relationship between s and D.
5. Plot both C vs σ and s vs D as separate graphs.

## Observation Table

*Table: Variation of speckle contrast with surface roughness, at fixed beam diameter and screen distance*

| S. No. | D (mm) | z (cm) | σ (nm) | σ/λ | Contrast, C |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |


## Graph

Plot **Speckle contrast, C** (y-axis) against **Roughness ratio, σ/λ** (x-axis).

Expected trend: a sharply rising curve from near zero (optically smooth, specular) to close to 1 (fully-developed speckle) once σ/λ exceeds roughly 0.1–0.2.

*C vs σ/λ, showing the transition from specular to fully-developed speckle*

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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Roughness ratio, &sigma;/&lambda;</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Speckle contrast, C</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>


## Calculation

1. For each trial, compute the roughness ratio σ/λ using λ = 632.8 nm.
2. Compute the predicted speckle contrast C ≈ 1−exp[−(2πσ/λ)²] and compare it with the simulator's readout.
3. Separately, compute the speckle grain size s = 1.22λz/D for your D-sweep trials and verify the inverse dependence on D.

## Result

*Table: Speckle-pattern behaviour for the simulated rough surface*

| Quantity | Mean value | Unit |
|---|---|---|
| 1 | | |
| 2 | | |


## Maximum Permissible Error

The speckle grain size s = 1.22λz/D is a product/quotient of measured quantities (λ taken as exact for a stabilized laser source), so the fractional errors in the screen distance z and beam diameter D simply add.

<div class="error-calc" data-exp="laser-speckle-metrology"></div>

## Precautions

- Use a genuinely coherent, single-frequency laser source; a source with poor spatial or temporal coherence will wash out the speckle pattern regardless of the surface roughness.
- Keep the beam diameter D and screen distance z fixed while varying only σ (and vice versa), so the two dependences are not confounded in your data.
- Avoid stray ambient light on the observation screen, since it reduces the apparent contrast of the genuine speckle pattern.

## Self-Check Quiz

??? question "1. A surface with RMS roughness much smaller than the laser wavelength (σ ≪ λ) will produce:"
    - **A)** High-contrast, fully-developed speckle
    - **B)** Low-contrast, nearly specular reflection
    - **C)** No reflected light at all
    - **D)** A speckle pattern with zero grain size

    **Answer: B** — When the surface is optically smooth compared to the wavelength, it reflects almost like a mirror, so scattered wavelets stay nearly in phase and produce little of the random interference that characterizes fully-developed speckle.


??? question "2. Doubling the beam diameter D, with the screen distance z fixed, will make the speckle grain size:"
    - **A)** Double
    - **B)** Halve
    - **C)** Stay the same
    - **D)** Quadruple

    **Answer: B** — Since s ≈ 1.22λz/D, s is inversely proportional to D, so doubling D halves the grain size.


??? question "3. Why can a laser speckle instrument grade surface roughness without ever touching the part?"
    - **A)** Because speckle contrast is set by surface roughness relative to the wavelength, and can be measured purely optically
    - **B)** Because lasers physically polish the surface as they scan it
    - **C)** Because speckle patterns only occur on rough surfaces, never on smooth ones
    - **D)** It cannot; a stylus is always still required

    **Answer: A** — The contrast (and other statistics) of the purely optical speckle pattern already encode the σ/λ ratio, so no physical contact with the surface is ever needed.


## Viva-Voce Questions

1. Why does speckle contrast depend on surface roughness while speckle grain size does not?
2. Explain physically why illuminating a rougher surface produces a higher-contrast speckle pattern.
3. How would using a shorter-wavelength laser (e.g., a blue laser instead of a red He-Ne) change the sensitivity of this technique to a given surface's roughness?
4. Why is a genuinely coherent source essential for observing speckle, and what would happen with an ordinary incoherent lamp instead?
5. Give one advantage of a laser-speckle-based surface inspection method over a traditional contact stylus profilometer, beyond simply avoiding scratches.
6. What practical factors (other than roughness) might also affect the measured speckle contrast in a real industrial setting?
