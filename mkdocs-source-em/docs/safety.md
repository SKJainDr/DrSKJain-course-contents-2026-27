# Electrical & Magnetic Safety, Precautions & Potential Harm

!!! warning "Essential Reading Before Any Real Electrical Experiment"
    Several experiments and workshops in this lab correspond to real hazards when performed with physical
    apparatus — high voltages (Van de Graaff generator, HV breakdown testing), stored energy in capacitors and
    inductors, strong magnetic fields, and RF power. Read this section before touching any real apparatus.

!!! danger "Warning"
    Never touch the terminals of a charged capacitor, energised HV supply, or an inductor immediately after
    switch-off — stored energy can deliver a dangerous shock even after the source is disconnected.

!!! tip "Try it live"
    Explore the physics on the interactive simulator with real-time sliders and graphs:
    **[🔬 Launch in Simulator](../../labs/advanced-electricity-magnetism-lab.html){target=_blank}**

## Hazard Categories

| Hazard | Typical source in this lab | Risk | Precaution |
|---|---|---|---|
| Electric shock | Charged capacitors, Van de Graaff dome, HV breakdown testing | Cardiac/muscular injury, burns | De-energize and discharge through a bleeder resistor before touching; never work alone on real HV apparatus |
| Capacitor/inductor stored energy | RC/RL transient circuits, LCR resonance | Shock or component explosion if shorted carelessly | Always discharge capacitors through a resistor, never a direct short; respect voltage/current ratings |
| Strong magnetic fields | Solenoids, Helmholtz coils, electromagnets | Interference with pacemakers/implants; ferromagnetic tool/object projectiles | Keep persons with medical implants away from strong-field areas; secure loose ferromagnetic objects |
| High-frequency RF | Antenna workshop, RF impedance-matching workshop | RF burns, tissue heating at high power | Never approach an energized transmitting antenna; follow RF-exposure guidelines |
| Corona/ozone | Van de Graaff generator, sharp-point conductors at high voltage | Ozone irritation, unwanted discharge/fire risk | Operate in ventilated spaces; keep flammable materials away from active corona regions |
| Eye/skin exposure | High-voltage arcs, breakdown testing | UV flash burns, arc-flash injury | Use appropriate face/eye protection during real breakdown testing; maintain safe standoff distance |

## General Precautions for Real Apparatus

- Always treat a capacitor or inductor as charged/energized until you have personally verified otherwise with a
  meter, and discharge it safely through an appropriate resistor before handling.
- Never defeat interlocks or safety enclosures on high-voltage equipment, even "just to look."
- Keep one hand in your pocket when probing live circuits, to reduce the risk of a shock path across the chest.
- Ensure a competent second person is present whenever working with voltages above extra-low-voltage limits.
- Ground/earth exposed conductive enclosures of test equipment before energizing.
- Know the location of the nearest emergency power cut-off before starting any high-power experiment.
- For any workshop scenario in this guide involving genuinely hazardous voltages, currents, or RF power
  (HV insulation testing, transformer testing, antenna transmission, EMI/EMC testing), treat the numbers
  simulated here as illustrative only — real work of this kind requires certified equipment, training, and
  supervision, and is not something to attempt from this guide alone.

## Reporting

If you are ever unsure whether a piece of real apparatus is safe to touch or energize, stop and ask your
laboratory supervisor before proceeding. It is always acceptable to pause an experiment for a safety check.
