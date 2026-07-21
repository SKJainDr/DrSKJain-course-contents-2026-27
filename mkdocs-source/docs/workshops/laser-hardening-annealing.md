# Workshop 6: ⚙️ Laser Hardening & Annealing

!!! info "Industrial Workshop 6 of 7"
    Laser Hardening & Annealing


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-wsHardening){target=_blank}**

## Workshop Brief

Harden the surface of a steel gear tooth to a case depth of about 0.8 mm using rapid self-quenching laser heating. Stay above the austenitizing temperature but below the melting point — melting ruins the surface finish, and insufficient heating leaves the case too shallow.

**Specifications:** Target case depth 0.8 mm · No surface melting

## Process Theory

Laser transformation hardening heats a thin surface layer of a steel component above its austenitizing temperature using a defocused, relatively low-power-density laser beam; because the laser only heats a thin surface layer while the cold bulk material remains at ambient temperature, heat is conducted away extremely rapidly the instant the beam moves on — providing a very high self-quench rate without any external quenchant.

This rapid self-quenching transforms the austenitized surface layer into hard martensite, increasing surface hardness and wear resistance, while the untransformed bulk retains its original toughness — an ideal combination for gear teeth and similar wear surfaces.

The process window is narrow: the surface temperature must exceed the austenitizing temperature (to enable transformation) throughout the intended case depth, but must remain below the melting point (surface melting destroys the finish and can cause distortion). Laser power, scan speed and spot size jointly set the peak surface temperature and the depth to which that temperature penetrates before the beam moves on.

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Laser power | 300 – 2500 | W |
| Scan speed | 2 – 40 | mm/s |
| Spot size | 0.5 – 8 | mm |

## Procedure

1. Record the precision score at the default power, scan speed and spot size.
2. Vary laser power alone and record the precision score at each value, noting the qualitative verdict (surface melted / case too shallow / acceptable).
3. Repeat, varying scan speed alone, then spot size alone.
4. Identify the parameter combination that achieves the ~0.8 mm case depth without surface melting, reaching a 90%+ precision score.

## Observation Table

*Table: Effect of laser hardening parameters on case depth and surface integrity*

| Trial | Power (W) | Scan speed (mm/s) | Spot size (mm) | Precision score (%) | Verdict |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
| 8 |  |  |  |  |  |

## Graph

Plot **Precision score (%)** (y-axis) against **Laser power (W)** (x-axis).

Expected trend: an optimum band bounded by insufficient case depth at low power and surface melting at high power.

*Precision score vs laser power, holding scan speed and spot size fixed*

<div class="graph-box">📈 Graph paper / plot area — attach printed or digital graph here</div>

## Calculation

1. Discuss qualitatively how increasing spot size (for fixed power) reduces power density and hence peak surface temperature.
2. State the final optimized (Power, Scan speed, Spot size) combination reaching certification.

## Result

*Table: Optimized parameter set for laser hardening*

| Power (W) | Scan speed (mm/s) | Spot size (mm) | Final precision (%) | Certified? (Y/N) |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Precautions

- Watch specifically for the 'surface melted' verdict at high power/low speed settings and back off before that point.
- Remember that a larger spot size at the same power reduces power density and may under-harden the surface.
