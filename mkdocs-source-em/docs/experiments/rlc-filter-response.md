# RLC Filters — Low-Pass / High-Pass / Band-Pass Frequency Response

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="rlc-filter-response"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/rlc-filter-response.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A series R–L–C network driven by a variable-frequency AC source; the output voltage is tapped across a chosen element to realise a low-pass, high-pass or band-pass filter response as frequency is swept.</div>
</div>

## Aim

To compute the frequency-dependent voltage-gain response of a series RLC circuit configured as a band-pass filter, and to locate its resonant (centre) frequency and −3 dB bandwidth.

## Theoretical Background

A series combination of a resistor R, inductor L and capacitor C driven by an AC source of variable frequency behaves very differently depending on which element's voltage is taken as the output. Because the inductive reactance ωL grows with frequency while the capacitive reactance 1/ωC falls with frequency, the net series reactance (ωL − 1/ωC) passes through zero at the resonant frequency ω₀ = 1/√(LC), where the impedance is purely resistive and minimum, and the current (and hence the voltage across R) is maximum. Tapping the output across R therefore realises a band-pass filter, peaking at ω₀ and falling off on either side; the sharpness of this peak is set by the circuit's quality factor Q = ω₀L/R. The same RLC network can equally be configured as a low-pass filter (output across C) or a high-pass filter (output across L), since each element's voltage has a different characteristic frequency dependence — this versatility is why RLC networks are the building blocks of analog filter design.

## Governing Formula

$$ |H(f)|_{bandpass} = \dfrac{R}{\sqrt{R^2 + (\omega L - 1/\omega C)^2}} $$

| Symbol | Meaning |
|---|---|
| \|H(f)\| | band-pass voltage-gain magnitude (dimensionless, 0–1) |
| R | series resistance (Ω) |
| L | series inductance (H) |
| C | series capacitance (F) |
| ω | angular frequency, ω = 2πf (rad/s) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **RLC Filters — Low-Pass / High-Pass / Band-Pass Frequency Response** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Resistance | R | 1–1000 Ω | 100 Ω |
| Inductance | L | 0.1–100 mH | 10 mH |
| Capacitance | C | 0.01–10 µF | 1 µF |
| Signal frequency | f | 10–20000 Hz | 1592 Hz |

## Procedure

1. Fix R, L, C at their default values and sweep f from 10 Hz to 20 kHz, recording the gain |H(f)| at each step.
2. Plot |H(f)| versus f and locate the frequency of maximum gain; compare it with the predicted resonance f₀ = 1/(2π√(LC)).
3. Find the two frequencies on either side of resonance where the gain falls to 1/√2 of its peak value (the −3 dB points), and compute the bandwidth and Q-factor.
4. Increase R and repeat, observing that the peak becomes broader and shorter (lower Q) as R increases.
5. Discuss qualitatively how tapping the output across L instead of R would change the shape of the response curve to a high-pass characteristic.

## Observation Table

| S. No. | f (Hz) | R (Ω) | L (mH) | C (µF) | |H(f)| |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Gain |H(f)| vs frequency f*

<div class="apparatus-3d-wrap graph-wrap" style="background:#FFFDF3;padding:10px;" markdown="1">
<div class="graph-toolbar" markdown="0">
  <span class="graph-hint">&#128203; Click the grid, then paste (Ctrl+V) a copied photo of your reading/meter trace to overlay it for tracing &mdash; nothing is uploaded, it stays on your screen only.</span>
  <span class="graph-toolbar-controls">
    <label>Overlay opacity <input type="range" class="graph-opacity" min="10" max="100" value="65"></label>
    <button type="button" class="graph-clear-btn">Clear pasted image</button>
  </span>
</div>
<div class="graph-canvas-wrap" tabindex="0" title="Click here, then press Ctrl+V to paste your image">
<svg viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#FFFDF3;border-radius:8px;">
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Gain |H(f)| vs frequency f</text>
<line x1="60.00" y1="40" x2="60.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="96.67" y1="40" x2="96.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="133.33" y1="40" x2="133.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="170.00" y1="40" x2="170.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="206.67" y1="40" x2="206.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="243.33" y1="40" x2="243.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="280.00" y1="40" x2="280.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="316.67" y1="40" x2="316.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="353.33" y1="40" x2="353.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="390.00" y1="40" x2="390.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="426.67" y1="40" x2="426.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="463.33" y1="40" x2="463.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="500.00" y1="40" x2="500.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="536.67" y1="40" x2="536.67" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="573.33" y1="40" x2="573.33" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="610.00" y1="40" x2="610.00" y2="465" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="40.00" x2="610" y2="40.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="68.33" x2="610" y2="68.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="96.67" x2="610" y2="96.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="125.00" x2="610" y2="125.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="153.33" x2="610" y2="153.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="181.67" x2="610" y2="181.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="210.00" x2="610" y2="210.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="238.33" x2="610" y2="238.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="266.67" x2="610" y2="266.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="295.00" x2="610" y2="295.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="323.33" x2="610" y2="323.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="351.67" x2="610" y2="351.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="380.00" x2="610" y2="380.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="408.33" x2="610" y2="408.33" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="436.67" x2="610" y2="436.67" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="465.00" x2="610" y2="465.00" stroke="#EDE3C2" stroke-width="0.6"/>
<line x1="60" y1="40" x2="60" y2="465" stroke="#0B173A" stroke-width="2"/>
<line x1="60" y1="465" x2="610" y2="465" stroke="#0B173A" stroke-width="2"/>
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">f (Hz)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">|H(f)|</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Resonant frequency f₀ and Q-factor | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Sweep frequency over a wide enough range to clearly capture both sides of the resonance peak.
- Keep R, L, C fixed while sweeping only f to trace out a single, clean response curve.
- Use a logarithmic frequency axis if the resonance is very sharp (high Q), for clearer visualisation.
- Remember that the −3 dB bandwidth is measured at the half-power (1/√2 amplitude) points, not the half-amplitude points.

## Maximum Permissible Error

$$ \text{Evaluated numerically at each swept frequency; no simple closed-form propagation} $$

The band-pass gain is a non-monomial function of R, L, C and f, so its uncertainty is best explored numerically by perturbing each input in turn rather than via a single algebraic formula.

<div class="error-calc" data-exp="rlc-filter-response"></div>

## Viva-Voce Questions

1. Derive the resonant frequency f₀ = 1/(2π√(LC)) for a series RLC circuit.
2. Define the quality factor Q and explain how it relates to the sharpness of the resonance peak.
3. Explain how the same RLC network can realise low-pass, high-pass and band-pass responses depending on which element's voltage is tapped.
4. What is the phase relationship between current and applied voltage exactly at resonance?
5. Give one practical application of a band-pass RLC filter (e.g. radio tuning circuits).
