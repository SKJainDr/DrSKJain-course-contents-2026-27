# Workshop 5: 🧵 Laser Chemical Vapour Deposition (LCVD)

!!! info "Industrial Workshop 5 of 7"
    Laser Chemical Vapour Deposition (LCVD)


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-wsLCVD){target=_blank}**

## Workshop Brief

Decompose WF₆ precursor gas with a focused laser to deposit a ~200 nm tungsten film on a substrate. Aim for a uniform thickness across the scanned area — too little power/gas starves growth, too much causes uneven, over-thick deposits.

**Specifications:** Precursor: WF₆ · Target: 200 nm, uniform

## Process Theory

In laser chemical vapour deposition (LCVD), a focused laser beam locally heats a substrate in the presence of a precursor gas (tungsten hexafluoride, WF₆), driving a thermally activated decomposition reaction that deposits solid tungsten onto the heated area while volatile by-products are carried away by the gas flow.

The deposition rate depends on the local substrate temperature (set by laser power and spot size, not separately controlled here) and on the local precursor gas concentration (set by the gas flow rate) available at the reaction site; growth is starved if either laser power or gas flow is too low.

Scan speed determines the dwell time of the laser at any point on the substrate: a slower scan allows more material to deposit at each point (thicker, but potentially non-uniform if too slow) while a faster scan spreads the same total energy/precursor exposure more thinly but more uniformly, provided growth does not become diffusion-limited.

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Laser power | 2 – 40 | W |
| Precursor gas flow | 2 – 60 | sccm |
| Scan speed | 0.2 – 8 | mm/s |

## Procedure

1. Record the precision score at the default power, gas flow and scan speed.
2. Vary laser power alone and record the precision score at each value.
3. Repeat, varying precursor gas flow alone, then scan speed alone.
4. Identify the parameter combination giving a uniform ~200 nm film with a 90%+ precision score.

## Observation Table

*Table: Effect of LCVD parameters on tungsten film uniformity*

| Trial | Power (W) | Gas flow (sccm) | Scan speed (mm/s) | Precision score (%) | Verdict |
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

Plot **Precision score (%)** (y-axis) against **Scan speed (mm/s)** (x-axis).

Expected trend: an optimum band — too slow overgrows/non-uniform, too fast under-deposits.

*Precision score vs scan speed, holding power and gas flow fixed*

<div class="graph-box">📈 Graph paper / plot area — attach printed or digital graph here</div>

## Calculation

1. Discuss qualitatively whether the growth in each trial is more likely to be reaction-rate-limited (laser power/temperature dependent) or supply-limited (gas-flow dependent).
2. State the final optimized (Power, Gas flow, Scan speed) combination reaching certification.

## Result

*Table: Optimized parameter set for LCVD tungsten deposition*

| Power (W) | Gas flow (sccm) | Scan speed (mm/s) | Final precision (%) | Certified? (Y/N) |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Precautions

- Distinguish reaction-rate-limited growth (increase power) from supply-limited growth (increase gas flow) before adjusting parameters.
- Sweep scan speed over its full range, since both very slow and very fast values can degrade uniformity.
