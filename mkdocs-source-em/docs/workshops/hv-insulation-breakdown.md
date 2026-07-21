# WS6: High-Voltage Insulation & Breakdown (Paschen) Testing

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS6: High-Voltage Insulation & Breakdown (Paschen) Testing** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are testing the insulation of a high-voltage gas-filled switchgear enclosure. Adjust the gas pressure and electrode gap to keep the system operating safely below its breakdown voltage, using the Paschen curve to avoid the dangerous low-pressure breakdown minimum.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Gas pressure | kPa | 1–300 | optimal &asymp; 100 kPa |
| Electrode gap | mm | 0.5–20 | optimal &asymp; 8 mm |
| Applied test voltage | kV | 1–50 | optimal &asymp; 20 kV |

## What You'll Learn

- Paschen's law shows breakdown voltage depends on the product of pressure and gap (pd), not on either alone, and has a characteristic minimum at a specific pd value.
- Operating near the Paschen minimum is dangerous because a small drop in pressure (e.g. from a leak) can sharply reduce the breakdown voltage rather than increase it, counter to naive intuition.
- Increasing the gap at fixed pressure eventually raises breakdown voltage again (right side of the Paschen curve), which is why high-voltage equipment is designed with generous clearances.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

High-voltage breakdown testing is genuinely hazardous; this workshop is a safe numerical model only and is not a substitute for certified high-voltage laboratory training.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
