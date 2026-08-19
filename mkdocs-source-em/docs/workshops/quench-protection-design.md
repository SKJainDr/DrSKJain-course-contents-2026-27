# WS12: Superconducting Magnet Quench-Protection Design

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS12: Superconducting Magnet Quench-Protection Design** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are designing the quench-protection system for a superconducting magnet coil. Set the dump-resistor value and detection threshold so that, if the coil quenches (loses superconductivity), the stored magnetic energy is safely extracted within the coil's thermal and voltage limits without nuisance-tripping during normal ramp-up.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Dump resistor value | mΩ | 5–200 | optimal ≈ 80 mΩ |
| Quench-voltage detection threshold | mV | 10–500 | optimal ≈ 100 mV |
| Resulting energy discharge time constant | s | 0.5–30 | optimal ≈ 8 s |

## What You'll Learn

- A quench is a sudden, localised loss of superconductivity that causes a normal (resistive) region to form and grow rapidly in the coil, converting stored magnetic energy into heat that can damage the magnet if not safely extracted.
- A dump resistor, switched into the circuit on quench detection, provides an external path to rapidly extract the stored energy (½LI²) as heat outside the magnet, with the discharge time constant L/R set by the dump resistor value.
- The detection threshold must be sensitive enough to catch a genuine quench quickly (before local heating becomes dangerous) but not so sensitive that normal voltage noise during ramp-up trips a costly and unnecessary protective dump.

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score reaches 100% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Superconducting magnets store very large amounts of energy in their field; always follow the facility's quench-protection commissioning and testing procedures, and never bypass or disable protection circuitry to 'simplify' testing.

## Reflection Questions

1. Why does a lower dump-resistor value give a longer energy discharge time constant, and why might that be undesirable?
2. What is the risk of setting the quench-detection threshold too low (too sensitive)? Too high (too insensitive)?
3. Where does the extracted magnetic energy ultimately go during a protected quench?
4. How does the coil's inductance L relate to the choice of dump resistor for a given allowable peak voltage?
5. How does this workshop connect to the magnetic vector potential and Meissner effect experiments in this lab's User Guide?
