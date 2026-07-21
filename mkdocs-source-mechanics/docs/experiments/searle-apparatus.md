# 7. Searle's Apparatus — Young's Modulus by Direct Elongation

!!! abstract "Module"
    Elasticity of Solids &middot; Module 2


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-searle){target=_blank}**

## Aim

To determine the Young's modulus of the material of a wire by directly measuring its elongation under a known tensile load, using Searle's apparatus.

## Theoretical Background

Searle's apparatus consists of two identical, long wires of the same material hung side by side from the same rigid support, each carrying a frame at its lower end. One wire (the 'reference' wire) carries a fixed, steady load throughout, keeping it taut; the other (the 'experimental' wire) additionally carries a hanger onto which further known weights are added.

A sensitive spirit-level, pivoted between the two frames with a micrometer screw at one end, detects the tiny relative extension of the experimental wire compared to the reference wire — any elongation tilts the level, which is restored to horizontal by turning the micrometer screw, whose reading then directly gives the elongation. Using a second, unstretched reference wire hung in parallel automatically cancels out any common effects such as temperature-induced expansion or slow sagging of the support, which would otherwise be indistinguishable from the elongation being measured.

Because the extension of a wire under simple tension is directly proportional to the applied load, and inversely proportional to its cross-sectional area, this experiment gives Young's modulus in perhaps its most direct textbook form — literally 'stress divided by strain' — with stress = Mg/(πr²) and strain = extension/original length.

This differential, two-wire design is the same basic principle used in far more sensitive strain-gauge and interferometric elongation measurements in materials-testing laboratories today.

## Governing Formulas

**Extension under load Mg:**

$$
l_{\text{ext}} = \dfrac{M g L}{\pi r^{2} Y}
$$

**Young's modulus:**

$$
Y = \dfrac{M g L}{\pi r^{2}\, l_{\text{ext}}}
$$

where $L$ is the original (unstretched) length of the experimental wire and $r$ its radius.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="105.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Rigid Support</text>
<rect x="210.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="275.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Reference Wire</text>
<text x="275.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">+ Frame</text>
<rect x="380.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="445.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Experimental</text>
<text x="445.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Wire + Load</text>
<rect x="550.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="615.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Spirit Level &</text>
<text x="615.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Micrometer</text>
<line x1="170.0" y1="100.0" x2="202.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="202.0,94.0 212.0,100.0 202.0,106.0" fill="#C97A27"/>
<line x1="340.0" y1="100.0" x2="372.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="372.0,94.0 382.0,100.0 372.0,106.0" fill="#C97A27"/>
<line x1="510.0" y1="100.0" x2="542.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="542.0,94.0 552.0,100.0 542.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled apparatus layout &mdash; original schematic prepared for this guide (not a photograph). Two identical wires of the same material hung side by side from a rigid support, each ending in a frame; a spirit level pivoted between the frames with a micrometer screw detects the relative extension of the loaded (experimental) wire against the steadily-loaded reference wire.</div>
</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Load added | M | 200 – 2000 | g |
| Original wire length | L | 100 – 300 | cm |
| Wire radius | r | 0.20 – 0.60 | mm |


**Readouts:**

| Quantity | Symbol | Unit |
|---|---|---|
| Elongation | l_ext | mm |

## Procedure

1. Launch the Searle's Apparatus panel; set the wire length L and radius r to their default values.
2. Add load M in equal steps and record the elongation shown on the readout (the micrometer reading needed to restore the spirit level to horizontal) at each step.
3. Plot the elongation against the load M; verify it is a straight line through the origin.
4. Unload in the same steps and verify the readings retrace the same line (no permanent set), confirming the wire remained within its elastic limit.
5. Calculate Young's modulus from the slope of the elongation vs load graph, using the known L and r.

## Observation Table

*Table: Elongation of the experimental wire with increasing load*

| S. No. | Load M (g) | Micrometer reading — loading (mm) | Micrometer reading — unloading (mm) | Mean elongation (mm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |


## Graph

Plot **Elongation** (y-axis) against **Load, M** (x-axis).

Expected trend: a straight line through the origin (l_ext ∝ M).

*Elongation vs M, expected to be a straight line through the origin; slope = gL/(πr²Y)*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Elongation vs Load</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif">Load, M (g)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#114A2C" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Elongation (mm)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. Compute the slope of the elongation vs M graph: slope = gL/(πr²Y).
2. Rearrange to find Y = gL/(πr² × slope), using the known L and r.
3. Check that the loading and unloading data agree within experimental scatter — divergence indicates the elastic limit was exceeded.

## Result

*Table: Young's modulus of the wire material*

| L (cm) | r (mm) | Slope (mm/g) | Y (dyne/cm²) |
|---|---|---|---|
| 1 | | | |


## Maximum Permissible Error

The wire radius r, measured with a screw gauge, enters squared and is typically sub-millimetre — its fractional error usually dominates the overall uncertainty in Y.

<div class="error-calc" data-exp="searle-apparatus"></div>

## Precautions

- Remove any kinks in the wire beforehand and apply an initial small load to both wires to keep them taut and straight before starting readings.
- Always turn the micrometer screw in the same direction when approaching the level (horizontal) position, to avoid backlash error.
- Load and unload gradually and note both sets of readings, checking for any permanent set that would indicate the elastic limit was exceeded.

## Self-Check Quiz

??? question "1. The purpose of the second (reference) wire in Searle's apparatus is to:"
    - **A)** Provide a backup in case the experimental wire breaks
    - **B)** Cancel out common effects such as temperature expansion and support sag that would otherwise be mistaken for elongation
    - **C)** Double the measured extension
    - **D)** Reduce the total load

    **Answer: B** — Because both wires hang from the same support and experience the same temperature and any support movement identically, only the differential extension — the true elastic elongation — is registered by the spirit level.


??? question "2. Doubling the wire radius r (all else fixed) changes the elongation for the same load by a factor of:"
    - **A)** 2
    - **B)** 1/2
    - **C)** 4
    - **D)** 1/4

    **Answer: D** — Elongation ∝ 1/r², so doubling r reduces the elongation to 1/4 of its original value.


??? question "3. Backlash error in the micrometer screw is minimised by:"
    - **A)** Turning the screw rapidly
    - **B)** Always approaching the final (level) reading from the same rotational direction
    - **C)** Using a thicker wire
    - **D)** Ignoring the screw reading entirely

    **Answer: B** — Backlash (small mechanical play) in a screw thread causes a different effective zero depending on the direction of the last turn — always finishing in the same direction removes this systematic error.



## Viva-Voce Questions

1. Why does Searle's apparatus use two wires rather than one, and what specific systematic errors does this design eliminate?
2. Derive the relation between stress, strain and Young's modulus, and identify each in this specific experiment.
3. Why is it important to remove kinks and apply an initial small load before beginning the actual measurement?
4. What is backlash error in a micrometer screw, and how is it avoided in this experiment?
5. How would you verify, purely from your own data, that the wire remained within its elastic limit throughout?
6. Why is the wire radius, rather than its length, usually the dominant source of error in the final result for Y?
