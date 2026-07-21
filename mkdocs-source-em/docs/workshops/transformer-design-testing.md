# WS2: Transformer Design & Testing

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS2: Transformer Design & Testing** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are asked to design a step-down transformer for a specified turns ratio and to minimize losses. Adjust the primary/secondary turns, core material, and winding parameters until the transformer delivers the required output voltage with maximum efficiency and acceptably low core loss.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Turns ratio N₁:N₂ (target set by task) |  | 2–20 | optimal &asymp; 10  |
| Core relative permeability | ×10³ | 1–10 | optimal &asymp; 5 ×10³ |
| Winding resistance (per winding) | mΩ | 10–500 | optimal &asymp; 80 mΩ |

## What You'll Learn

- An ideal transformer's voltage ratio equals its turns ratio, V₂/V₁ = N₂/N₁, and its power is conserved (V₁I₁ = V₂I₂).
- Real transformers lose energy to winding resistance (copper loss, ∝I²R) and to core hysteresis and eddy-current losses (core loss, roughly independent of load).
- A higher core permeability reduces the magnetizing current needed and improves efficiency, but real cores saturate above a material-dependent flux density.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Real transformer testing involves high voltages and hot windings; always follow institutional electrical-safety procedures for physical bench work.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
