# 14. Making a Hologram

!!! abstract "Module"
    Laser Light Concepts


!!! tip "Try it live"
    Explore this on the interactive simulator with real-time sliders and graphs: **[🔬 Launch in Simulator](../../../labs/advanced-laser-optics-lab.html#panel-holography){target=_blank}**

## Aim

To understand the recording and reconstruction stages of a hologram and to appreciate the role of coherent laser light in capturing both amplitude and phase information.

## Theoretical Background

A conventional photograph records only the intensity (amplitude squared) of light reflected from a scene, discarding all information about the phase of the light waves — and hence all three-dimensional depth information. A hologram, in contrast, records the interference pattern formed between light scattered from the object (the object beam) and a mutually coherent reference beam derived from the same laser.

Because the two beams are coherent, their interference pattern — a microscopically fine fringe structure — encodes both the amplitude and the relative phase of the object wave at every point on the recording medium (a high-resolution photographic plate or equivalent). This recorded fringe pattern is the hologram.

To reconstruct the image, the developed hologram is illuminated with a beam identical to the original reference beam. The fine interference fringes act as a complex diffraction grating that reconstructs the original object wavefront, including its phase — producing a genuinely three-dimensional virtual image that appears to shift in perspective as the viewing angle changes, exactly as the original object would.

## Governing Formulas

**Recorded intensity at the plate:**

$$
I = |E_{\text{obj}} + E_{\text{ref}}|^2 = |E_{\text{obj}}|^2 + |E_{\text{ref}}|^2 + 2\,\text{Re}\!\left(E_{\text{obj}}E_{\text{ref}}^{*}\right)
$$

<div class="apparatus-3d-wrap" markdown="1">
<div class="apparatus-3d" data-setup="holography"></div>

<div class="apparatus-photo">
<img src="../../assets/apparatus/holography.png" alt="Apparatus layout diagram for this experiment">
<div class="cap">Labelled apparatus layout — original illustration prepared for this guide (not a photograph). See the drag-to-rotate 3-D schematic below for a spatial view of the same setup.</div>
</div>

<div class="apparatus-3d-caption"><b>3-D apparatus schematic</b> &middot; drag to rotate, scroll to zoom &middot; Laser &rarr; beamsplitter &rarr; object &amp; reference beams &rarr; plate</div>
</div>

## Simulator Controls

| Control | Symbol | Range | Unit |
|---|---|---|---|
| Recording/reconstruction stage | — | 4 stages | — |
| Viewing angle (reconstruction only) | — | −30 – +30 | ° |

## Procedure

1. Step through stage 1 (object and reference beams meeting at the plate) and note how the two beams overlap.
2. Step through stage 2 (interference pattern recorded on the plate) and note the fine fringe structure that encodes the object information.
3. Step through stage 3 (illuminating the developed hologram with the reference beam alone) and observe how the fringe pattern begins to diffract the illuminating beam.
4. Step through stage 4 (reconstructed wavefront) and vary the viewing angle to observe the parallax/perspective shift characteristic of a genuine 3-D image.

## Observation Table

*Table: The four stages of holographic recording and reconstruction*

| Stage | Description observed | Key physical process at this stage |
|---|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |

## Graph

Plot **Apparent perspective shift of reconstructed image** (y-axis) against **Viewing angle (°)** (x-axis).

Expected trend: a smooth, continuous shift in apparent viewpoint as angle changes, confirming genuine 3-D reconstruction.

*Qualitative record of perspective change with viewing angle during reconstruction*

<div class="graph-box">📈 Graph paper / plot area — attach printed or digital graph here</div>

## Calculation

1. Identify, from the recorded intensity expression, which cross term (2·Re(E_obj E_ref*)) is responsible for carrying the phase information of the object beam.
2. Note qualitatively how the fringe spacing on the plate depends on the angle between the object and reference beams (finer fringes for larger angles).

## Result

*Table: Summary of the holographic recording/reconstruction sequence*

| Stage | Physical process |
|---|---|
| 1 |  |
| 2 |  |
| 3 |  |

## Maximum Permissible Error

Holography as presented here is a qualitative recording/reconstruction demonstration, not an instrumental measurement — there is no single numeric result with a propagated maximum permissible error. Use the space below to sketch/note the four stages instead.

## Precautions

- Distinguish clearly between the recording stages (1–2, needs both beams) and the reconstruction stages (3–4, needs only the reference beam and the developed plate).
- Note that only coherent, monochromatic light (a laser) can produce a usable hologram — this links directly to the Coherence and Monochromaticity experiments.

## Self-Check Quiz

??? question "1. Unlike an ordinary photograph, a hologram records:"
    - **A)** Only the intensity of the object beam
    - **B)** Both the amplitude and the relative phase of the object wave
    - **C)** Only colour information
    - **D)** Nothing about the object beam at all

    **Answer: B** — The interference between object and reference beams encodes phase as well as amplitude, which is what allows full 3-D reconstruction.


??? question "2. Why must the object beam and reference beam come from the same laser?"
    - **A)** To save power
    - **B)** So they are mutually coherent and can form a stable interference pattern
    - **C)** It doesn't matter, any two lasers work
    - **D)** To make the object appear brighter

    **Answer: B** — Only mutually coherent beams (same source, fixed phase relationship) produce a stable fringe pattern that can be recorded as a hologram.


??? question "3. The recorded intensity at the photographic plate is given by I = |E_obj + E_ref|². The cross term 2Re(E_obj·E_ref*) is important because it:"
    - **A)** Is always zero and can be ignored
    - **B)** Is the term that actually encodes the phase information of the object wave
    - **C)** Only affects the colour of the hologram
    - **D)** Represents pure noise

    **Answer: B** — The cross term is where the interference — and therefore the phase information about the object — actually lives; the other two terms are just the individual beam intensities.


??? question "4. What fundamentally makes holography possible that an ordinary camera lacks?"
    - **A)** A bigger lens
    - **B)** A highly coherent light source (laser) needed to form a stable interference pattern
    - **C)** A faster shutter speed
    - **D)** A colour film

    **Answer: B** — Ordinary cameras use incoherent light and record intensity only; holography specifically requires a coherent source to capture and later reconstruct phase via interference.


## Viva-Voce Questions

1. Why must the reference and object beams originate from the same laser source?
2. What distinguishes a hologram from an ordinary photograph in terms of the information each one records?
3. Why must both the object beam and the reference beam originate from the same laser source?
4. What information is recorded on a holographic plate that is not recorded on an ordinary photograph?
5. Why must a holographic plate record both amplitude and phase information for a full 3-D reconstruction?
6. What happens if the reconstruction beam does not match the original reference beam in wavelength or direction?
7. Explain the difference between the real and virtual images formed during hologram reconstruction.
