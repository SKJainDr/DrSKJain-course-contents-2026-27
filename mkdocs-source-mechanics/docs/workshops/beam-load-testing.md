# Workshop 3: 🏗️ Structural Beam Load Testing & Strain Certification

!!! info "Industrial & Applied Mechanics Workshop 3 of 6"
    Structural Beam Load Testing & Strain Certification


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-wsBeamLoad){target=_blank}**

## Workshop Brief

Load-test a candidate steel I-beam intended for a small pedestrian footbridge, confirming that under its full rated design load it stays safely within its elastic limit with an adequate factor of safety, and does not deflect more than the serviceability limit.

**Specifications:** Design load 12 kN · Span 4 m · Serviceability deflection limit: span/300 · Target factor of safety ≥ 2.5

## Process Theory

Before any structural beam is put into service, its behaviour under load must be verified against two separate criteria: a strength criterion (the maximum stress induced anywhere in the beam must stay safely below the material's yield stress, with a comfortable factor of safety in hand for unforeseen overloads or material variability) and a serviceability criterion (the beam's deflection under normal working load must not be so large that the structure feels unsafe or unusable, even though it may still be far from actual structural failure).

For a simply-supported beam under a central point load, both the maximum bending stress and the maximum deflection can be calculated directly from beam theory once the beam's cross-sectional properties (second moment of area, section modulus) and material properties (Young's modulus, yield stress) are known — but a physical load test, instrumented with strain gauges and a deflection dial gauge, is still standard practice to confirm that the as-built beam actually behaves as the calculation predicts, catching any manufacturing defect, unexpected material property, or support condition not captured by the idealized calculation.

The workshop task is to apply the rated design load incrementally, recording strain and deflection at each step, verifying that both stay proportional to load throughout (confirming genuinely elastic behaviour with no incipient yielding), and confirming the two numerical criteria — factor of safety and deflection limit — are both comfortably satisfied before certifying the beam fit for service.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="82.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="147.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Test Beam on</text>
<text x="147.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Supports</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Applied Load</text>
<rect x="507.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="572.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Strain Gauge &</text>
<text x="572.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Dial Gauge</text>
<line x1="212.5" y1="100.0" x2="287.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="287.0,94.0 297.0,100.0 287.0,106.0" fill="#C97A27"/>
<line x1="425.0" y1="100.0" x2="499.5" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="499.5,94.0 509.5,100.0 499.5,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled process layout &mdash; original schematic prepared for this guide (not a photograph).</div>
</div>
</div>

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Applied load | 0 – 15 | kN |
| Beam section modulus | 40 – 120 | cm³ |
| Beam second moment of area | 800 – 4000 | cm⁴ |


## Procedure

1. Apply the load in increments from zero up to the full 12 kN design load, recording the strain-gauge reading and the mid-span deflection at each step.
2. Plot strain against load and confirm a straight line through the origin (elastic behaviour, no yielding).
3. Compute the maximum bending stress at the design load from the strain reading (stress = strain × Young's modulus) and compare it with the material's yield stress to obtain the factor of safety.
4. Compute the mid-span deflection at the design load and compare with the serviceability limit (span/300).
5. Certify the beam only if both the factor of safety (≥ 2.5) and the deflection limit are satisfied simultaneously.

## Observation Table

*Table: Strain and deflection with increasing applied load*

| Trial | Load (kN) | Strain (microstrain) | Stress (MPa) | Deflection (mm) | Verdict |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |


## Graph

Plot **Strain (microstrain)** (y-axis) against **Applied load (kN)** (x-axis).

Expected trend: a straight line through the origin, confirming elastic behaviour up to the design load.

<div class="graph-box">📈 Graph paper / plot area &mdash; attach printed or digital graph here</div>

## Calculation

1. Compute the factor of safety = yield stress / maximum stress at the design load.
2. Compute the deflection ratio = span / mid-span deflection at the design load and compare with the required 300.

## Result

*Table: Certification summary for the candidate beam*

| Design load (kN) | Max. stress (MPa) | Factor of safety | Deflection (mm) | Certified? (Y/N) |
|---|---|---|---|---|
| 1 | | | | |


## Precautions

- Apply and remove the load in the same increments and confirm the strain returns to zero on full unloading, verifying no permanent (plastic) deformation occurred.
- Never load a real test beam beyond a small margin past its rated design load without an engineer's explicit authorization and appropriate safety barriers.
