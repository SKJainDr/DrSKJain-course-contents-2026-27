# WS4: Eddy-Current Non-Destructive Testing

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS4: Eddy-Current Non-Destructive Testing** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are a quality-control inspector using eddy-current testing to find hidden cracks in an aluminium aircraft panel without damaging it. Tune the probe's coil frequency and lift-off distance to maximize flaw sensitivity while keeping the background signal noise low enough to avoid false alarms.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Probe coil frequency | kHz | 1–500 | optimal &asymp; 100 kHz |
| Probe lift-off distance | mm | 0.1–5 | optimal &asymp; 0.5 mm |
| Signal amplifier gain | dB | 0–60 | optimal &asymp; 30 dB |

## What You'll Learn

- An eddy-current probe induces circulating currents in a conductive sample; a crack disrupts these currents and changes the coil's impedance, which is detected as a signal.
- Higher frequency confines eddy currents nearer the surface (thanks to the skin-depth effect) giving better sensitivity to surface cracks but less penetration depth for buried flaws.
- Increasing the 'lift-off' (probe-to-surface gap) strongly reduces coupling and sensitivity — lift-off variation is one of the most common sources of false signals in the field.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Real eddy-current NDT equipment is low-power and safe, but proper calibration against reference standards is essential before any real inspection.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
