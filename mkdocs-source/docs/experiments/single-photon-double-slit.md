# 10. Single-Photon Double-Slit Build-up

!!! abstract "Module"
    Particle Nature of Light · Experiment 3


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-singlephoton){target=_blank}**

## Aim

To observe the statistical build-up of an interference pattern from individually detected photons sent through a double slit one at a time, demonstrating wave–particle duality.

## Theoretical Background

If photons are sent through a double slit one at a time — so rarely that at most one photon is ever in transit — each photon is still detected as a single, localized point on the screen, exactly as a classical particle would be. There is no way to predict in advance exactly where any individual photon will land.

However, after a large number of such individual detection events accumulate, the resulting pattern of dots is not uniform: it reproduces the same fringe pattern (bright and dark bands) predicted by classical wave interference, with the probability of a photon landing at a given point proportional to the classical intensity, I ∝ cos²(...), of the two-slit pattern at that point.

This experiment shows that no single photon 'knows' about the emerging pattern, nor does it travel through only one slit in the classical sense — the interference pattern is a statistical property that emerges only over many independent, individually-particle-like detection events, encapsulating the essential mystery of wave–particle duality.

## Governing Formulas

**Probability density (two-slit):**

$$
P(y) \propto \cos^2\!\left(\dfrac{\pi d y}{\lambda D}\right)
$$

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="single-photon-double-slit"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/single-photon-double-slit.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic below for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; Attenuated source &rarr; double slit &rarr; photon-counting screen</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Photon arrival rate | — | 1 – 60 | photons/sec |

## Procedure

1. Set a low photon arrival rate and start the simulation; observe individual dots appearing at random-looking positions on the screen.
2. Let the simulation run and record the number of detected photons at regular intervals (e.g. every 100, 500, 2000 counts).
3. At each recorded interval, note (qualitatively or by pixel count binning) whether a fringe pattern is beginning to emerge from the scatter of dots.
4. Repeat at a higher arrival rate and confirm that the same final pattern emerges, only more quickly in wall-clock time.

## Observation Table

*Table: Emergence of the interference pattern with increasing photon count*

| S. No. | Total photons detected | Pattern visibility (none / faint / clear fringes) |
|---|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |

## Graph

Plot **Fringe visibility / contrast (qualitative or measured)** (y-axis) against **Number of photons detected (log scale)** (x-axis).

Expected trend: visibility rising from near-zero (few photons) toward the classical interference contrast (many photons).

*Build-up curve: fringe contrast vs cumulative photon count*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Detected Counts vs Position (build-up)</text>
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
<text x="345.0" y="506" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif">Screen position, y (a.u.)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#142B66" font-weight="600" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">Photon counts, N</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15×15 grid</b> — choose your own scale per square; plot from your observation table</div>
</div>

## Calculation

1. If a horizontal intensity histogram is exported at each interval, compute the visibility V = (Imax − Imin)/(Imax + Imin) at each stage.
2. Plot V against the cumulative photon count and note the count at which V approaches its asymptotic (classical) value.

## Result

*Table: Fringe visibility versus accumulated photon count*

| Photon count | Estimated visibility V |
|---|---|
| 1 |  |
| 2 |  |
| 3 |  |

## Maximum Permissible Error

This experiment is a qualitative demonstration, not an instrumental measurement — its natural 'error' is the statistical counting uncertainty of accumulating discrete photon detection events, which shrinks as more photons are collected.

<div class="error-calc" data-exp="single-photon-double-slit"></div>

## Precautions

- Do not judge the pattern from too few detections — early dots always look random regardless of the eventual pattern.
- Keep the arrival rate low enough (conceptually) that at most one photon is 'in flight' at a time, consistent with the single-photon interpretation.

## Self-Check Quiz

??? question "1. When a single photon is sent through the double slit, where does it land on the screen?"
    - **A)** Always exactly at the centre
    - **B)** Spread out continuously like a wave, never at a single point
    - **C)** At one single, localized point — exactly like a classical particle
    - **D)** It doesn't land anywhere unless many photons are sent together

    **Answer: C** — Every individual detection event is a single localized spot — the particle-like behaviour is seen event by event.


??? question "2. After thousands of individual photons accumulate one at a time, the resulting pattern of dots:"
    - **A)** Is completely random with no structure
    - **B)** Reproduces the classical two-slit interference fringe pattern
    - **C)** Shows only a single-slit pattern
    - **D)** Is uniform across the whole screen

    **Answer: B** — This is the heart of wave–particle duality: individually particle-like detections build up a wave-like interference pattern over many trials.


??? question "3. The probability of a photon landing at position y is proportional to:"
    - **A)** y itself
    - **B)** cos²(πdy/λD), the same intensity distribution predicted by classical wave interference
    - **C)** A constant, independent of y
    - **D)** 1/y²

    **Answer: B** — P(y) ∝ cos²(πdy/λD) — the quantum probability density exactly matches the classical intensity pattern.


??? question "4. Why is it essential that photons are sent 'so rarely that at most one is ever in transit'?"
    - **A)** To save laser power
    - **B)** To rule out the possibility that photons are interfering with each other, proving each photon somehow 'interferes with itself'
    - **C)** It isn't essential — the result would be the same either way
    - **D)** To make the experiment run faster

    **Answer: B** — With only one photon in the apparatus at a time, no classical interaction between photons is possible, showing the interference pattern is a single-photon phenomenon.


## Viva-Voce Questions

1. Does an individual photon pass through one slit or both? What does this experiment tell us about that question?
2. How does this experiment settle the wave-versus-particle debate about the nature of light?
3. How can an interference pattern build up even when photons are sent through the apparatus one at a time?
4. What happens to the interference pattern if a detector is placed at one slit to determine which slit each photon passed through?
5. What does this experiment demonstrate about the wave–particle duality of light?
6. Why can we not predict exactly where a single photon will land on the screen, only its probability distribution?
7. How does the accumulated pattern from many single photons compare with the classical double-slit fringe pattern?
