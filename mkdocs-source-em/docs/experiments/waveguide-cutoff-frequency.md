# Rectangular Waveguide — TE₁₀ Mode & Cutoff Frequency

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="waveguide-cutoff-frequency"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/waveguide-cutoff-frequency.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A rectangular metallic waveguide of broad-wall dimension a; the dominant TE₁₀ mode propagates only above its cutoff frequency f_c = c/2a, below which the field is evanescent and decays exponentially along the guide.</div>
</div>

## Aim

To compute the cutoff frequency of the dominant TE₁₀ mode of a rectangular waveguide from its broad-wall dimension, and determine whether a given signal frequency will propagate or be evanescently attenuated.

## Theoretical Background

Unlike a coaxial cable or a simple pair of wires, a hollow rectangular metallic waveguide cannot support a signal at every frequency: for each mode (a particular transverse field pattern satisfying the boundary conditions on the conducting walls), there is a minimum cutoff frequency f_c below which the wave cannot propagate and instead decays exponentially with distance along the guide (an evanescent wave). The dominant, lowest-cutoff mode of a rectangular guide is TE₁₀, whose cutoff frequency depends only on the guide's broad-wall dimension a: f_c = c/(2a). Operating well above cutoff (but below the cutoff of the next higher mode) ensures single-mode propagation with low loss, which is why waveguide dimensions are chosen very deliberately in radar, satellite and microwave engineering to match the intended operating frequency band.

## Governing Formula

$$ f_c(TE_{10}) = \dfrac{c}{2a} $$

| Symbol | Meaning |
|---|---|
| f_c | cutoff frequency of the TE₁₀ mode (Hz) |
| c | speed of light in vacuum |
| a | waveguide broad-wall (longer transverse) dimension (m) |
| f | actual signal frequency being tested (Hz) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Rectangular Waveguide — TE₁₀ Mode & Cutoff Frequency** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Waveguide broad-wall dimension | a | 1–10 cm | 2.29 cm |
| Signal frequency | f | 1–20 GHz | 9 GHz |

## Procedure

1. Fix a = 2.29 cm (a standard X-band waveguide dimension) and compute f_c.
2. Vary the signal frequency f from 1 GHz to 20 GHz and, for each value, note whether the simulator reports propagation or evanescent attenuation.
3. Vary the broad-wall dimension a and observe how f_c shifts; verify f_c ∝ 1/a by plotting f_c versus 1/a.
4. Determine the range of a for which a fixed signal frequency (e.g. 9 GHz) propagates in the dominant mode only (i.e. above the TE₁₀ cutoff but below the next mode's cutoff, roughly 2f_c).
5. Discuss why waveguides are generally unsuitable for carrying signals at frequencies much below the microwave range (the required a would become impractically large).

## Observation Table

| S. No. | a (cm) | f_c (GHz) | f tested (GHz) | Propagates? (Y/N) |
|---|---|---|---|---||
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Graph

*Cutoff frequency f_c vs 1/a*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Cutoff frequency f_c vs 1/a</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">1/a (1/cm)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">f_c (GHz)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of f_c vs 1/a (→ c/2) | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Remember the cutoff condition depends only on the broad-wall dimension a for the TE₁₀ mode, not on the narrower dimension b.
- Operate the guide below the cutoff of the next higher-order mode to avoid multi-mode propagation.
- Change only a or f at a time when tabulating.
- Treat the waveguide walls as perfectly conducting for this idealised cutoff calculation.

## Maximum Permissible Error

$$ \dfrac{\Delta f_c}{f_c} = \dfrac{\Delta a}{a} $$

f_c = c/(2a) is inversely proportional to a alone, so its fractional error equals that of the measured dimension a.

<div class="error-calc" data-exp="waveguide-cutoff-frequency"></div>

## Viva-Voce Questions

1. Explain physically why a hollow waveguide has a cutoff frequency while a coaxial cable does not.
2. Derive the TE₁₀ cutoff frequency from the boundary conditions on the waveguide walls.
3. What happens to a signal launched below the cutoff frequency?
4. Why is TE₁₀ called the 'dominant mode'?
5. How would you choose waveguide dimensions for an X-band radar system operating near 9–10 GHz?
