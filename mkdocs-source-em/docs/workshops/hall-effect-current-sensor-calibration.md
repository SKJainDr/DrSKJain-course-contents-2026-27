# WS10: Hall-Effect Current Sensor Calibration

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS10: Hall-Effect Current Sensor Calibration** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are calibrating a Hall-effect current sensor for an EV motor-drive inverter. Adjust the sensor's core air-gap, bias current and amplifier gain so that its output tracks the true primary current linearly over the full rated range with minimal offset error.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Core air-gap | mm | 0.2–5 | optimal ≈ 1.5 mm |
| Hall-element bias current | mA | 1–20 | optimal ≈ 8 mA |
| Output amplifier gain | V/T | 10–200 | optimal ≈ 100 V/T |

## What You'll Learn

- A closed-loop Hall-effect current sensor concentrates the magnetic field from the primary conductor through a ferromagnetic core with a small air-gap, in which a Hall element measures the field proportional to the current.
- The air-gap size trades off sensitivity (a narrower gap concentrates more flux through the Hall element) against core saturation margin (too narrow a gap saturates the core at high currents, causing nonlinearity).
- The Hall element's bias current sets its intrinsic sensitivity, and the output amplifier's gain scales the small Hall voltage up to a usable sensor output — both must be matched so the full current range maps onto the sensor's usable output voltage span without clipping.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score reaches 100% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

When calibrating sensors on live motor-drive circuits, ensure proper isolation and rated voltage/current probes; inverter DC-bus voltages can remain dangerously high even after the drive is switched off, due to bus capacitor stored energy.

## Reflection Questions

1. Why does a narrower air-gap increase sensitivity but risk core saturation at high currents?
2. How do the bias current and amplifier gain interact to set the sensor's overall sensitivity (V per A)?
3. What would an offset error in the calibrated sensor cause in a motor-control feedback loop?
4. Why is closed-loop (flux-nulling) Hall sensing generally more accurate than simple open-loop Hall sensing?
5. How does this workshop connect to the Hall-effect carrier-density experiment in this lab's User Guide?
