# Reflection, Refraction & Brewster's Angle for EM Waves

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
<text x="320" y="330" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">A virtual ray-optics bench with an EM wave incident on a</text>
<text x="320" y="348" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">dielectric interface of adjustable n₁, n₂, with adjustable</text>
<text x="320" y="366" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">incidence angle and selectable s- or p-polarization, showing</text>
<text x="320" y="384" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">computed reflectance/transmittance and the reflected ray's</text>
<text x="320" y="402" text-anchor="middle" font-size="12.5" fill="#274" font-family="Inter,Helvetica,sans-serif">polarization state.</text>
</svg>
<div class="apparatus-3d-caption"><b>Apparatus schematic</b> &middot; A virtual ray-optics bench with an EM wave incident on a dielectric interface of adjustable n₁, n₂, with adjustable incidence angle and selectable s- or p-polarization, showing computed reflectance/transmittance and the reflected ray's polarization state.</div>
</div>

## Aim

To study the reflection and transmission of an electromagnetic wave at a dielectric interface using the Fresnel equations, and to locate Brewster's angle at which p-polarized reflection vanishes.

## Theoretical Background

When an EM wave meets the planar interface between two dielectric media of refractive indices n₁ and n₂, part of it reflects and part refracts according to Snell's law n₁sinθᵢ = n₂sinθₜ. The fraction reflected depends on polarization and angle of incidence, given by the Fresnel equations. For light polarized with its E-field in the plane of incidence (p-polarization), the reflection coefficient passes through exactly zero at a special angle called Brewster's angle, θ_B = arctan(n₂/n₁), at which the reflected and refracted rays are perpendicular to each other. At this angle, only s-polarized light is reflected, so reflected light off a dielectric surface at Brewster's angle is completely (linearly) polarized — the principle exploited by polarizing sunglasses and by Brewster windows in laser cavities to eliminate reflection losses for one polarization.

## Governing Formula

$$ Snell's law: n₁ sinθᵢ = n₂ sinθₜ     |     Brewster's angle: θ_B = arctan(n₂/n₁) $$

| Symbol | Meaning |
|---|---|
| n₁, n₂ | refractive indices of the incident and transmitting media |
| θᵢ, θₜ | angles of incidence and refraction |
| θ_B | Brewster's angle, at which p-polarized reflectance is zero |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Reflection, Refraction & Brewster's Angle for EM Waves** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Incident medium index | n₁ | 1–2  | 1  |
| Transmitting medium index | n₂ | 1–2.5  | 1.5  |
| Angle of incidence | θᵢ | 0–89 ° | 30 ° |
| Polarization (0=s, 1=p) | pol | 0–1  | 1  |

## Procedure

1. For p-polarized light, sweep the angle of incidence from 0° to 89° and plot the reflectance R_p(θᵢ); locate the angle where it drops to zero.
2. Compare this angle with the calculated Brewster's angle θ_B = arctan(n₂/n₁) for the chosen n₁, n₂.
3. Repeat for s-polarized light and confirm R_s never reaches zero at any angle (no Brewster angle exists for s-polarization).
4. At θ = θ_B, verify numerically that the reflected and refracted rays are exactly perpendicular to each other.
5. Vary n₂ (keeping n₁ fixed) and verify θ_B shifts accordingly; tabulate θ_B versus n₂/n₁.
6. Send unpolarized light (an equal mix of s and p) at θ_B and confirm the reflected beam is purely s-polarized.

## Observation Table

| S. No. | n₁ | n₂ | θᵢ (°) | R_p (%) | R_s (%) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Reflectance vs Angle of Incidence &mdash; R_p dips to zero at Brewster's angle; R_s does not*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Reflectance vs Angle of Incidence</text>
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
<text x="345" y="500" text-anchor="middle" font-size="13" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">θᵢ (°) &#8594;</text>
<text x="20" y="252" text-anchor="middle" font-size="13" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 20 252)">Reflectance R &#8594;</text>
</svg>
</div>
<div class="apparatus-3d-caption" style="background:var(--lab-navy);"><b>15&times;15 grid</b> &mdash; choose your own scale per square; plot from your observation table. Expected trend: <i>R_p dips to zero at Brewster's angle; R_s does not</i></div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| n₂/n₁ | Brewster angle (measured) | Brewster angle (arctan n₂/n₁) | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Ensure the angle of incidence is measured from the normal to the interface, not from the surface itself.
- Distinguish carefully between s- and p-polarization when reading off reflectance curves — only p shows a Brewster null.
- Keep n₁ < n₂ or n₁ > n₂ clearly in mind, since total internal reflection (a separate phenomenon) only occurs going from denser to rarer medium beyond the critical angle.
- Use enough angular resolution near the expected Brewster angle to locate the null precisely.

## Maximum Permissible Error

$$ Δθ_B ≈ [1/(1+(n₂/n₁)²)]·(n₂/n₁)·(Δn₂/n₂ + Δn₁/n₁) $$

Obtained by differentiating θ_B = arctan(n₂/n₁) with respect to the ratio n₂/n₁.

<div class="error-calc" data-exp="reflection-refraction-brewster"></div>

## Viva-Voce Questions

1. Derive Brewster's angle condition from the Fresnel equation for p-polarized reflectance.
2. Why does no Brewster angle exist for s-polarized light?
3. Show that at Brewster's angle the reflected and refracted rays are perpendicular.
4. How are Brewster windows used inside a laser cavity, and why?
5. Distinguish Brewster's angle from the critical angle for total internal reflection.
6. How do polarizing sunglasses exploit Brewster-angle reflection from horizontal surfaces like water or roads?
