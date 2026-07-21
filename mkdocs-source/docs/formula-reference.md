# Formula Quick Reference

A single-page cheat-sheet of every governing equation used across the 18 experiments, grouped the same way as the main [Contents](index.md). Use this page while doing calculations so you don't have to open each experiment page individually — click the linked experiment name if you need the full derivation or context.

## Wave Optics

**[1. Young's Double-Slit](experiments/youngs-double-slit.md)**

$$
\Delta = \dfrac{d\,y}{D} \qquad \Delta = n\lambda \;(\text{bright}) \qquad \Delta = \left(n+\tfrac12\right)\lambda \;(\text{dark}) \qquad \beta = \dfrac{\lambda D}{d}
$$

**[2. Slit Diffraction](experiments/slit-diffraction.md)**

$$
a\sin\theta = m\lambda \qquad (a+b)\sin\theta = n\lambda \qquad R = \dfrac{\lambda}{\Delta\lambda} = nN
$$

**[3. Polarization & Malus's Law](experiments/polarization-malus.md)**

$$
I(\theta) = I_0\cos^2\theta
$$

**[4. Dispersion by a Prism](experiments/prism-dispersion.md)**

$$
n(\lambda) = A + \dfrac{B}{\lambda^2} \qquad \delta \approx (n-1)A_{\text{apex}} \qquad \omega = \dfrac{n_v - n_r}{n_y - 1}
$$

**[5. Michelson Interferometer](experiments/michelson-interferometer.md)**

$$
\text{OPD} = 2\,\Delta L \qquad \Delta m = \dfrac{2\,\Delta L}{\lambda} \qquad \Delta L = \dfrac{\Delta m\,\lambda}{2}
$$

## Geometrical Optics

**[6. Focusing by a Convex Lens](experiments/convex-lens-focusing.md)**

$$
N_f = \dfrac{f}{D} \qquad r_{\text{Airy}} \approx 1.22\,\dfrac{\lambda f}{D}
$$

**[7. Compound Lens System](experiments/compound-lens-system.md)**

$$
\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f} \qquad m_i = -\dfrac{v_i}{u_i} \qquad m_{\text{total}} = m_1 \times m_2
$$

## Particle Nature of Light

**[8. Photoelectric Effect](experiments/photoelectric-effect.md)**

$$
E = h\nu = \dfrac{hc}{\lambda} \qquad KE_{\max} = h\nu - \phi \qquad V_0 = \dfrac{h\nu - \phi}{e}
$$

**[9. Compton Scattering](experiments/compton-scattering.md)**

$$
\Delta\lambda = \lambda_C(1-\cos\theta) \qquad \lambda_C = \dfrac{h}{m_e c} = 2.426\ \text{pm} \qquad \lambda' = \lambda + \Delta\lambda
$$

**[10. Single-Photon Double-Slit](experiments/single-photon-double-slit.md)**

$$
P(y) \propto \cos^2\!\left(\dfrac{\pi d y}{\lambda D}\right)
$$

## Laser Light Concepts

**[11. Coherence Length & Time](experiments/coherence.md)**

$$
\tau_c \approx \dfrac{1}{\Delta\nu} \qquad L_c = c\,\tau_c
$$

**[12. Directionality & Beam Quality](experiments/directionality-beam-quality.md)**

$$
D_{\text{spot}}(L) \approx D_0 + \theta_{\text{div}}\,L
$$

**[13. Monochromaticity & Spectral Purity](experiments/monochromaticity-purity.md)**

$$
\text{Purity} = \dfrac{\Delta\lambda}{\lambda}
$$

**[14. Making a Hologram](experiments/holography.md)**

$$
I = |E_{\text{obj}} + E_{\text{ref}}|^2 = |E_{\text{obj}}|^2 + |E_{\text{ref}}|^2 + 2\,\text{Re}\!\left(E_{\text{obj}}E_{\text{ref}}^{*}\right)
$$

## Explore & Stay Safe

**[15. Red → UV Wavelength & Photon-Energy Explorer](experiments/wavelength-explorer.md)**

$$
\nu = \dfrac{c}{\lambda} \qquad E = h\nu = \dfrac{hc}{\lambda}
$$

## Practical Applications

**[16. Laser Doppler Vibrometry](experiments/laser-doppler-vibrometry.md)**

$$
f_D = \dfrac{2v\cos\theta}{\lambda} \qquad v_{max} = A\omega
$$

**[17. Optical Fiber NA & Attenuation](experiments/optical-fiber-na-attenuation.md)**

$$
\text{NA} = \sqrt{n_1^{2}-n_2^{2}} \qquad P_{out} = P_{in}\times 10^{-\alpha L/10}
$$

**[18. Laser Speckle Metrology](experiments/laser-speckle-metrology.md)**

$$
s \approx 1.22\dfrac{\lambda z}{D} \qquad C \approx 1-\exp\!\left[-\left(\dfrac{2\pi\sigma}{\lambda}\right)^{2}\right]
$$

## Physical Constants Used Throughout

| Constant | Symbol | Value |
|---|---|---|
| Speed of light | c | 3 × 10⁸ m/s |
| Planck's constant | h | 6.626 × 10⁻³⁴ J·s (= 4.1357 × 10⁻¹⁵ eV·s) |
| Electron charge | e | 1.602 × 10⁻¹⁹ C |
| Electron rest mass | mₑ | 9.109 × 10⁻³¹ kg |
| Compton wavelength | λ_C = h/(mₑc) | 2.426 pm |
| Thermal voltage (300 K) | V_T = kT/e | 25.85 mV |
