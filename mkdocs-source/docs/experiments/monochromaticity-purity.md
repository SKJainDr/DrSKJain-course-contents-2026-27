# 13. Monochromaticity & Spectral Purity

!!! abstract "Module"
    Laser Light Concepts


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-monochromaticity){target=_blank}**

## Aim

To compare the spectral purity of different light sources by measuring the ratio Δλ/λ of linewidth to central wavelength.

## Theoretical Background

Monochromaticity describes how closely a source approaches emitting a single, pure wavelength. In practice, every real source emits over some finite spectral width Δλ centred on a nominal wavelength λ; the quantity Δλ/λ is called the spectral purity (a smaller value indicates a purer, more nearly monochromatic source).

A single-mode stabilized laser can achieve Δλ/λ of order 10⁻⁶ or better, a multimode gas laser typically 10⁻⁴, a light-emitting diode around 3×10⁻², and a white-light (thermal) source close to unity, since it emits across essentially the whole visible band.

High spectral purity is essential wherever precise wavelength-dependent effects matter: spectroscopic resolution, coherence length (and hence holography), and wavelength-division multiplexing in fibre-optic communications, where adjacent channels must not spectrally overlap.

## Governing Formulas

**Spectral purity:**

$$
\text{Purity} = \dfrac{\Delta\lambda}{\lambda}
$$

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="monochromaticity-purity"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/monochromaticity-purity.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic below for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; Source &rarr; grating/prism &rarr; spectrum analyzer</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Central wavelength | λ | 400 – 700 | nm |
| Source type (linewidth Δλ) | Δλ | 0.001 – 250 | nm |

## Procedure

1. For each of the four source types (single-mode laser, multimode gas laser, LED, white-light source), set the central wavelength to a common value and record Δλ and the computed purity Δλ/λ.
2. Repeat for at least two different central wavelengths and confirm that the purity ratio for a given source type scales as expected.
3. Tabulate and rank the four sources by spectral purity.

## Observation Table

*Table: Spectral purity of representative source types at a fixed central wavelength*

| S. No. | Source type | λ (nm) | Δλ (nm) | Purity Δλ/λ |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

## Graph

Plot **Spectral purity Δλ/λ (log scale)** (y-axis) against **Source type (ranked)** (x-axis).

Expected trend: values spanning several orders of magnitude, laser < LED < white light.

*Comparative bar/log chart of spectral purity across source types*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Spectral Purity Comparison</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif">Source type (categorical)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Purity, Δλ/λ (log scale suggested)</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15×15 grid</b> — choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. Compute Δλ/λ for every tabulated row and rank the sources from most to least monochromatic.
2. Relate the purity value of the multimode gas laser to the coherence length computed in the Coherence experiment, and check the two results for consistency (smaller Δλ/λ ⇔ longer Lc, at fixed λ).

## Result

*Table: Spectral purity ranking of the four sources*

| Source | Δλ/λ | Relative ranking |
|---|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |

## Maximum Permissible Error

purity = W/λ, where W is the measured spectral linewidth. Sum the fractional error in the linewidth measurement and in the central-wavelength measurement.

<div class="error-calc" data-exp="monochromaticity-purity"></div>

## Precautions

- Use a logarithmic scale when comparing purity values, since they differ by orders of magnitude across source types.
- Keep the central wavelength fixed while comparing source types so that the comparison isolates Δλ alone.

## Self-Check Quiz

??? question "1. A smaller spectral purity value Δλ/λ indicates:"
    - **A)** A less pure, broader-spectrum source
    - **B)** A purer, more nearly monochromatic source
    - **C)** A brighter source
    - **D)** Nothing about spectral quality

    **Answer: B** — Δλ/λ directly measures how 'spread out' the emission is relative to its central wavelength — smaller is purer.


??? question "2. Roughly how does a single-mode stabilized laser's spectral purity compare to a white-light thermal source?"
    - **A)** Laser ≈ 10⁻⁶, thermal source ≈ 1 — many orders of magnitude purer
    - **B)** They are approximately equal
    - **C)** The thermal source is purer
    - **D)** Purity cannot be compared between different source types

    **Answer: A** — A stabilized single-mode laser (~10⁻⁶) is roughly a million times purer than a white-light thermal source (~1), which emits across the whole visible band.


??? question "3. Which light source listed would you expect to have the worst (largest) spectral purity?"
    - **A)** Single-mode stabilized laser
    - **B)** Multimode gas laser
    - **C)** Light-emitting diode (LED)
    - **D)** White-light thermal source

    **Answer: D** — A thermal source emits across essentially the whole visible band, giving Δλ/λ close to unity — the least monochromatic of the four.


??? question "4. Spectral purity Δλ/λ and coherence length Lc are related because both ultimately depend on:"
    - **A)** The source's total output power
    - **B)** The source's spectral linewidth
    - **C)** The size of the light source
    - **D)** The colour of the light

    **Answer: B** — A narrower linewidth simultaneously gives smaller Δλ/λ (higher purity) and a longer coherence length — the two concepts are two views of the same underlying property.


## Viva-Voce Questions

1. Why is high spectral purity essential for wavelength-division multiplexing in optical fibre communication?
2. How are spectral purity and coherence length related to one another physically?
3. What does a smaller value of Δλ/λ indicate about the spectral purity of a source?
4. Why is a single-mode laser far more monochromatic than a filtered lamp of the same nominal wavelength?
5. How is the spectral linewidth Δλ of a source related to its coherence length?
6. Why is high spectral purity important for applications such as spectroscopy or interferometry?
7. What instrument would you use to directly measure the linewidth of a laser source?
