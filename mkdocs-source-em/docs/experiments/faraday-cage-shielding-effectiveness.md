# Electrostatic & EM Shielding Effectiveness of a Faraday Cage

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="faraday-cage-shielding-effectiveness"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/faraday-cage-shielding-effectiveness.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; An external time-varying EM field is incident on a closed conducting enclosure; a field probe placed inside measures the strongly attenuated residual field, quantifying the enclosure's shielding effectiveness in dB.</div>
</div>

## Aim

To compute the shielding effectiveness of a conducting enclosure (Faraday cage) as a function of wall thickness, conductivity and frequency, via the skin-depth attenuation of the incident field as it penetrates the conducting wall.

## Theoretical Background

A Faraday cage — a closed or nearly closed conducting enclosure — shields its interior from external electric and electromagnetic fields. For a static or slowly varying electric field, free charges in the conductor simply rearrange themselves to cancel the field inside completely, regardless of wall thickness. For a time-varying electromagnetic field, the story is more subtle: the field does penetrate into the conducting wall, but its amplitude decays exponentially with depth according to the material's skin depth δ = √(2/(ωμσ)), which itself shrinks as frequency and conductivity increase. The resulting absorption loss, expressed in decibels, is approximately SE(dB) = 8.69·t/δ, where t is the wall thickness — so even a modest thickness of a good conductor provides enormous attenuation at radio frequencies, which is why thin metal foil or fine mesh is often sufficient for practical RF shielding (real enclosures are also limited by seams and apertures, not modelled here).

## Governing Formula

$$ SE\,(dB) = 8.69\,\dfrac{t}{\delta}, \qquad \delta = \sqrt{\dfrac{2}{\omega\mu\sigma}} $$

| Symbol | Meaning |
|---|---|
| SE | shielding effectiveness (dB), pure absorption loss |
| t | wall / mesh thickness (m) |
| δ | skin depth of the wall material at frequency f (m) |
| σ | wall conductivity (S/m) |
| ω | angular frequency, ω = 2πf |
| μ | permeability of the wall material (≈ μ₀ for non-magnetic metals) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Electrostatic & EM Shielding Effectiveness of a Faraday Cage** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Wall / mesh thickness | t | 0.05–5 mm | 1 mm |
| Wall conductivity | σ | 1–60 ×10⁶ S/m | 35 ×10⁶ S/m |
| Field frequency | f | 0.1–1000 MHz | 100 MHz |

## Procedure

1. Fix t and σ at their default values and vary f from 0.1 MHz to 1000 MHz, recording the skin depth δ and shielding effectiveness SE at each step.
2. Plot SE versus log f and note how rapidly shielding improves with increasing frequency for a fixed wall thickness.
3. Fix f and vary the wall thickness t, verifying SE ∝ t.
4. Fix f and t, and vary the conductivity σ (e.g. comparing copper-like and steel-like values), and observe the effect on δ and SE.
5. Discuss why this idealised absorption-loss model tends to over-predict real-world shielding effectiveness, and what additional loss mechanisms (seams, apertures) a real enclosure design must also consider.

## Observation Table

| S. No. | f (MHz) | t (mm) | σ (×10⁶ S/m) | δ (µm) | SE (dB) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Shielding effectiveness SE vs frequency f*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Shielding effectiveness SE vs frequency f</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">log f (MHz)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">SE (dB)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | SE at reference frequency f₀ | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Remember this model captures absorption loss only; real enclosures also lose effectiveness through seams, joints and apertures.
- Static electric shielding (zero interior field) holds regardless of thickness; the finite-δ model here applies specifically to time-varying fields.
- Vary only one of t, σ, f at a time while tabulating the others.
- Use consistent SI units when computing δ and SE from the raw control values.

## Maximum Permissible Error

$$ \dfrac{\Delta SE}{SE} = \dfrac{\Delta t}{t} + \tfrac{1}{2}\left(\dfrac{\Delta f}{f} + \dfrac{\Delta\sigma}{\sigma}\right) $$

SE = 8.69t/δ with δ ∝ 1/√(fσ), so f and σ each enter with a half-power (square-root) dependence, contributing half their fractional error.

<div class="error-calc" data-exp="faraday-cage-shielding-effectiveness"></div>

## Viva-Voce Questions

1. Explain why a Faraday cage shields static electric fields completely, regardless of wall thickness.
2. Define skin depth and explain why it decreases with increasing frequency.
3. Derive the approximate absorption-loss formula SE ≈ 8.69t/δ.
4. Why can a fine wire mesh be nearly as effective as a solid metal sheet at RF shielding?
5. What other loss mechanisms, besides absorption, contribute to a real enclosure's total shielding effectiveness?
