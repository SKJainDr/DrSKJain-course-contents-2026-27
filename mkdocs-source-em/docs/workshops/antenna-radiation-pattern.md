# WS3: Antenna Radiation Pattern & Gain Optimization

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS3: Antenna Radiation Pattern & Gain Optimization** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are optimizing a dipole antenna array for a communications link. Adjust the element length, spacing, and phasing to maximize gain in the desired direction while keeping the sidelobe level and beamwidth within the specified mission requirements.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Element length (in wavelengths) | λ | 0.3–1.0 | optimal &asymp; 0.5 λ |
| Array element spacing | λ | 0.25–1.0 | optimal &asymp; 0.5 λ |
| Inter-element phase shift | ° | 0–180 | optimal &asymp; 0 ° |

## What You'll Learn

- A half-wave dipole (length ≈ 0.5λ) is resonant and radiates efficiently with a well-known figure-8 pattern.
- Combining elements into an array allows the radiation pattern to be shaped ('beamformed') by controlling element spacing and relative phase.
- Element spacing near λ (with in-phase feeding) can introduce unwanted grating lobes, while too-close spacing increases mutual coupling losses.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

This workshop models field strength only; never approach an energized transmitting antenna in a real installation without proper RF-exposure precautions.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
