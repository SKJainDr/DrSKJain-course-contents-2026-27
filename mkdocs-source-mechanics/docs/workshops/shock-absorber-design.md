# Workshop 6: 🚗 Automotive Shock-Absorber Damping Design

!!! info "Industrial & Applied Mechanics Workshop 6 of 6"
    Automotive Shock-Absorber Damping Design


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-mechanics-matter-lab.html#panel-wsShockAbsorber){target=_blank}**

## Workshop Brief

Tune the damping coefficient of a vehicle's shock absorber (damper) for a given suspension spring and sprung mass, to achieve a good compromise between ride comfort (soft, well-damped response to bumps) and road holding (tyre contact force staying well-controlled over rough roads), certifying the design against both criteria.

**Specifications:** Sprung mass (per corner) 400 kg · Suspension spring stiffness: given · Target damping ratio range: 0.2 – 0.4

## Process Theory

A vehicle's suspension at each wheel behaves, to a good first approximation, as a single mass-spring-damper system: the sprung mass (the portion of the vehicle's weight supported by that wheel) sits on a spring (the suspension spring) and a damper (the shock absorber) that both connect it to the wheel, which in turn follows the road surface profile as the vehicle moves. This system's damping ratio ζ — the same fundamental parameter that appears in the damped-oscillation and forced-resonance experiments — largely determines how the vehicle responds to bumps and how well the tyre maintains its grip on the road.

Too little damping (a low ζ) leaves the suspension lightly damped: after hitting a bump, the vehicle body bounces for several cycles before settling, and the tyre's contact force with the road fluctuates significantly, momentarily reducing grip during hard braking or cornering exactly when it matters most. Too much damping (a high ζ), conversely, makes the suspension stiff and jarring — bumps are transmitted almost directly into the vehicle body with little of the softening that a well-tuned damper provides, giving a harsh ride, even though the tyre's contact force stays comparatively steady.

Production passenger-vehicle suspensions are typically tuned to a damping ratio in the range of about 0.2 to 0.4, deliberately underdamped, striking the balance between comfort and control that is why 'shock absorber' is something of a misnomer — the spring, not the damper, actually absorbs the shock energy; the damper's real job is to dissipate that energy at a controlled rate so the suspension does not simply keep bouncing.

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-photo">
<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
<rect x="0" y="0" width="720" height="220" fill="#FBF7EE" rx="10"/>
<rect x="40.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="105.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Sprung Mass</text>
<rect x="210.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="275.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Suspension</text>
<text x="275.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Spring</text>
<rect x="380.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="445.0" y="100.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Shock Absorber</text>
<rect x="550.0" y="65.0" width="130" height="70" rx="10" fill="#EFE3C8" stroke="#1F6E43" stroke-width="2.2"/>
<text x="615.0" y="91.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Wheel / Road</text>
<text x="615.0" y="109.0" text-anchor="middle" font-size="13.5" font-weight="600" fill="#14251C" font-family="Inter,Helvetica,sans-serif">Input</text>
<line x1="170.0" y1="100.0" x2="202.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="202.0,94.0 212.0,100.0 202.0,106.0" fill="#C97A27"/>
<line x1="340.0" y1="100.0" x2="372.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="372.0,94.0 382.0,100.0 372.0,106.0" fill="#C97A27"/>
<line x1="510.0" y1="100.0" x2="542.0" y2="100.0" stroke="#C97A27" stroke-width="2.5"/>
<polygon points="542.0,94.0 552.0,100.0 542.0,106.0" fill="#C97A27"/>
</svg>
<div class="cap">Labelled process layout &mdash; original schematic prepared for this guide (not a photograph).</div>
</div>
</div>

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Damping coefficient c | 500 – 6000 | N·s/m |
| Spring stiffness k | 15000 – 40000 | N/m |
| Sprung mass | 300 – 550 | kg |


## Procedure

1. Start with the default damping coefficient and note the damping ratio ζ, the bump-response overshoot, and the tyre contact-force variation shown by the simulator.
2. Vary the damping coefficient c alone (holding k and mass fixed) and record ζ, overshoot, and contact-force variation at each setting.
3. Identify the range of c that keeps ζ within the target 0.2–0.4 band.
4. Within that range, note the trade-off between ride comfort (overshoot) and road holding (contact-force variation) as c is varied.
5. Select and record the final certified damping coefficient that best balances both criteria within the target ζ range.

## Observation Table

*Table: Effect of damping coefficient on ride comfort and road holding*

| Trial | Damping c (N·s/m) | Damping ratio ζ | Bump overshoot (%) | Contact-force variation (%) | Verdict |
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

Plot **Damping ratio, &zeta;** (y-axis) against **Damping coefficient, c (N&middot;s/m)** (x-axis).

Expected trend: an increasing, roughly linear trend, since ζ = c / (2√(km)).

<div class="graph-box">📈 Graph paper / plot area &mdash; attach printed or digital graph here</div>

## Calculation

1. Tabulate ζ, overshoot and contact-force variation against the swept damping coefficient.
2. State the final damping coefficient selected and confirm it falls within the target damping-ratio band.

## Result

*Table: Certified suspension damping design*

| Damping c (N·s/m) | Damping ratio ζ | Bump overshoot (%) | Contact-force variation (%) | Certified? (Y/N) |
|---|---|---|---|---|
| 1 | | | | |


## Precautions

- Change the damping coefficient in moderate steps rather than extremes, to clearly observe the comfort/road-holding trade-off across the usable range.
- Remember that the target damping-ratio band (0.2–0.4) is itself a design compromise — note in your report which end of the band you favoured and why.
