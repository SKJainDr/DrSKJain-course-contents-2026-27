# WS5: Magnetic Shielding Enclosure Design

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS5: Magnetic Shielding Enclosure Design** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You must design a mu-metal enclosure to protect a sensitive magnetometer from stray laboratory fields. Choose the shield material, thickness, and number of nested layers to achieve the required shielding factor without making the enclosure impractically large or expensive.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Shield material relative permeability | ×10³ | 1–100 | optimal &asymp; 50 ×10³ |
| Shield wall thickness | mm | 0.2–5 | optimal &asymp; 1.5 mm |
| Number of nested shield layers |  | 1–4 | optimal &asymp; 2  |

## What You'll Learn

- High-permeability materials (mu-metal) shield low-frequency and DC magnetic fields by providing a low-reluctance path that diverts flux around the protected volume, unlike electric-field shielding which relies on free charge.
- Shielding factor improves with wall thickness and permeability, but with strongly diminishing returns — doubling thickness rarely doubles the shielding factor.
- Nesting multiple shields with air gaps between them multiplies the overall shielding factor and is often more effective than a single thick shield of the same total material.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Mu-metal loses its high permeability if mechanically stressed or machined without subsequent annealing — this is a real design constraint, not just an academic point.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
