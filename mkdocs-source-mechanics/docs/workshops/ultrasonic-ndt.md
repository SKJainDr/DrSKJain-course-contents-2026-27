# Workshop 2: 🔍 Ultrasonic Non-Destructive Testing — Flaw Detection

!!! info "Industrial & Applied Mechanics Workshop 2 of 6"
    Ultrasonic Non-Destructive Testing — Flaw Detection


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-wsNDT){target=_blank}**

## Workshop Brief

Use pulse-echo ultrasonic testing to locate and size a hidden internal defect (a void or crack) inside a 60 mm thick steel test block, without cutting it open. Correctly identify the defect's depth and estimate its size from the echo timing and amplitude.

**Specifications:** Target block thickness 60 mm · Material: mild steel · Defect depth unknown (to be found) · Detection tolerance ± 1 mm

## Process Theory

Ultrasonic non-destructive testing (NDT) sends a short pulse of high-frequency sound into a solid material from a probe on its surface and listens for echoes: some sound reflects back from the far (back) wall of the component, and — crucially — any internal defect (crack, void, inclusion) with a different acoustic impedance from the surrounding material reflects part of the pulse back early, before the back-wall echo arrives.

Because the speed of sound in a given material is essentially constant and well known, the time delay between sending the pulse and receiving a defect echo directly gives the defect's depth below the surface: depth = (velocity × time)/2, the factor of 2 accounting for the round trip. The amplitude and duration of the defect echo, compared to a calibrated reference reflector, gives a rough estimate of the defect's size.

Correctly interpreting the echo trace requires distinguishing genuine defect echoes from probe ring-down noise near the surface, and from the expected back-wall echo — a real inspector cross-checks by scanning the probe laterally to see the defect echo move and change amplitude in a way consistent with a localized reflector, rather than accepting a single trace at face value.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="82.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="147.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Ultrasonic</text>
<text x="147.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Probe</text>
<rect x="295.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="360.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Test Block with</text>
<text x="360.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Defect</text>
<rect x="507.5" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="572.5" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Pulse-Echo</text>
<text x="572.5" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Display</text>
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
| Probe frequency | 1 – 10 | MHz |
| Pulse repetition rate | 100 – 2000 | Hz |
| Gain (amplification) | 0 – 60 | dB |


## Procedure

1. Start with the default probe frequency and gain and observe the echo trace and the simulator's preliminary depth estimate.
2. Vary the gain alone and note how the defect echo and background noise both change in visibility.
3. Vary the probe frequency alone and note the trade-off between resolution (higher frequency, better resolution) and penetration/noise (lower frequency, more penetration but coarser resolution).
4. Identify the combination of frequency and gain that gives the clearest, most reliable defect echo, and read off the certified depth estimate.
5. Record the final certified defect depth and confirm it is within the ±1 mm detection tolerance.

## Observation Table

*Table: Effect of probe frequency and gain on defect-detection accuracy*

| Trial | Frequency (MHz) | Gain (dB) | Reported defect depth (mm) | Detection confidence (%) | Verdict |
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

Plot **Detection confidence (%)** (y-axis) against **Gain (dB)** (x-axis).

Expected trend: a peak at an intermediate gain — too little gain misses the echo, too much gain saturates the trace with noise.

<div class="graph-box">📈 Graph paper / plot area &mdash; attach printed or digital graph here</div>

## Calculation

1. Tabulate detection confidence against each swept parameter and identify the optimum region for each.
2. State the final probe settings and the certified defect depth.

## Result

*Table: Certified flaw-detection result*

| Frequency (MHz) | Gain (dB) | Final depth reported (mm) | Within tolerance? (Y/N) |
|---|---|---|---|
| 1 | | | |


## Precautions

- Use a couplant (gel) between the probe and the test surface in a real inspection — an air gap reflects almost all the sound and prevents any signal from entering the material.
- Cross-check any suspected defect echo by scanning the probe laterally; a genuine localized defect's echo should move and change amplitude consistently, unlike random noise.
