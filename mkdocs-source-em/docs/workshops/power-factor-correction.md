# WS8: Power-Factor Correction Capacitor Bank Sizing

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS8: Power-Factor Correction Capacitor Bank Sizing** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

A factory's inductive machine load is dragging its power factor down, incurring utility penalties. You must size a shunt capacitor bank and select its switching stages so that the plant's power factor is corrected close to unity without overcorrecting into leading-VAR territory that would also attract a penalty.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Capacitor bank rating | kVAR | 50–500 | optimal ≈ 280 kVAR |
| Number of switched stages |  | 1–8 | optimal ≈ 4 |
| Resulting power factor ×100 |  | 70–100 | optimal ≈ 98 |

## What You'll Learn

- A lagging power factor, typical of plants dominated by induction motors, means the supply must carry extra reactive current that does no real work but still incurs I²R losses and utility demand charges.
- Shunt capacitors supply local reactive power, cancelling the inductive VARs drawn from the grid and raising the power factor towards unity.
- Switching the bank in discrete stages, rather than a single fixed block, lets the correction track the load's varying reactive demand through the day without ever overcorrecting into a leading (capacitive) power factor, which utilities penalise just as much as a lagging one.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score reaches 100% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Capacitor banks store significant energy even after disconnection; always follow lockout/discharge procedures before any physical maintenance, and never switch a bank while it still carries residual charge from a previous de-energisation.

## Reflection Questions

1. Why does a purely resistive load have a power factor of exactly 1, requiring no correction?
2. What would happen to the plant's power factor if the capacitor bank were oversized for a light-load period?
3. How does staged switching help match reactive compensation to a load that varies through the day?
4. In a real installation, which of these controls is fixed at design time and which can be adjusted automatically in real time?
5. How does this workshop connect to the RLC filter response and transmission-line experiments in this lab's User Guide?
