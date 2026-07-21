# Workshop 5: 🧪 Viscometer Calibration & Lubricant Grading

!!! info "Industrial & Applied Mechanics Workshop 5 of 6"
    Viscometer Calibration & Lubricant Grading


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-wsViscometer){target=_blank}**

## Workshop Brief

Calibrate a falling-ball viscometer against a certified reference oil, then use it to grade an unknown industrial lubricant sample into its correct ISO Viscosity Grade (VG) class for quality-control release.

**Specifications:** Reference oil viscosity: certified value provided · Target grading accuracy: correct ISO VG class · Test temperature: 40 °C

## Process Theory

Industrial lubricants are classified by standardized viscosity grades (such as the ISO VG system) because correct viscosity — neither too thin (inadequate load-bearing oil film, risking metal-to-metal contact) nor too thick (excessive churning losses and poor cold-flow) — is essential to a lubricant correctly protecting bearings, gears and other machine elements across their operating temperature range.

A falling-ball (Stokes' law) viscometer provides a simple, robust quality-control method: dropping a calibrated sphere through a sample and timing its fall over a fixed distance gives its terminal velocity, from which the viscosity follows directly via Stokes' law, provided the sphere and fluid densities are known. Because absolute calibration of every geometric and frictional detail of a real instrument is impractical, standard practice is to first calibrate the instrument's effective constant using a certified reference oil of precisely known viscosity, and then apply that same calibration constant to unknown samples measured under identical conditions.

Once the unknown sample's viscosity has been measured this way, it is compared against the boundaries of the ISO VG classes (each class specified by a viscosity range at 40 °C) to determine which grade the batch belongs to — a mis-graded batch released to a customer expecting a different viscosity grade can cause premature equipment wear or failure in service, making this a genuine quality-control gate rather than a purely academic measurement.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="82.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="147.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Falling-Ball</text>
<text x="147.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Tube</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Reference /</text>
<text x="360.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Unknown Sample</text>
<rect x="507.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="572.5" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Timing System</text>
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
| Ball fall time, reference oil | 20 – 200 | s |
| Ball fall time, unknown sample | 20 – 200 | s |
| Test temperature | 20 – 100 | °C |


## Procedure

1. Drop the calibration ball through the certified reference oil and record its fall time over the fixed measuring distance.
2. Using the reference oil's certified viscosity and the measured fall time, calculate the instrument's calibration constant.
3. Drop the same ball through the unknown lubricant sample and record its fall time under identical conditions.
4. Using the calibration constant, calculate the unknown sample's viscosity.
5. Compare the calculated viscosity against the ISO VG class boundaries and assign the sample to its correct grade for quality-control release.

## Observation Table

*Table: Fall times and derived viscosities for reference and unknown samples*

| Sample | Fall time (s) | Certified/derived viscosity (cSt) | ISO VG class | Verdict |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |


## Graph

Plot **Fall time (s)** (y-axis) against **Viscosity (cSt)** (x-axis).

Expected trend: a straight line through the origin, since fall time is directly proportional to viscosity for a fixed ball and geometry.

<div class="graph-box">📈 Graph paper / plot area &mdash; attach printed or digital graph here</div>

## Calculation

1. Compute the calibration constant from the reference oil's certified viscosity and its measured fall time.
2. Apply the calibration constant to the unknown sample's fall time to obtain its viscosity, and identify its ISO VG class.

## Result

*Table: Quality-control grading result for the unknown lubricant*

| Sample | Measured viscosity (cSt) | Assigned ISO VG class | Within class tolerance? (Y/N) |
|---|---|---|---|
| 1 | | | |


## Precautions

- Keep the reference oil and the unknown sample at exactly the same, carefully controlled temperature during their respective measurements, since viscosity is strongly temperature-dependent.
- Use the same ball and the same measuring distance for both the calibration and the unknown-sample measurement, so the instrument constant cancels correctly.
