# Eddy-Current Damping — Lenz's Law Braking

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="eddy-current-damping"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/eddy-current-damping.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic above for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; A conducting plate moves with velocity v through a localised magnetic field region; the eddy currents induced in the plate oppose the field change (Lenz's law), producing a velocity-dependent retarding force.</div>
</div>

## Aim

To model the retarding force experienced by a conducting plate moving through a non-uniform magnetic field due to induced eddy currents, and study its dependence on conductivity, plate thickness, speed and field strength.

## Theoretical Background

When a solid conductor moves through a region of non-uniform magnetic field (or experiences a changing flux), Faraday's law induces circulating eddy currents within the bulk of the material, not just in a single wire loop. By Lenz's law, these eddy currents flow in whatever direction opposes the change that created them, which means they exert a retarding (braking) force on the moving conductor — converting its kinetic energy into resistive (I²R) heating within the material itself. This eddy-current braking effect grows with the conductor's electrical conductivity, its speed through the field, and the square of the field strength, and is exploited in applications ranging from magnetic braking systems in trains and roller coasters to the damping mechanisms of sensitive analog galvanometers and electricity meters.

## Governing Formula

$$ F_{eddy} \propto \sigma\, t\, B^2\, v\, w^2 $$

| Symbol | Meaning |
|---|---|
| F_eddy | eddy-current retarding force (N) |
| σ | electrical conductivity of the plate (S/m) |
| t | plate thickness (m) |
| B | magnetic flux density in the field region (T) |
| v | plate velocity through the field (m/s) |
| w | characteristic width of the induced current loops (m) |

## Interactive Controls

Launch the [simulator](../../../labs/advanced-electricity-magnetism-lab.html){target=_blank} and use the following controls on the **Eddy-Current Damping — Lenz's Law Braking** panel:

| Control | Symbol | Range | Default |
|---|---|---|---|
| Magnetic flux density | B | 10–500 mT | 200 mT |
| Plate velocity | v | 0.1–10 m/s | 2 m/s |
| Plate conductivity | σ | 1–60 ×10⁶ S/m | 35 ×10⁶ S/m |
| Plate thickness | t | 0.5–10 mm | 3 mm |

## Procedure

1. Fix B, σ, t at their default values and vary v from 0.1 to 10 m/s, recording the retarding force F.
2. Plot F versus v and verify a straight line through the origin, confirming F ∝ v at fixed field and material.
3. Fix v and vary B, and verify that F ∝ B² by plotting F versus B².
4. Fix B and v and vary the plate conductivity σ (e.g. comparing an aluminium-like and a copper-like value), and verify F ∝ σ.
5. Vary the plate thickness t and verify F ∝ t; discuss why a thicker plate experiences greater eddy-current braking.

## Observation Table

| S. No. | v (m/s) | B (mT) | σ (×10⁶ S/m) | t (mm) | F (mN) |
|---|---|---|---|---|---||
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Graph

*Retarding force F vs velocity v*

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
<text x="320.0" y="22" text-anchor="middle" font-size="17" font-weight="700" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">Retarding force F vs velocity v</text>
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
<text x="335.0" y="500" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif">v (m/s)</text>
<text x="18" y="252.5" text-anchor="middle" font-size="14" fill="#0B173A" font-family="Inter,Helvetica,sans-serif" transform="rotate(-90 18 252.5)">F (mN)</text>
</svg>
</div>
</div>

## Calculations

Use the governing formula above with your tabulated observations to compute the required result for each row. Show at least one complete sample calculation with units.

## Result

| Quantity | Slope of F vs v | Expected value | % deviation |
|---|---|---|---||
|  |  |  |  |

## Precautions

- Keep the field region localised (non-uniform) — a perfectly uniform infinite field produces no net eddy-current braking on a plate moving through it.
- Vary only one of B, v, σ, t at a time while tabulating the others.
- Note that F ∝ B², so small errors in B are doubled in their effect on the computed force.
- Distinguish eddy-current braking (a bulk, continuous-medium effect) from the induced EMF in a single discrete loop (Faraday's law experiment).

## Maximum Permissible Error

$$ \dfrac{\Delta F}{F} = \dfrac{\Delta\sigma}{\sigma} + \dfrac{\Delta t}{t} + 2\dfrac{\Delta B}{B} + \dfrac{\Delta v}{v} $$

F ∝ σtB²v has B squared, so its fractional error contributes twice to the total.

<div class="error-calc" data-exp="eddy-current-damping"></div>

## Viva-Voce Questions

1. Explain, using Lenz's law, why eddy currents always oppose the motion that creates them.
2. Why does eddy-current braking require a non-uniform (spatially varying) field rather than a uniform one?
3. Where does the kinetic energy lost by the moving conductor ultimately go?
4. Name two practical applications of eddy-current damping.
5. Why are laminated cores (thin insulated sheets) used in transformers to reduce eddy-current losses?
