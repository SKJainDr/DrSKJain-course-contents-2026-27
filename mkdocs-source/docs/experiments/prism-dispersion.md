# 4. Dispersion by a Prism

!!! abstract "Module"
    Wave Optics · Module 4


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-dispersion){target=_blank}**

## Aim

To study how a prism separates white light into its constituent colours due to the wavelength dependence of refractive index (normal dispersion).

## Theoretical Background

The refractive index n of an optical material is not a single constant but depends weakly on the wavelength of light passing through it. For most transparent materials in the visible range, n decreases smoothly as wavelength increases — a behaviour termed normal dispersion, empirically described by Cauchy's relation n(λ) = A + B/λ², where A and B are material constants.

Because the angle of deviation produced by a prism depends on the refractive index of the prism material at that wavelength, violet light (higher n) is deviated more than red light (lower n) for the same apex angle. A prism therefore spreads an incident beam of white light into a continuous spectrum from red to violet, unlike a mirror, which reflects all wavelengths by the same angle.

The overall spread of colours (the dispersive power) depends both on the apex angle A of the prism and on the intrinsic dispersion of its material — the difference (n_violet − n_red) relative to (n_yellow − 1).

## Governing Formulas

**Cauchy's dispersion relation:**

$$
n(\lambda) = A + \dfrac{B}{\lambda^2}
$$

**Prism deviation (thin-prism / small-angle approximation):**

$$
\delta \approx (n-1)A_{\text{apex}}
$$

**Dispersive power:**

$$
\omega = \dfrac{n_v - n_r}{n_y - 1}
$$

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="prism-dispersion"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/prism-dispersion.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic below for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; White light &rarr; slit &rarr; prism &rarr; spectrum screen</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Prism apex angle | A | 20 – 70 | ° |
| Dispersive power (exaggerated for visibility) | — | 1 – 10 | arb. units |

## Procedure

1. Set the prism apex angle to a fixed value and observe the spread of the emergent spectrum for a low dispersive-power setting.
2. Progressively increase the dispersive-power control and note the increasing angular separation between red and violet in the emergent beam.
3. Repeat for at least three different apex angles A and tabulate the qualitative spread of the spectrum in each case.
4. Sketch/record the relative bending of red, yellow and violet rays for one representative setting.

## Observation Table

*Table: Effect of apex angle and dispersive power on the emergent spectrum*

| S. No. | Apex angle A (°) | Dispersive power setting | Qualitative spectral spread (narrow/medium/wide) |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Graph

Plot **Relative angular spread of spectrum** (y-axis) against **Apex angle A (°)** (x-axis).

Expected trend: an increasing trend with A.

*Qualitative trend of spectral spread with prism apex angle*

<div class="apparatus-3d-wrap graph-wrap" style="background:#FFFDF3;padding:10px;" markdown="1">
<div class="graph-toolbar" markdown="0">
  <span class="graph-hint">&#128203; Click the grid, then paste (Ctrl+V) a copied photo of your camera/CRO/DSO trace to overlay it for tracing &mdash; nothing is uploaded, it stays on your screen only.</span>
  <span class="graph-toolbar-controls">
    <label>Overlay opacity <input type="range" class="graph-opacity" min="10" max="100" value="65"></label>
    <button type="button" class="graph-clear-btn">Clear pasted image</button>
  </span>
</div>
<div class="graph-canvas-wrap" tabindex="0" title="Click here, then press Ctrl+V to paste your camera/CRO/DSO image">
<svg viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#FFFDF3;border-radius:8px;">
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Refractive Index vs 1/λ² (Cauchy plot)</text>
<line x1="73.67" y1="40.0" x2="73.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="77.33" y1="40.0" x2="77.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="81.0" y1="40.0" x2="81.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="84.67" y1="40.0" x2="84.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="88.33" y1="40.0" x2="88.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="92.0" y1="40.0" x2="92.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="95.67" y1="40.0" x2="95.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="99.33" y1="40.0" x2="99.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="103.0" y1="40.0" x2="103.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="106.67" y1="40.0" x2="106.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="110.33" y1="40.0" x2="110.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="114.0" y1="40.0" x2="114.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="117.67" y1="40.0" x2="117.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="121.33" y1="40.0" x2="121.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="125.0" y1="40.0" x2="125.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="128.67" y1="40.0" x2="128.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="132.33" y1="40.0" x2="132.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="136.0" y1="40.0" x2="136.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="139.67" y1="40.0" x2="139.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="143.33" y1="40.0" x2="143.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="147.0" y1="40.0" x2="147.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="150.67" y1="40.0" x2="150.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="154.33" y1="40.0" x2="154.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="158.0" y1="40.0" x2="158.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="161.67" y1="40.0" x2="161.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="165.33" y1="40.0" x2="165.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="169.0" y1="40.0" x2="169.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="172.67" y1="40.0" x2="172.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="176.33" y1="40.0" x2="176.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="180.0" y1="40.0" x2="180.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="183.67" y1="40.0" x2="183.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="187.33" y1="40.0" x2="187.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="191.0" y1="40.0" x2="191.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="194.67" y1="40.0" x2="194.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="198.33" y1="40.0" x2="198.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="202.0" y1="40.0" x2="202.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="205.67" y1="40.0" x2="205.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="209.33" y1="40.0" x2="209.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="213.0" y1="40.0" x2="213.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="216.67" y1="40.0" x2="216.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="220.33" y1="40.0" x2="220.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="224.0" y1="40.0" x2="224.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="227.67" y1="40.0" x2="227.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="231.33" y1="40.0" x2="231.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="235.0" y1="40.0" x2="235.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="238.67" y1="40.0" x2="238.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="242.33" y1="40.0" x2="242.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="246.0" y1="40.0" x2="246.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="249.67" y1="40.0" x2="249.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="257.0" y1="40.0" x2="257.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="260.67" y1="40.0" x2="260.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="264.33" y1="40.0" x2="264.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="268.0" y1="40.0" x2="268.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="271.67" y1="40.0" x2="271.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="275.33" y1="40.0" x2="275.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="279.0" y1="40.0" x2="279.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="282.67" y1="40.0" x2="282.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="286.33" y1="40.0" x2="286.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="290.0" y1="40.0" x2="290.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="293.67" y1="40.0" x2="293.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="297.33" y1="40.0" x2="297.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="301.0" y1="40.0" x2="301.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="304.67" y1="40.0" x2="304.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="308.33" y1="40.0" x2="308.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="312.0" y1="40.0" x2="312.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="315.67" y1="40.0" x2="315.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="319.33" y1="40.0" x2="319.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="323.0" y1="40.0" x2="323.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="326.67" y1="40.0" x2="326.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="330.33" y1="40.0" x2="330.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="334.0" y1="40.0" x2="334.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="337.67" y1="40.0" x2="337.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="341.33" y1="40.0" x2="341.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="345.0" y1="40.0" x2="345.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="348.67" y1="40.0" x2="348.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="352.33" y1="40.0" x2="352.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="356.0" y1="40.0" x2="356.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="359.67" y1="40.0" x2="359.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="363.33" y1="40.0" x2="363.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="367.0" y1="40.0" x2="367.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="370.67" y1="40.0" x2="370.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="374.33" y1="40.0" x2="374.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="378.0" y1="40.0" x2="378.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="381.67" y1="40.0" x2="381.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="385.33" y1="40.0" x2="385.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="389.0" y1="40.0" x2="389.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="392.67" y1="40.0" x2="392.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="396.33" y1="40.0" x2="396.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="400.0" y1="40.0" x2="400.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="403.67" y1="40.0" x2="403.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="407.33" y1="40.0" x2="407.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="411.0" y1="40.0" x2="411.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="414.67" y1="40.0" x2="414.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="418.33" y1="40.0" x2="418.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="422.0" y1="40.0" x2="422.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="425.67" y1="40.0" x2="425.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="429.33" y1="40.0" x2="429.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="433.0" y1="40.0" x2="433.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="440.33" y1="40.0" x2="440.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="444.0" y1="40.0" x2="444.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="447.67" y1="40.0" x2="447.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="451.33" y1="40.0" x2="451.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="455.0" y1="40.0" x2="455.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="458.67" y1="40.0" x2="458.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="462.33" y1="40.0" x2="462.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="466.0" y1="40.0" x2="466.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="469.67" y1="40.0" x2="469.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="473.33" y1="40.0" x2="473.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="477.0" y1="40.0" x2="477.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="480.67" y1="40.0" x2="480.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="484.33" y1="40.0" x2="484.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="488.0" y1="40.0" x2="488.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="491.67" y1="40.0" x2="491.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="495.33" y1="40.0" x2="495.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="499.0" y1="40.0" x2="499.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="502.67" y1="40.0" x2="502.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="506.33" y1="40.0" x2="506.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="510.0" y1="40.0" x2="510.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="513.67" y1="40.0" x2="513.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="517.33" y1="40.0" x2="517.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="521.0" y1="40.0" x2="521.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="524.67" y1="40.0" x2="524.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="528.33" y1="40.0" x2="528.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="532.0" y1="40.0" x2="532.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="535.67" y1="40.0" x2="535.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="539.33" y1="40.0" x2="539.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="543.0" y1="40.0" x2="543.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="546.67" y1="40.0" x2="546.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="550.33" y1="40.0" x2="550.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="554.0" y1="40.0" x2="554.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="557.67" y1="40.0" x2="557.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="561.33" y1="40.0" x2="561.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="565.0" y1="40.0" x2="565.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="568.67" y1="40.0" x2="568.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="572.33" y1="40.0" x2="572.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="576.0" y1="40.0" x2="576.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="579.67" y1="40.0" x2="579.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="583.33" y1="40.0" x2="583.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="587.0" y1="40.0" x2="587.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="590.67" y1="40.0" x2="590.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="594.33" y1="40.0" x2="594.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="598.0" y1="40.0" x2="598.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="601.67" y1="40.0" x2="601.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="605.33" y1="40.0" x2="605.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="609.0" y1="40.0" x2="609.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="612.67" y1="40.0" x2="612.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="616.33" y1="40.0" x2="616.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="42.83" x2="620.0" y2="42.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="45.67" x2="620.0" y2="45.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="48.50" x2="620.0" y2="48.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="51.33" x2="620.0" y2="51.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="54.17" x2="620.0" y2="54.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="57.0" x2="620.0" y2="57.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="59.83" x2="620.0" y2="59.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="62.67" x2="620.0" y2="62.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="65.50" x2="620.0" y2="65.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="68.33" x2="620.0" y2="68.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="71.17" x2="620.0" y2="71.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="74.0" x2="620.0" y2="74.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="76.83" x2="620.0" y2="76.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="79.67" x2="620.0" y2="79.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="82.50" x2="620.0" y2="82.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="85.33" x2="620.0" y2="85.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="88.17" x2="620.0" y2="88.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="91.0" x2="620.0" y2="91.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="93.83" x2="620.0" y2="93.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="96.67" x2="620.0" y2="96.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="99.50" x2="620.0" y2="99.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="102.33" x2="620.0" y2="102.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="105.17" x2="620.0" y2="105.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="108.0" x2="620.0" y2="108.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="110.83" x2="620.0" y2="110.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="113.67" x2="620.0" y2="113.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="116.50" x2="620.0" y2="116.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="119.33" x2="620.0" y2="119.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="122.17" x2="620.0" y2="122.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="125.0" x2="620.0" y2="125.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="127.83" x2="620.0" y2="127.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="130.67" x2="620.0" y2="130.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="133.50" x2="620.0" y2="133.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="136.33" x2="620.0" y2="136.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="139.17" x2="620.0" y2="139.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="142.0" x2="620.0" y2="142.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="144.83" x2="620.0" y2="144.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="147.67" x2="620.0" y2="147.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="150.50" x2="620.0" y2="150.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="153.33" x2="620.0" y2="153.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="156.17" x2="620.0" y2="156.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="159.0" x2="620.0" y2="159.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="161.83" x2="620.0" y2="161.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="164.67" x2="620.0" y2="164.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="167.50" x2="620.0" y2="167.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="170.33" x2="620.0" y2="170.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="173.17" x2="620.0" y2="173.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="176.0" x2="620.0" y2="176.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="178.83" x2="620.0" y2="178.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="184.50" x2="620.0" y2="184.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="187.33" x2="620.0" y2="187.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="190.17" x2="620.0" y2="190.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="193.0" x2="620.0" y2="193.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="195.83" x2="620.0" y2="195.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="198.67" x2="620.0" y2="198.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="201.50" x2="620.0" y2="201.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="204.33" x2="620.0" y2="204.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="207.17" x2="620.0" y2="207.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="210.0" x2="620.0" y2="210.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="212.83" x2="620.0" y2="212.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="215.67" x2="620.0" y2="215.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="218.50" x2="620.0" y2="218.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="221.33" x2="620.0" y2="221.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="224.17" x2="620.0" y2="224.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="227.0" x2="620.0" y2="227.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="229.83" x2="620.0" y2="229.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="232.67" x2="620.0" y2="232.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="235.50" x2="620.0" y2="235.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="238.33" x2="620.0" y2="238.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="241.17" x2="620.0" y2="241.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="244.0" x2="620.0" y2="244.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="246.83" x2="620.0" y2="246.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="249.67" x2="620.0" y2="249.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="252.50" x2="620.0" y2="252.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="255.33" x2="620.0" y2="255.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="258.17" x2="620.0" y2="258.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="261.0" x2="620.0" y2="261.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="263.83" x2="620.0" y2="263.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="266.67" x2="620.0" y2="266.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="269.50" x2="620.0" y2="269.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="272.33" x2="620.0" y2="272.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="275.17" x2="620.0" y2="275.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="278.0" x2="620.0" y2="278.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="280.83" x2="620.0" y2="280.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="283.67" x2="620.0" y2="283.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="286.50" x2="620.0" y2="286.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="289.33" x2="620.0" y2="289.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="292.17" x2="620.0" y2="292.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="295.0" x2="620.0" y2="295.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="297.83" x2="620.0" y2="297.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="300.67" x2="620.0" y2="300.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="303.50" x2="620.0" y2="303.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="306.33" x2="620.0" y2="306.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="309.17" x2="620.0" y2="309.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="312.0" x2="620.0" y2="312.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="314.83" x2="620.0" y2="314.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="317.67" x2="620.0" y2="317.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="320.50" x2="620.0" y2="320.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="326.17" x2="620.0" y2="326.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="329.0" x2="620.0" y2="329.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="331.83" x2="620.0" y2="331.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="334.67" x2="620.0" y2="334.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="337.50" x2="620.0" y2="337.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="340.33" x2="620.0" y2="340.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="343.17" x2="620.0" y2="343.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="346.0" x2="620.0" y2="346.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="348.83" x2="620.0" y2="348.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="351.67" x2="620.0" y2="351.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="354.50" x2="620.0" y2="354.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="357.33" x2="620.0" y2="357.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="360.17" x2="620.0" y2="360.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="363.0" x2="620.0" y2="363.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="365.83" x2="620.0" y2="365.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="368.67" x2="620.0" y2="368.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="371.50" x2="620.0" y2="371.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="374.33" x2="620.0" y2="374.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="377.17" x2="620.0" y2="377.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="380.0" x2="620.0" y2="380.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="382.83" x2="620.0" y2="382.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="385.67" x2="620.0" y2="385.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="388.50" x2="620.0" y2="388.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="391.33" x2="620.0" y2="391.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="394.17" x2="620.0" y2="394.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="397.0" x2="620.0" y2="397.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="399.83" x2="620.0" y2="399.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="402.67" x2="620.0" y2="402.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="405.50" x2="620.0" y2="405.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="408.33" x2="620.0" y2="408.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="411.17" x2="620.0" y2="411.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="414.0" x2="620.0" y2="414.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="416.83" x2="620.0" y2="416.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="419.67" x2="620.0" y2="419.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="422.50" x2="620.0" y2="422.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="425.33" x2="620.0" y2="425.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="428.17" x2="620.0" y2="428.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="431.0" x2="620.0" y2="431.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="433.83" x2="620.0" y2="433.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="436.67" x2="620.0" y2="436.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="439.50" x2="620.0" y2="439.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="442.33" x2="620.0" y2="442.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="445.17" x2="620.0" y2="445.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="448.0" x2="620.0" y2="448.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="450.83" x2="620.0" y2="450.83" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="453.67" x2="620.0" y2="453.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="456.50" x2="620.0" y2="456.50" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="459.33" x2="620.0" y2="459.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="462.17" x2="620.0" y2="462.17" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="40.0" x2="70.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="88.33" y1="40.0" x2="88.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="106.67" y1="40.0" x2="106.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="125.0" y1="40.0" x2="125.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="143.33" y1="40.0" x2="143.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="161.67" y1="40.0" x2="161.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="180.0" y1="40.0" x2="180.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="198.33" y1="40.0" x2="198.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="216.67" y1="40.0" x2="216.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="235.0" y1="40.0" x2="235.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="271.67" y1="40.0" x2="271.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="290.0" y1="40.0" x2="290.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="308.33" y1="40.0" x2="308.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="326.67" y1="40.0" x2="326.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="345.0" y1="40.0" x2="345.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="363.33" y1="40.0" x2="363.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="381.67" y1="40.0" x2="381.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="400.0" y1="40.0" x2="400.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="418.33" y1="40.0" x2="418.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="455.0" y1="40.0" x2="455.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="473.33" y1="40.0" x2="473.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="491.67" y1="40.0" x2="491.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="510.0" y1="40.0" x2="510.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="528.33" y1="40.0" x2="528.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="546.67" y1="40.0" x2="546.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="565.0" y1="40.0" x2="565.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="583.33" y1="40.0" x2="583.33" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="601.67" y1="40.0" x2="601.67" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="620.0" y1="40.0" x2="620.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="40.0" x2="620.0" y2="40.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="54.17" x2="620.0" y2="54.17" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="68.33" x2="620.0" y2="68.33" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="82.50" x2="620.0" y2="82.50" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="96.67" x2="620.0" y2="96.67" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="110.83" x2="620.0" y2="110.83" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="125.0" x2="620.0" y2="125.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="139.17" x2="620.0" y2="139.17" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="153.33" x2="620.0" y2="153.33" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="167.50" x2="620.0" y2="167.50" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="195.83" x2="620.0" y2="195.83" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="210.0" x2="620.0" y2="210.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="224.17" x2="620.0" y2="224.17" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="238.33" x2="620.0" y2="238.33" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="252.50" x2="620.0" y2="252.50" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="266.67" x2="620.0" y2="266.67" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="280.83" x2="620.0" y2="280.83" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="295.0" x2="620.0" y2="295.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="309.17" x2="620.0" y2="309.17" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="337.50" x2="620.0" y2="337.50" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="351.67" x2="620.0" y2="351.67" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="365.83" x2="620.0" y2="365.83" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="380.0" x2="620.0" y2="380.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="394.17" x2="620.0" y2="394.17" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="408.33" x2="620.0" y2="408.33" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="422.50" x2="620.0" y2="422.50" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="436.67" x2="620.0" y2="436.67" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="450.83" x2="620.0" y2="450.83" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="465.0" x2="620.0" y2="465.0" stroke="#E3D6A0" stroke-width="0.6"/>
<line x1="70.0" y1="40.0" x2="70.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="106.67" y1="40.0" x2="106.67" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="143.33" y1="40.0" x2="143.33" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="180.0" y1="40.0" x2="180.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="216.67" y1="40.0" x2="216.67" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="253.33" y1="40.0" x2="253.33" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="290.0" y1="40.0" x2="290.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="326.67" y1="40.0" x2="326.67" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="363.33" y1="40.0" x2="363.33" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="400.0" y1="40.0" x2="400.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="436.67" y1="40.0" x2="436.67" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="473.33" y1="40.0" x2="473.33" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="510.0" y1="40.0" x2="510.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="546.67" y1="40.0" x2="546.67" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="583.33" y1="40.0" x2="583.33" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="620.0" y1="40.0" x2="620.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="40.0" x2="620.0" y2="40.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="68.33" x2="620.0" y2="68.33" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="96.67" x2="620.0" y2="96.67" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="125.0" x2="620.0" y2="125.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="153.33" x2="620.0" y2="153.33" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="181.67" x2="620.0" y2="181.67" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="210.0" x2="620.0" y2="210.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="238.33" x2="620.0" y2="238.33" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="266.67" x2="620.0" y2="266.67" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="295.0" x2="620.0" y2="295.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="323.33" x2="620.0" y2="323.33" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="351.67" x2="620.0" y2="351.67" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="380.0" x2="620.0" y2="380.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="408.33" x2="620.0" y2="408.33" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="436.67" x2="620.0" y2="436.67" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<line x1="70.0" y1="465.0" x2="620.0" y2="465.0" stroke="#1F3A93" stroke-width="1.1" stroke-opacity="0.55"/>
<rect x="70" y="40" width="550" height="425" fill="none" stroke="#0B173A" stroke-width="2"/>
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif">1 / λ²  (μm⁻²)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Refractive index, n</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15×15 grid</b> — choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. Using Cauchy's relation with representative A, B constants for crown glass, calculate n at λ = 700 nm (red) and λ = 400 nm (violet).
2. Estimate the dispersive power ω using the calculated indices at red, yellow and violet wavelengths.

## Result

*Table: Refractive index at representative wavelengths (Cauchy's relation)*

| λ (nm) | n(λ) calculated | Colour |
|---|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |

## Maximum Permissible Error

From n = sin[(A+δm)/2] / sin(A/2), where A is the prism apex angle and δm the angle of minimum deviation. Both are read off the same spectrometer circular scale, so use its vernier least count for both ΔA and Δδm.

<div class="error-calc" data-exp="prism-dispersion"></div>

## Precautions

- Remember that the simulator exaggerates dispersive power for visibility; real crown glass has ω of only a few percent.
- Keep the apex angle fixed while studying the effect of dispersive power, and vice versa.

## Self-Check Quiz

??? question "1. Cauchy's relation n(λ) = A + B/λ² predicts that, for normal dispersion, refractive index:"
    - **A)** Increases with wavelength
    - **B)** Decreases with wavelength
    - **C)** Is independent of wavelength
    - **D)** Oscillates with wavelength

    **Answer: B** — Since n = A + B/λ², n decreases as λ increases (B, λ² both positive) — shorter wavelengths (violet) have higher n than longer wavelengths (red).


??? question "2. Which colour is deviated most by a prism?"
    - **A)** Red
    - **B)** Yellow
    - **C)** Violet
    - **D)** All colours equally

    **Answer: C** — Violet light has the highest refractive index in normal dispersion, so δ ≈ (n−1)A_apex is largest for violet.


??? question "3. The dispersive power ω = (n_v − n_r)/(n_y − 1) is best described as:"
    - **A)** The total deviation angle
    - **B)** A dimensionless measure of how strongly a material spreads colours, independent of the prism's apex angle
    - **C)** The apex angle of the prism
    - **D)** Only relevant to violet light

    **Answer: B** — ω characterises the material itself (via its indices at three reference wavelengths), separate from the prism's geometric apex angle.


??? question "4. A mirror does not produce a spectrum from white light because:"
    - **A)** Mirrors absorb all colours except white
    - **B)** Reflection angle depends on wavelength just like refraction
    - **C)** The law of reflection is the same for every wavelength — there is no dispersion in reflection
    - **D)** Mirrors only reflect violet light

    **Answer: C** — Reflection depends only on geometry (angle of incidence = angle of reflection) for every wavelength alike, unlike refraction where n(λ) varies.


## Viva-Voce Questions

1. Why does a prism, unlike a plane mirror, produce a spectrum from white light?
2. What is meant by 'normal' dispersion, and under what conditions does 'anomalous' dispersion occur?
3. Why does the angle-of-minimum-deviation method give a more reliable value of refractive index than an arbitrary angle of incidence?
4. Why is the refractive index of a prism material higher for violet light than for red light?
5. What is meant by the dispersive power of a prism, and how is it calculated?
6. How would the angle of deviation change if the prism material were replaced by one of higher refractive index?
7. Why must the incident beam be effectively monochromatic when measuring refractive index by the minimum-deviation method?
