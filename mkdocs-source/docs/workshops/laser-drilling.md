# Workshop 1: 🕳️ Laser Drilling

!!! info "Industrial Workshop 1 of 7"
    Laser Drilling


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-wsDrilling){target=_blank}**

## Workshop Brief

Drill a precision blind hole in a 2 mm stainless-steel sheet using a pulsed Nd:YAG laser. Aim for a clean, round hole with minimal heat-affected zone (HAZ) — too little energy leaves the hole incomplete; too much energy or too many pulses widens the HAZ and distorts the hole.

**Specifications:** Target Ø 0.5 mm · Target depth 2.0 mm · Material: SS304 · Minimal HAZ

## Process Theory

Laser drilling uses a pulsed, high-peak-power laser (typically Q-switched Nd:YAG) focused to a small spot to rapidly melt and vaporize material, ejecting molten material from the hole by vapour pressure and assist-gas flow. Each pulse removes a thin layer of material; repeated pulses progressively deepen the hole.

The key trade-off is between material removal rate and heat-affected zone (HAZ): higher pulse energy and longer pulse duration deliver more energy per pulse (faster material removal) but allow more heat to conduct sideways into the surrounding material, widening the HAZ, distorting the hole geometry, and potentially causing recast/cracking. Too few pulses or too little energy per pulse fails to reach the required depth.

Process parameters must therefore be tuned jointly: pulse energy and duration set the peak power density and thermal penetration per pulse, while the number of pulses sets the cumulative depth achieved.

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Pulse energy | 10 – 150 | mJ |
| Pulse duration | 1 – 50 | ns |
| Number of pulses | 20 – 400 | — |

## Procedure

1. Start with the default pulse energy, duration and pulse count and note the precision score and verdict shown by the simulator.
2. Systematically vary pulse energy alone (holding duration and pulse count fixed) and record the precision score at each setting.
3. Repeat, varying pulse duration alone, then the number of pulses alone.
4. From the three sweeps, identify the combination of parameters that maximizes the precision score (target: 90%+ for certification).
5. Record the final certified parameter set once the 90%+ precision threshold is reached.

## Observation Table

*Table: Effect of pulsed Nd:YAG parameters on drilling precision*

| Trial | Pulse energy (mJ) | Pulse duration (ns) | No. of pulses | Precision score (%) | Verdict |
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

Plot **Precision score (%)** (y-axis) against **Pulse energy (mJ)** (x-axis).

Expected trend: a peak at an intermediate pulse energy, falling off both at very low energy (incomplete hole) and very high energy (excess HAZ).

*Precision score vs pulse energy, holding other parameters fixed*

<div class="graph-box">📈 Graph paper / plot area — attach printed or digital graph here</div>

## Calculation

1. Tabulate precision score against each swept parameter and identify the optimum region for each.
2. State the final parameter combination used to reach the 90%+ certification threshold.

## Result

*Table: Optimized parameter set for laser drilling*

| Pulse energy (mJ) | Pulse duration (ns) | No. of pulses | Final precision (%) | Certified? (Y/N) |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Precautions

- Increase pulse energy and pulse count gradually rather than jumping to extreme values, to see the precision trend clearly.
- Note that both too little and too much energy reduce precision — the optimum lies at an intermediate value.
