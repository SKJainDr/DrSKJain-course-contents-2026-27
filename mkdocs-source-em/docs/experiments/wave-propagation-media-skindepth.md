# Propagation of EM Waves in Dielectric & Conducting Media (Skin Depth)

<div class="apparatus-3d-wrap" markdown="1">
<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#eef3f7;border-radius:8px;">
<rect x="30" y="60" width="150" height="90" rx="10" fill="#0e2a3d"/>
<text x="105" y="100" text-anchor="middle" font-size="14" fill="#f2d9a6" font-family="Inter,Helvetica,sans-serif" font-weight="700">SOURCE /</text>
<text x="105" y="118" text-anchor="middle" font-size="14" fill="#f2d9a6" font-family="Inter,Helvetica,sans-serif" font-weight="700">CONTROL</text>
<rect x="245" y="45" width="150" height="120" rx="10" fill="#c8932a"/>
<text x="320" y="95" text-anchor="middle" font-size="13.5" fill="#0e2a3d" font-family="Inter,Helvetica,sans-serif" font-weight="700">APPARATUS</text>
<text x="320" y="115" text-anchor="middle" font-size="11.5" fill="#0e2a3d" font-family="Inter,Helvetica,sans-serif">(virtual setup)</text>
<rect x="460" y="60" width="150" height="90" rx="10" fill="#a8452f"/>
<text x="535" y="100" text-anchor="middle" font-size="14" fill="#fdf6e7" font-family="Inter,Helvetica,sans-serif" font-weight="700">PROBE /</text>
<text x="535" y="118" text-anchor="middle" font-size="14" fill="#fdf6e7" font-family="Inter,Helvetica,sans-serif" font-weight="700">DETECTOR</text>
<line x1="180" y1="105" x2="245" y2="105" stroke="#0B173A" stroke-width="3" marker-end="url(#arrow)"/>
<line x1="395" y1="105" x2="460" y2="105" stroke="#0B173A" stroke-width="3" marker-end="url(#arrow)"/>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#0B173A"/></marker></defs>
<line x1="70" y1="230" x2="570" y2="230" stroke="#0B173A" stroke-width="1" stroke-dasharray="4,3"/>
<text x="320" y="330" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">A virtual EM wave incident on a slab of adjustable material</text>
<text x="320" y="348" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">(dielectric or conductor, with selectable εr, μr, σ), animated</text>
<text x="320" y="366" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">to show the wave slowing/attenuating inside, with a live plot of</text>
<text x="320" y="384" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">amplitude versus penetration depth.</text>
</svg>
<div class="apparatus-3d-caption"><b>Apparatus schematic</b> &middot; A virtual EM wave incident on a slab of adjustable material (dielectric or conductor, with selectable εr, μr, σ), animated to show the wave slowing/attenuating inside, with a live plot of amplitude versus penetration depth.</div>
</div>

## Aim

To study how the speed, wavelength, and attenuation of an electromagnetic wave change on entering a dielectric or a conducting medium, and to determine the skin depth for a conductor as a function of frequency and conductivity.

## Theoretical Background

In a lossless dielectric of relative permittivity εr and relative permeability μr, an EM wave travels at reduced speed v = c/n where the refractive index n = √(μrεr), with no attenuation. In a conducting medium of conductivity σ, however, the wave is exponentially attenuated as it propagates because oscillating currents driven by E dissipate energy as heat (Ohmic loss). Its amplitude falls as e^{−z/δ}, where the skin depth δ = √(2/ωμσ) is the distance over which the amplitude drops to 1/e of its surface value. Skin depth decreases with increasing frequency and conductivity, which is why high-frequency currents in a good conductor are confined to a thin surface layer (the 'skin effect'), and why good conductors like metals are excellent reflectors and poor transmitters of high-frequency EM waves.

## Governing Formula

$$ Dielectric: v = c/√(μrεr)     |     Conductor: δ = √(2/ωμσ) $$

| Symbol | Meaning |
|---|---|
| v | wave speed inside the dielectric (m/s) |
| n = √(μrεr) | refractive index |
| δ | skin depth in a conductor (m) |
| ω | angular frequency (rad/s) |
| σ | conductivity (S/m) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Propagation of EM Waves in Dielectric & Conducting Media (Skin Depth)** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Relative permittivity (dielectric mode) | εr | 1–10  | 4  |
| Wave frequency | f | 0.1–1000 MHz | 100 MHz |
| Conductivity (conductor mode) | σ | 0.1–60 MS/m | 6 MS/m |
| Medium (0=dielectric, 1=conductor) | mode | 0–1  | 0  |

## Procedure

1. In dielectric mode, vary εr and verify the wave speed inside falls as v = c/√εr (with μr = 1).
2. Verify the wavelength inside the dielectric shrinks by the same factor √εr while the frequency stays fixed (set by the source).
3. Switch to conductor mode and vary the frequency; plot δ vs f and verify δ ∝ 1/√f.
4. At fixed frequency, vary the conductivity σ and verify δ ∝ 1/√σ.
5. Compute the skin depth for copper (σ ≈ 6×10⁷ S/m) at 50 Hz and at 1 GHz, and comment on the enormous difference.
6. Estimate, using the skin depth, roughly what thickness of a conducting enclosure is needed to shield against a given frequency (link to the shielding workshop).

## Observation Table

| S. No. | Mode | Frequency f (MHz) | εr or σ | Wave speed / Skin depth | Wavelength (dielectric mode) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Skin Depth vs Frequency (log-log) &mdash; slope ≈ -1/2*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Skin Depth vs Frequency (log-log)</text>
<line x1="77.33" y1="40.0" x2="77.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="84.67" y1="40.0" x2="84.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="92.0" y1="40.0" x2="92.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="99.33" y1="40.0" x2="99.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="114.0" y1="40.0" x2="114.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="121.33" y1="40.0" x2="121.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="128.67" y1="40.0" x2="128.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="136.0" y1="40.0" x2="136.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="150.67" y1="40.0" x2="150.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="158.0" y1="40.0" x2="158.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="165.33" y1="40.0" x2="165.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="172.67" y1="40.0" x2="172.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="187.33" y1="40.0" x2="187.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="194.67" y1="40.0" x2="194.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="202.0" y1="40.0" x2="202.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="209.33" y1="40.0" x2="209.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="224.0" y1="40.0" x2="224.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="231.33" y1="40.0" x2="231.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="238.67" y1="40.0" x2="238.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="246.0" y1="40.0" x2="246.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="260.67" y1="40.0" x2="260.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="268.0" y1="40.0" x2="268.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="275.33" y1="40.0" x2="275.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="282.67" y1="40.0" x2="282.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="297.33" y1="40.0" x2="297.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="304.67" y1="40.0" x2="304.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="312.0" y1="40.0" x2="312.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="319.33" y1="40.0" x2="319.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="334.0" y1="40.0" x2="334.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="341.33" y1="40.0" x2="341.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="348.67" y1="40.0" x2="348.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="356.0" y1="40.0" x2="356.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="370.67" y1="40.0" x2="370.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="378.0" y1="40.0" x2="378.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="385.33" y1="40.0" x2="385.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="392.67" y1="40.0" x2="392.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="407.33" y1="40.0" x2="407.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="414.67" y1="40.0" x2="414.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="422.0" y1="40.0" x2="422.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="429.33" y1="40.0" x2="429.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="444.0" y1="40.0" x2="444.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="451.33" y1="40.0" x2="451.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="458.67" y1="40.0" x2="458.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="466.0" y1="40.0" x2="466.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="480.67" y1="40.0" x2="480.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="488.0" y1="40.0" x2="488.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="495.33" y1="40.0" x2="495.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="502.67" y1="40.0" x2="502.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="517.33" y1="40.0" x2="517.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="524.67" y1="40.0" x2="524.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="532.0" y1="40.0" x2="532.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="539.33" y1="40.0" x2="539.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="554.0" y1="40.0" x2="554.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="561.33" y1="40.0" x2="561.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="568.67" y1="40.0" x2="568.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="576.0" y1="40.0" x2="576.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="590.67" y1="40.0" x2="590.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="598.0" y1="40.0" x2="598.0" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="605.33" y1="40.0" x2="605.33" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="612.67" y1="40.0" x2="612.67" y2="465.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="45.67" x2="620.0" y2="45.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="51.33" x2="620.0" y2="51.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="57.0" x2="620.0" y2="57.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="62.67" x2="620.0" y2="62.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="74.0" x2="620.0" y2="74.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="79.67" x2="620.0" y2="79.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="85.33" x2="620.0" y2="85.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="91.0" x2="620.0" y2="91.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="102.33" x2="620.0" y2="102.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="108.0" x2="620.0" y2="108.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="113.67" x2="620.0" y2="113.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="119.33" x2="620.0" y2="119.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="130.67" x2="620.0" y2="130.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="136.33" x2="620.0" y2="136.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="142.0" x2="620.0" y2="142.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="147.67" x2="620.0" y2="147.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="159.0" x2="620.0" y2="159.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="164.67" x2="620.0" y2="164.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="170.33" x2="620.0" y2="170.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="176.0" x2="620.0" y2="176.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="187.33" x2="620.0" y2="187.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="193.0" x2="620.0" y2="193.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="198.67" x2="620.0" y2="198.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="204.33" x2="620.0" y2="204.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="215.67" x2="620.0" y2="215.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="221.33" x2="620.0" y2="221.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="227.0" x2="620.0" y2="227.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="232.67" x2="620.0" y2="232.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="244.0" x2="620.0" y2="244.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="249.67" x2="620.0" y2="249.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="255.33" x2="620.0" y2="255.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="261.0" x2="620.0" y2="261.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="272.33" x2="620.0" y2="272.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="278.0" x2="620.0" y2="278.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="283.67" x2="620.0" y2="283.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="289.33" x2="620.0" y2="289.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="300.67" x2="620.0" y2="300.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="306.33" x2="620.0" y2="306.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="312.0" x2="620.0" y2="312.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="317.67" x2="620.0" y2="317.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="329.0" x2="620.0" y2="329.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="334.67" x2="620.0" y2="334.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="340.33" x2="620.0" y2="340.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="346.0" x2="620.0" y2="346.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="357.33" x2="620.0" y2="357.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="363.0" x2="620.0" y2="363.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="368.67" x2="620.0" y2="368.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="374.33" x2="620.0" y2="374.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="385.67" x2="620.0" y2="385.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="391.33" x2="620.0" y2="391.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="397.0" x2="620.0" y2="397.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="402.67" x2="620.0" y2="402.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="414.0" x2="620.0" y2="414.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="419.67" x2="620.0" y2="419.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="425.33" x2="620.0" y2="425.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="431.0" x2="620.0" y2="431.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="442.33" x2="620.0" y2="442.33" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="448.0" x2="620.0" y2="448.0" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="453.67" x2="620.0" y2="453.67" stroke="#EDE3C2" stroke-width="0.35"/>
<line x1="70.0" y1="459.33" x2="620.0" y2="459.33" stroke="#EDE3C2" stroke-width="0.35"/>
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
<text x="345" y="500" text-anchor="middle" font-size="13" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log₁₀ f &#8594;</text>
<text x="20" y="252" text-anchor="middle" font-size="13" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 20 252)">log₁₀ δ &#8594;</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table. Expected trend: <i>slope ≈ -1/2</i></div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Case | Measured quantity | Theoretical value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Keep μr = 1 (non-magnetic medium) unless specifically studying magnetic conductors, to isolate the effect of εr or σ alone.
- Remember skin depth applies strictly to good conductors (σ/ωε ≫ 1); the formula is not valid for weakly-conducting or dielectric media.
- Use consistent SI units (rad/s for ω, S/m for σ) when checking the numeric value of δ.
- Note the refractive index model here assumes a non-dispersive dielectric; real materials' εr can vary with frequency.

## Maximum Permissible Error

$$ Δδ/δ = ½(Δf/f + Δσ/σ) $$

δ ∝ 1/√(fσ), so the fractional errors in f and σ are each halved before summing.

<div class="error-calc" data-exp="wave-propagation-media-skindepth"></div>

## Viva-Voce Questions

1. Derive the refractive index n = √(μrεr) from the wave equation in a dielectric medium.
2. Why does an EM wave attenuate exponentially inside a conductor but not inside an ideal (lossless) dielectric?
3. Derive the expression for skin depth starting from the wave equation with a conduction-current term.
4. Why are radio antennas and high-frequency circuit traces often silver-plated even though bulk silver is only marginally more conductive than copper?
5. How does skin depth explain why AC power transmission cables sometimes use stranded or hollow conductors?
6. Relate the concept of skin depth to electromagnetic shielding effectiveness of an enclosure.
