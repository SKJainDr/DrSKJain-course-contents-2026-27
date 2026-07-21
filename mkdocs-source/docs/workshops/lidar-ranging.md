# Workshop 7: 📡 LIDAR Ranging

!!! info "Industrial Workshop 7 of 7"
    LIDAR Ranging


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-wsLidar){target=_blank}**

## Workshop Brief

A pulse is fired at an unknown target and its echo is captured on the oscilloscope trace below. Move the measurement cursor onto the centre of the returned echo and set a sensible detection threshold above the noise floor, then read off the corresponding distance.

**Specifications:** Estimate the true target distance · Avoid false triggers from noise

## Process Theory

LIDAR (Light Detection And Ranging) measures distance by timing the round trip of a short laser pulse from the instrument to a target and back. If the pulse departs at t = 0 and its echo is detected at a round-trip time t_RT, the one-way distance to the target is R = c·t_RT / 2, since the pulse travels the distance twice (out and back) at the speed of light c.

In a real detector, the returned echo sits on top of a noisy baseline (background light, detector and amplifier noise). A detection threshold must be set high enough above the noise floor to avoid false triggers from noise spikes, but low enough that the genuine (possibly weak) echo is not missed.

The measurement cursor should be placed at the temporal centre (or leading edge, depending on convention) of the true echo pulse; placing it on a noise spike instead, or offsetting it from the true echo centre, directly translates into a ranging error via R = c·t_RT/2.

## Process Parameters

| Parameter | Range | Unit |
|---|---|---|
| Measurement cursor (round-trip time) | 100 – 500 | ns |
| Detection threshold | 10 – 90 | % |

## Procedure

1. Set the detection threshold to a low value first and note how many noise spikes exceed it (false triggers).
2. Increase the threshold until only the genuine echo pulse remains above it, and record this threshold value.
3. Move the measurement cursor across the trace and identify the round-trip time at the centre of the genuine echo.
4. Read the estimated distance and precision score from the readouts; adjust cursor and threshold together to maximize the precision score.

## Observation Table

*Table: Effect of detection threshold and cursor placement on ranging precision*

| Trial | Threshold (%) | Cursor position (ns) | Estimated distance (m) | Precision score (%) | Verdict |
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

Plot **Precision score (%)** (y-axis) against **Cursor position (ns)** (x-axis).

Expected trend: a sharp peak at the round-trip time corresponding to the true echo centre.

*Precision score vs cursor position at a fixed, appropriately-set threshold*

<div class="graph-box">📈 Graph paper / plot area — attach printed or digital graph here</div>

## Calculation

1. Using R = c·t_RT/2 with c = 3×10^8 m/s, compute the estimated distance for the cursor position judged to be at the echo centre.
2. Compare this calculated distance with the simulator's displayed 'estimated distance' and comment on any discrepancy.

## Result

*Table: LIDAR range determination*

| t_RT at echo centre (ns) | R = c·t_RT/2 (m) calculated | R (simulator, m) | Final precision (%) |
|---|---|---|---|
| 1 |  |  |  |

## Precautions

- Always set the threshold above the noise floor before trusting any cursor-based distance reading.
- Distinguish a genuine echo (broader, consistent shape) from a narrow noise spike before centring the cursor on it.
