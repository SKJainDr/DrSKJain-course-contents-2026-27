# Workshop 4: ⚙️ Rotor Balancing Workshop

!!! info "Industrial & Applied Mechanics Workshop 4 of 6"
    Rotor Balancing Workshop


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-wsRotorBalance){target=_blank}**

## Workshop Brief

Reduce the residual vibration of an unbalanced rotor (e.g. a fan or pump impeller) spinning at its rated speed, by calculating and adding a trim (correction) mass at the correct radius and angular position, bringing the vibration within the ISO balance-quality tolerance for its machine class.

**Specifications:** Rotor mass 8 kg · Operating speed 3000 rpm · Target: ISO 1940 balance grade G6.3 or better

## Process Theory

A perfectly balanced rotor has its mass distributed so that its centre of mass lies exactly on its rotation axis; any small manufacturing asymmetry, casting inhomogeneity, or accumulated deposit shifts the centre of mass slightly off-axis, creating an effective 'heavy spot' that generates a centrifugal force rotating with the shaft. This rotating force is transmitted into the bearings and supporting structure as a vibration at exactly the rotational speed (once per revolution) — the classic signature that distinguishes unbalance from other vibration causes such as misalignment or bearing wear.

Balancing corrects this by measuring the amplitude and phase of the once-per-revolution vibration (using a vibration sensor and a phase reference such as a once-per-revolution timing mark), from which the magnitude and angular location of the effective unbalance can be calculated. A trim mass is then added (or, equivalently, material removed) at a calculated radius and angular position diametrically related to the unbalance, so as to shift the centre of mass back onto the rotation axis, or at least much closer to it.

International balancing standards such as ISO 1940 define allowable residual unbalance in terms of a balance quality grade (G-number) related to the rotor's operating speed and application — a higher-speed or more critical rotor (such as a turbine) requires a much tighter tolerance (lower G-number) than a low-speed fan.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="82.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="147.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Unbalanced</text>
<text x="147.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Rotor</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Vibration</text>
<text x="360.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Sensor</text>
<rect x="507.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="572.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Trim Mass</text>
<text x="572.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Location</text>
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
| Trim mass added | 0 – 40 | g |
| Trim mass radius | 3 – 15 | cm |
| Trim mass angular position | 0 – 360 | ° |


## Procedure

1. Note the initial (uncorrected) vibration amplitude and phase reading of the rotor at its rated speed.
2. Estimate the trim mass, radius and angular position needed to cancel the unbalance, based on the initial reading.
3. Apply a trial trim mass and observe the change in vibration amplitude and phase — use this trial-and-correction data to refine the estimate (the standard 'single-plane, trial-weight' balancing procedure).
4. Iterate the trim mass magnitude and angular position until the residual vibration amplitude falls within the target ISO balance grade.
5. Record the final certified trim mass, radius and angular position.

## Observation Table

*Table: Residual vibration with successive trim-mass corrections*

| Trial | Trim mass (g) | Radius (cm) | Angular position (°) | Residual vibration (mm/s) | Verdict |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |


## Graph

Plot **Residual vibration (mm/s)** (y-axis) against **Trim mass (g)** (x-axis).

Expected trend: a minimum at the correctly-sized trim mass, rising again if the trim mass overshoots the required correction.

<div class="graph-box">📈 Graph paper / plot area &mdash; attach printed or digital graph here</div>

## Calculation

1. Tabulate residual vibration against trial trim-mass settings and identify the setting giving the minimum residual vibration.
2. State the final certified trim mass, radius and angular position, and the resulting ISO balance grade achieved.

## Result

*Table: Certified rotor balancing result*

| Final trim mass (g) | Radius (cm) | Angular position (°) | Residual vibration (mm/s) | ISO grade achieved | Certified? (Y/N) |
|---|---|---|---|---|---|
| 1 | | | | | |


## Precautions

- Always mark the angular reference position clearly on the rotor before starting, since the trim-mass angular position is meaningless without a fixed zero reference.
- Add trim mass in small increments near the estimated correct value rather than a single large guess, since overshooting requires removing mass again.
