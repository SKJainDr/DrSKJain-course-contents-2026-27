# Formula Quick Reference

A single-page cheat-sheet of every governing equation used across the 18 experiments, grouped the same way as the main [Contents](index.md). Use this page while doing calculations so you don't have to open each experiment page individually — click the linked experiment name if you need the full derivation or context.

## Rotational Dynamics

**[1. Bifilar Suspension](experiments/bifilar-suspension.md)**

$$
T = 2\pi\sqrt{\dfrac{I l}{Mgb^{2}}} \qquad I = \dfrac{M g b^{2} T^{2}}{4\pi^{2} l}
$$

**[2. Torsional Pendulum](experiments/torsional-pendulum.md)**

$$
C = \dfrac{\pi\eta r^{4}}{2l} \qquad I = \dfrac{2md^{2}T^{2}}{T'^{2}-T^{2}} \qquad \eta = \dfrac{8\pi l I}{r^{4}T^{2}}
$$

**[3. Flywheel](experiments/flywheel.md)**

$$
\omega = \dfrac{2\pi n_{1}}{t} \qquad I = \dfrac{mr^{2}(2gh-\omega^{2}r^{2})}{\omega^{2}}\times\dfrac{n_{2}}{n_{1}+n_{2}}
$$

**[4. Compound (Bar) Pendulum](experiments/compound-pendulum.md)**

$$
T = 2\pi\sqrt{\dfrac{k^{2}+h^{2}}{gh}} \qquad h_{1}h_{2}=k^{2} \qquad g = \dfrac{4\pi^{2}L}{T^{2}}
$$

## Elasticity of Solids

**[5. Non-Uniform (Cantilever) Bending](experiments/non-uniform-bending.md)**

$$
Y = \dfrac{4Wl^{3}}{bd^{3}y}
$$

**[6. Uniform Bending](experiments/uniform-bending.md)**

$$
Y = \dfrac{3Mga l^{2}}{2bd^{3}e}
$$

**[7. Searle's Apparatus](experiments/searle-apparatus.md)**

$$
Y = \dfrac{MgL}{\pi r^{2} l_{\text{ext}}}
$$

**[8. Static Torsion](experiments/static-torsion.md)**

$$
\theta = \dfrac{2Cl}{\pi\eta r^{4}} \qquad \eta = \dfrac{2Cl}{\pi r^{4}\theta}
$$

## Fluid Properties: Viscosity & Surface Tension

**[9. Poiseuille's Method](experiments/poiseuille-viscosity.md)**

$$
\eta = \dfrac{\pi P r^{4} t}{8Vl}, \qquad P=\rho g h
$$

**[10. Stokes' Method](experiments/stokes-viscosity.md)**

$$
\eta = \dfrac{2}{9}\dfrac{r^{2}g(\rho-\sigma)}{v}
$$

**[11. Capillary Rise](experiments/capillary-rise.md)**

$$
T = \dfrac{h r \rho g}{2}
$$

## Oscillations, Damping & Acoustic Methods (PG)

**[12. Coupled Pendulums](experiments/coupled-pendulums.md)**

$$
f_{s}=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{l}} \qquad f_{a}=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{l}+\dfrac{2k}{m}} \qquad T_{\text{beat}}=\dfrac{1}{f_{a}-f_{s}}
$$

**[13. Damped Oscillations](experiments/damped-oscillations.md)**

$$
A_{n}=A_{0}e^{-\gamma t} \qquad \delta = \ln\!\left(\dfrac{A_{n}}{A_{n+1}}\right)=\gamma T \qquad Q\approx\dfrac{\pi}{\delta}
$$

**[14. Forced Oscillations & Resonance](experiments/forced-oscillations-resonance.md)**

$$
A(\omega)=\dfrac{F_{0}/m}{\sqrt{(\omega_{0}^{2}-\omega^{2})^{2}+(2\gamma\omega)^{2}}} \qquad Q=\dfrac{f_{0}}{\Delta f}
$$

**[15. Ultrasonic Interferometer](experiments/ultrasonic-interferometer.md)**

$$
\lambda = 2\overline{\Delta d} \qquad v=f\lambda \qquad \beta=\dfrac{1}{\rho v^{2}} \qquad K=\rho v^{2}
$$

## Practical Applications

**[16. Ballistic Pendulum](experiments/ballistic-pendulum.md)**

$$
v = \dfrac{M+m}{m}\sqrt{2gh} \qquad 1-\cos\theta = \dfrac{m^{2}v^{2}}{2gL(M+m)^{2}}
$$

**[17. Rolling Race on an Incline](experiments/rolling-race-incline.md)**

$$
a = \dfrac{g\sin\theta}{1+k} \qquad I = kmr^{2} \qquad t = \sqrt{\dfrac{2L}{a}}
$$

**[18. Gyroscopic Precession](experiments/gyroscopic-precession.md)**

$$
L = I\omega = \tfrac{1}{2}MR^{2}\omega \qquad \tau = Mgd \qquad \Omega = \dfrac{\tau}{L} = \dfrac{2gd}{R^{2}\omega}
$$

