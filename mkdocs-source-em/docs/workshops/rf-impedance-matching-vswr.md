# WS7: RF Impedance Matching & VSWR Minimization

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS7: RF Impedance Matching & VSWR Minimization** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are commissioning an RF transmitter feeding an antenna through a coaxial cable. Tune a matching network (adjustable reactive elements) so that the load impedance seen by the transmitter is as close as possible to the cable's characteristic impedance, minimizing the voltage standing-wave ratio (VSWR) and reflected power.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Shunt matching reactance | Ω | -200–200 | optimal &asymp; 0 Ω |
| Series matching reactance | Ω | -200–200 | optimal &asymp; 0 Ω |
| Load resistance seen at antenna feed | Ω | 10–200 | optimal &asymp; 50 Ω |

## What You'll Learn

- VSWR = (1+|Γ|)/(1−|Γ|), where Γ is the reflection coefficient at the load; a perfectly matched load (Z_load = Z₀) gives Γ = 0 and VSWR = 1.
- An L-section matching network of series and shunt reactive elements can transform almost any load impedance to match a transmission line's characteristic impedance at a single frequency.
- High VSWR reflects power back toward the transmitter, reducing delivered power and potentially damaging the transmitter's output stage if severe enough.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

This workshop models RF power and impedance numerically; never work on an energized transmitter or antenna feedline without RF-safety training and proper lockout procedures.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
