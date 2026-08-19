# -*- coding: utf-8 -*-
"""
Per-experiment plain-text formula/graph/error metadata for the E&M booklet.
Graph title/axis labels and error-formula/note/variables are extracted
programmatically from each experiment's .md file by build_booklet_em.py;
this module supplies only the plain-text "Formula Used" panel (formula +
symbol meanings), since the .md files store some formulas as LaTeX for
MathJax rendering, which needs a plain-Unicode equivalent for the PDF.
"""

FORMULAS = {
    # ---- Electrostatics ----
    "coulombs-law.md": ("F = q\u2081q\u2082 / (4\u03c0\u03b5\u2080\u03b5r r\u00b2)", [
        ("F", "electrostatic force between the charges (N)"),
        ("q\u2081, q\u2082", "the two point charges (C)"),
        ("r", "separation between the charges (m)"),
        ("\u03b5r", "relative permittivity of the surrounding medium"),
    ]),
    "dipole-field-potential.md": ("E_axial = 2kp / r\u00b3 ,  p = q\u00b7(2a)", [
        ("E_axial", "on-axis field of the dipole (N/C)"),
        ("p", "dipole moment"),
        ("r", "distance from the dipole centre"),
    ]),
    "gauss-law-flux.md": ("\u03a6 = Q_enc / \u03b5\u2080", [
        ("\u03a6", "total electric flux through the closed surface"),
        ("Q_enc", "net charge enclosed by the surface"),
    ]),
    "parallel-plate-capacitor.md": ("C = \u03b5\u2080\u03b5r A / d", [
        ("C", "capacitance (F)"),
        ("A", "plate area"),
        ("d", "plate separation"),
        ("\u03b5r", "relative permittivity of the dielectric, if present"),
    ]),
    "conductors-charge-distribution.md": ("\u03c3 = Q / A  (surface charge density, varies with curvature)", [
        ("\u03c3", "local surface charge density"),
        ("Q", "total charge on the conductor"),
    ]),
    "image-charge-grounded-plane.md": ("F = q\u00b2 / (4\u03c0\u03b5\u2080(2d)\u00b2)", [
        ("F", "attractive force towards the grounded plane (N)"),
        ("q", "point charge magnitude (C)"),
        ("d", "height of the charge above the plane (m)"),
    ]),
    "multipole-expansion-quadrupole.md": ("V_quad(r) = 3qa\u00b2 / (4\u03c0\u03b5\u2080 r\u00b3)", [
        ("V", "on-axis quadrupole potential (V)"),
        ("q", "end-charge magnitude (C)"),
        ("a", "charge spacing (m)"),
        ("r", "field-point distance, r \u226b a"),
    ]),
    # ---- Magnetostatics ----
    "biot-savart-wire.md": ("B = \u03bc\u2080 I / (2\u03c0 r)", [
        ("B", "magnetic flux density at distance r (T)"),
        ("I", "current in the wire (A)"),
        ("r", "perpendicular distance from the wire"),
    ]),
    "circular-coil-helmholtz.md": ("B_axis = \u03bc\u2080 I a\u00b2 / (2(a\u00b2+x\u00b2)^(3/2))", [
        ("B_axis", "on-axis field of a circular coil (T)"),
        ("I", "coil current (A)"),
        ("a", "coil radius"),
        ("x", "axial distance from the coil centre"),
    ]),
    "ampere-law-solenoid-toroid.md": ("B_solenoid = \u03bc\u2080 n I ,  B_toroid = \u03bc\u2080 N I / (2\u03c0r)", [
        ("n", "turns per unit length (solenoid)"),
        ("N", "total turns (toroid)"),
        ("I", "current (A)"),
    ]),
    "force-parallel-conductors.md": ("F/L = \u03bc\u2080 I\u2081I\u2082 / (2\u03c0d)", [
        ("F/L", "force per unit length between the wires (N/m)"),
        ("I\u2081, I\u2082", "currents in the two wires (A)"),
        ("d", "separation between the wires"),
    ]),
    "magnetic-vector-potential-dipole.md": ("A_\u03c6(r,\u03b8) = \u03bc\u2080 I a\u00b2 sin\u03b8 / (4r\u00b2)", [
        ("A_\u03c6", "azimuthal vector potential (T\u00b7m)"),
        ("I", "loop current (A)"),
        ("a", "loop radius"),
        ("r, \u03b8", "spherical field-point coordinates, r \u226b a"),
    ]),
    "cyclotron-velocity-selector.md": ("v = E/B ,  r_c = mv/(qB)", [
        ("v", "selected (undeflected) speed (m/s)"),
        ("E, B", "crossed electric and magnetic fields"),
        ("r_c", "cyclotron radius in the pure B-field region"),
    ]),
    # ---- Electrodynamics ----
    "faraday-induction.md": ("EMF = \u2212N d\u03a6/dt", [
        ("EMF", "induced electromotive force (V)"),
        ("N", "number of turns in the coil"),
        ("d\u03a6/dt", "rate of change of magnetic flux linkage"),
    ]),
    "motional-emf-lenz.md": ("EMF = BLv", [
        ("EMF", "motional electromotive force (V)"),
        ("B", "magnetic flux density (T)"),
        ("L", "rail separation (rod length in the field)"),
        ("v", "velocity of the sliding rod"),
    ]),
    "rc-rl-transients.md": ("V_C(t) = V(1\u2212e^(\u2212t/RC)) ,  I_L(t) = (V/R)(1\u2212e^(\u2212Rt/L))", [
        ("V_C(t), I_L(t)", "capacitor voltage / inductor current during charging"),
        ("R, C, L", "resistance, capacitance, inductance"),
    ]),
    "lcr-resonance.md": ("f\u2080 = 1/(2\u03c0\u221a(LC)) ,  Q = \u03c9\u2080L/R", [
        ("f\u2080", "series-resonance frequency (Hz)"),
        ("Q", "quality factor of the circuit"),
        ("L, C, R", "inductance, capacitance, resistance"),
    ]),
    "eddy-current-damping.md": ("F_eddy \u221d \u03c3 t B\u00b2 v w\u00b2", [
        ("F_eddy", "eddy-current retarding force (N)"),
        ("\u03c3, t", "plate conductivity and thickness"),
        ("B, v", "field strength and plate velocity"),
    ]),
    "rlc-filter-response.md": ("|H(f)|_bandpass = R / \u221a(R\u00b2+(\u03c9L\u22121/\u03c9C)\u00b2)", [
        ("|H(f)|", "band-pass voltage-gain magnitude (0\u20131)"),
        ("R, L, C", "series resistance, inductance, capacitance"),
        ("\u03c9", "angular frequency, \u03c9 = 2\u03c0f"),
    ]),
    "poynting-vector-coaxial-cable.md": ("S(r) = VI / (2\u03c0 r\u00b2 ln(b/a))", [
        ("S(r)", "axial Poynting flux at radius r (W/m\u00b2)"),
        ("V, I", "conductor voltage and current"),
        ("a, b", "inner- and outer-conductor radii"),
    ]),
    # ---- EM Waves & Propagation ----
    "maxwell-plane-waves.md": ("c = 1/\u221a(\u03bc\u2080\u03b5\u2080) ,  E/B = c", [
        ("c", "speed of light in vacuum"),
        ("E, B", "transverse, mutually perpendicular, in-phase field amplitudes"),
    ]),
    "wave-propagation-media-skindepth.md": ("\u03b4 = \u221a(2/(\u03c9\u03bc\u03c3)) ,  E(x) = E\u2080 e^(\u2212x/\u03b4)", [
        ("\u03b4", "skin depth in the conducting medium"),
        ("\u03c9, \u03bc, \u03c3", "angular frequency, permeability, conductivity"),
    ]),
    "reflection-refraction-brewster.md": ("n\u2081sin\u03b8\u1d62 = n\u2082sin\u03b8_t ,  tan\u03b8_B = n\u2082/n\u2081", [
        ("\u03b8\u1d62, \u03b8_t", "angles of incidence and refraction"),
        ("\u03b8_B", "Brewster angle (fully polarised reflection)"),
        ("n\u2081, n\u2082", "refractive indices of the two media"),
    ]),
    "waveguide-cutoff-frequency.md": ("f_c(TE10) = c / (2a)", [
        ("f_c", "cutoff frequency of the dominant TE\u2081\u2080 mode (Hz)"),
        ("a", "waveguide broad-wall dimension (m)"),
    ]),
    "transmission-line-impedance-vswr.md": ("\u0393 = (Z_L\u2212Z\u2080)/(Z_L+Z\u2080) ,  VSWR = (1+|\u0393|)/(1\u2212|\u0393|)", [
        ("\u0393", "voltage reflection coefficient"),
        ("Z\u2080, Z_L", "line characteristic impedance and load impedance"),
        ("VSWR", "voltage standing-wave ratio (\u2265 1)"),
    ]),
    "faraday-cage-shielding-effectiveness.md": ("SE (dB) = 8.69 t/\u03b4 ,  \u03b4 = \u221a(2/(\u03c9\u03bc\u03c3))", [
        ("SE", "shielding effectiveness (dB, absorption loss)"),
        ("t", "enclosure wall thickness"),
        ("\u03b4", "skin depth of the wall material"),
    ]),
    # ---- Electric & Magnetic Materials ----
    "dielectric-polarization-clausius-mossotti.md": ("(\u03b5r\u22121)/(\u03b5r+2) = N\u03b1/(3\u03b5\u2080)", [
        ("\u03b5r", "relative permittivity of the dielectric"),
        ("N", "number density of molecules"),
        ("\u03b1", "molecular polarizability"),
    ]),
    "magnetic-hysteresis-bh-curve.md": ("H_c \u2248 0.15 \u00d7 H_max  (model estimate of coercivity)", [
        ("H_c", "coercivity of the ferromagnetic core"),
        ("H_max", "peak applied magnetising field"),
    ]),
    "hall-effect-carrier-density.md": ("V_H = IB / (n\u00b7e\u00b7t)", [
        ("V_H", "Hall voltage across the sample (V)"),
        ("I, B", "sample current and transverse field"),
        ("n, t", "carrier density and sample thickness"),
    ]),
    "meissner-effect-flux-expulsion.md": ("B(x) = B\u2080 e^(\u2212x/\u03bb)", [
        ("B(x)", "field remaining at depth x inside the superconductor"),
        ("B\u2080", "applied surface field"),
        ("\u03bb", "London penetration depth"),
    ]),
}
