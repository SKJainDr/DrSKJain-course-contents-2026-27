# WS11: Waveguide Feed Design for a Radar Front-End

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS11: Waveguide Feed Design for a Radar Front-End** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are designing the waveguide feed for a radar transmitter. Choose the waveguide broad-wall dimension and operating frequency margin above cutoff so that only the dominant TE₁₀ mode propagates with low attenuation, avoiding both evanescent cutoff and higher-order mode breakthrough.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Waveguide broad-wall dimension a | cm | 1–8 | optimal ≈ 2.29 cm |
| Operating frequency above cutoff | % | 0–100 | optimal ≈ 30% |
| Resulting insertion loss | dB | 0–10 | optimal ≈ 0.5 dB |

## What You'll Learn

- Every waveguide mode has its own cutoff frequency; the dominant TE₁₀ mode has the lowest cutoff, and operating too close to it causes rapidly rising attenuation and phase distortion.
- Operating too far above the TE₁₀ cutoff risks exceeding the cutoff of the next higher-order mode, which can then also propagate and interfere with the desired single-mode signal.
- Waveguide dimensions are therefore chosen so the intended operating frequency sits in a 'sweet spot' comfortably above the dominant mode's cutoff but safely below the next mode's cutoff.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score reaches 100% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

High-power radar transmitters can produce dangerous levels of microwave radiation at waveguide flanges and joints; never work on an energised waveguide run, and always confirm isolation and follow RF exposure safety procedures.

## Reflection Questions

1. Why is operating exactly at the cutoff frequency undesirable, even though the mode technically 'propagates' just above it?
2. What happens if the chosen frequency is pushed too far above the TE₁₀ cutoff?
3. How does the broad-wall dimension a set both the cutoff frequency and the usable single-mode bandwidth?
4. Why is TE₁₀ preferred as the operating mode over higher-order modes?
5. How does this workshop connect to the rectangular-waveguide cutoff-frequency experiment in this lab's User Guide?
