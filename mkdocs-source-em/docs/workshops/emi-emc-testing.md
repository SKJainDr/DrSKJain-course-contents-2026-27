# WS1: EMI/EMC Compliance Testing

<div class="back-note" markdown="1">
&#128295; This is a **hands-on industrial workshop** &mdash; launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and open the **WS1: EMI/EMC Compliance Testing** panel to attempt it interactively. Your score is based on how close each control is set to its optimal (target) value.
</div>

## Scenario

You are a compliance test engineer at a consumer-electronics company. A new switch-mode power supply must pass radiated-emission limits before it can be sold. Your job is to tune the product's shielding and filtering until the measured emission spectrum stays under the regulatory limit line across the required frequency band.

## Controls to Tune

| Control | Unit | Typical Range | Notes |
|---|---|---|---|
| Shielding effectiveness | dB | 0–80 | optimal &asymp; 45 dB |
| EMI filter cutoff frequency | kHz | 10–500 | optimal &asymp; 150 kHz |
| Ground-plane quality index | % | 0–100 | optimal &asymp; 85 % |

## What You'll Learn

- Radiated emissions from switching circuits rise with dI/dt and loop area; shielding and grounding both reduce the effective radiating loop.
- An EMI filter's cutoff must sit below the switching frequency's harmonics that are closest to the regulatory limit, without needlessly attenuating the wanted signal.
- Compliance test labs use a calibrated antenna in an anechoic or open-area test site and compare the measured spectrum against a regulatory limit line (e.g. CISPR/FCC Class B).

## Suggested Approach

1. Read the scenario carefully and identify which physical principle links each control to the outcome you are trying to achieve.
2. Start with each control at its mid-range value and observe the live readout/score.
3. Adjust one control at a time, noting how the score changes, before combining adjustments.
4. Iterate until your score is consistently above 90% &mdash; the simulator awards a printable completion certificate at this level.
5. Once satisfied, note down the final values you converged on and compare them with the underlying formula's prediction of the true optimum.

## Safety Note

Never operate real EMC test equipment or high-power RF sources without supervision; the virtual workshop uses simulated field-strength readings only.

## Reflection Questions

1. Which control had the largest effect on your score, and why does the underlying physics predict that?
2. If two controls both improve the outcome, is their combined effect simply additive, or do they interact? Explain using the relevant formula.
3. In a real industrial setting, which of these controls would be easiest to adjust, and which would be fixed by equipment/material constraints?
4. What would happen to your result if one control were pushed far outside its optimal range — is the penalty symmetric on both sides?
5. How does this workshop's scenario connect to one or more of the 18 experiments in this lab's User Guide?
