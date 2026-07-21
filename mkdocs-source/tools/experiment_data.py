# -*- coding: utf-8 -*-
"""
Central per-experiment data for:
  - the graph title / axis labels (variable name + unit only, no numeric scale)
  - the maximum-permissible-error formula, explanation, and the list of
    least-count (LC) input fields needed for the interactive calculator /
    printable booklet.

Used by both build_booklet.py (PDF) and insert_error_calc.py (docs JS widget
+ markdown sections).
"""

EXPERIMENTS = [
    {
        "file": "youngs-double-slit.md",
        "panel": "interference",
        "graph_title": "Fringe Width vs Wavelength",
        "x_label": "Wavelength, \u03bb (nm)",
        "y_label": "Fringe width, \u03b2 (mm)",
        "error_result_symbol": "\u03b2",
        "error_formula_text": "\u0394\u03b2 / \u03b2  =  \u0394\u03bb/\u03bb  +  \u0394D/D  +  \u0394d/d",
        "error_note": "\u03b2 = \u03bbD/d is a simple product/quotient of three measured quantities, so the "
                       "maximum fractional error is the sum of the fractional errors (least count / measured "
                       "value) of each.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8},
            {"key": "D", "label": "D", "name": "Slit-to-screen distance", "unit": "cm", "default": 100},
            {"key": "d", "label": "d", "name": "Slit separation", "unit": "\u03bcm", "default": 500},
        ],
        "formula_js": "var beta = (lam.v*D.v)/d.v; var rel = lam.lc/lam.v + D.lc/D.v + d.lc/d.v; "
                       "return {Y: beta, Yunit:'mm (scale-dependent; treat as relative)', dY: beta*rel, pct: rel*100};",
    },
    {
        "file": "slit-diffraction.md",
        "panel": "diffraction",
        "graph_title": "Grating Element vs sin\u03b8 (slope method)",
        "x_label": "sin\u03b8 (order n = 1)",
        "y_label": "Grating element, (a+b) (\u03bcm)",
        "error_result_symbol": "(a+b)",
        "error_formula_text": "\u0394(a+b) / (a+b)  =  \u0394\u03bb/\u03bb  +  cot\u03b8 \u00b7 \u0394\u03b8",
        "error_note": "From (a+b) sin\u03b8 = n\u03bb, differentiating gives a cot\u03b8 term for the angle "
                       "uncertainty in addition to the wavelength's fractional error.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8},
            {"key": "theta", "label": "\u03b8", "name": "Diffraction angle", "unit": "\u00b0", "default": 20},
        ],
        "formula_js": "var th = theta.v*Math.PI/180; var dth = theta.lc*Math.PI/180; "
                       "var rel = lam.lc/lam.v + (Math.cos(th)/Math.sin(th))*dth; "
                       "var ab = lam.v/Math.sin(th); return {Y: ab, Yunit:'nm (arbitrary order n=1)', dY: ab*rel, pct: rel*100};",
    },
    {
        "file": "polarization-malus.md",
        "panel": "polarization",
        "graph_title": "Transmitted Intensity vs cos\u00b2\u03b8",
        "x_label": "cos\u00b2\u03b8",
        "y_label": "Transmitted intensity, I (%)",
        "error_result_symbol": "I",
        "error_formula_text": "\u0394I / I  =  \u0394I\u2080/I\u2080  +  2 tan\u03b8 \u00b7 \u0394\u03b8",
        "error_note": "I = I\u2080cos\u00b2\u03b8, so d(ln I) = d(ln I\u2080) \u2212 2 tan\u03b8\u00b7d\u03b8; the angle term "
                       "grows rapidly as \u03b8 \u2192 90\u00b0, so avoid taking your reading very close to the "
                       "crossed-polarizer position.",
        "variables": [
            {"key": "I0", "label": "I\u2080", "name": "Reference intensity", "unit": "%", "default": 100},
            {"key": "theta", "label": "\u03b8", "name": "Analyzer angle", "unit": "\u00b0", "default": 30},
        ],
        "formula_js": "var th = theta.v*Math.PI/180; var dth = theta.lc*Math.PI/180; "
                       "var rel = I0.lc/I0.v + 2*Math.tan(th)*dth; "
                       "var I = I0.v*Math.pow(Math.cos(th),2); return {Y: I, Yunit:'%', dY: I*rel, pct: rel*100};",
    },
    {
        "file": "prism-dispersion.md",
        "panel": "dispersion",
        "graph_title": "Refractive Index vs 1/\u03bb\u00b2 (Cauchy plot)",
        "x_label": "1 / \u03bb\u00b2  (\u03bcm\u207b\u00b2)",
        "y_label": "Refractive index, n",
        "error_result_symbol": "n",
        "error_formula_text": "\u0394n  \u2248  \u00bd\u00b7cot[(A+\u03b4m)/2]\u00b7(\u0394A+\u0394\u03b4m)  +  \u00bd\u00b7cot(A/2)\u00b7\u0394A",
        "error_note": "From n = sin[(A+\u03b4m)/2] / sin(A/2), where A is the prism apex angle and \u03b4m the "
                       "angle of minimum deviation. Both are read off the same spectrometer circular scale, "
                       "so use its vernier least count for both \u0394A and \u0394\u03b4m.",
        "variables": [
            {"key": "A", "label": "A", "name": "Apex angle", "unit": "\u00b0", "default": 60, "hasLC": False},
            {"key": "dm", "label": "\u03b4m", "name": "Angle of minimum deviation", "unit": "\u00b0", "default": 40, "hasLC": False},
            {"key": "lc", "label": "LC", "name": "Spectrometer vernier least count", "unit": "\u00b0", "default": 0.083, "isLC": True},
        ],
        "formula_js": "var Ar = A.v*Math.PI/180, dmr = dm.v*Math.PI/180, lcr = lc.v*Math.PI/180; "
                       "var n = Math.sin((Ar+dmr)/2)/Math.sin(Ar/2); "
                       "var dn = 0.5*(1/Math.tan((Ar+dmr)/2))*(2*lcr) + 0.5*(1/Math.tan(Ar/2))*lcr; "
                       "return {Y: n, Yunit:'(dimensionless)', dY: dn, pct: (dn/n)*100};",
    },
    {
        "file": "michelson-interferometer.md",
        "panel": "michelson",
        "graph_title": "Fringe-Order Shift vs Mirror Displacement",
        "x_label": "Mirror displacement, \u0394L (nm)",
        "y_label": "Fringe order shift, \u0394m",
        "error_result_symbol": "\u0394L",
        "error_formula_text": "\u0394(\u0394L)  =  (\u03bb/2)\u00d7(fringe-counting uncertainty)  +  \u0394L\u00d7(\u0394\u03bb/\u03bb)",
        "error_note": "\u0394L = \u0394m\u00b7\u03bb/2. The dominant error is usually miscounting fringes by \u00b11 near the "
                       "start/end of a sweep, contributing \u00b1\u03bb/2 directly; the source's own spectral "
                       "uncertainty adds a smaller relative term.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8, "hasLC": False},
            {"key": "lamlc", "label": "\u0394\u03bb", "name": "Source spectral uncertainty", "unit": "nm", "default": 0.01, "isLC": True},
            {"key": "dm", "label": "\u0394m", "name": "Fringes counted", "unit": "fringes", "default": 500, "hasLC": False},
            {"key": "dmlc", "label": "\u00b1", "name": "Counting uncertainty", "unit": "fringes", "default": 1, "isLC": True},
        ],
        "formula_js": "var DL = (dm.v*lam.v)/2; var errFromCount = (lam.v/2)*dmlc.v; "
                       "var errFromLam = DL*(lamlc.v/lam.v); var dDL = errFromCount + errFromLam; "
                       "return {Y: DL, Yunit:'nm', dY: dDL, pct: (dDL/DL)*100};",
    },
    {
        "file": "convex-lens-focusing.md",
        "panel": "focusing",
        "graph_title": "Spot Radius vs f-number",
        "x_label": "f-number, N_f = f/D",
        "y_label": "Spot radius, r (\u03bcm)",
        "error_result_symbol": "r",
        "error_formula_text": "\u0394r / r  =  \u0394\u03bb/\u03bb  +  \u0394f/f  +  \u0394D/D",
        "error_note": "r = 1.22\u03bbf/D is a product/quotient of three measured quantities \u2014 sum the "
                       "fractional (least count / value) errors of each.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8},
            {"key": "f", "label": "f", "name": "Focal length", "unit": "cm", "default": 10},
            {"key": "D", "label": "D", "name": "Aperture diameter", "unit": "cm", "default": 2.5},
        ],
        "formula_js": "var r = 1.22*lam.v*f.v/D.v; var rel = lam.lc/lam.v + f.lc/f.v + D.lc/D.v; "
                       "return {Y: r, Yunit:'nm (convert to \u03bcm by /1000)', dY: r*rel, pct: rel*100};",
    },
    {
        "file": "compound-lens-system.md",
        "panel": "compound",
        "graph_title": "Final Image Distance vs Object Distance",
        "x_label": "Object distance, u\u2081 (cm)",
        "y_label": "Final image distance, v\u2082 (cm)",
        "error_result_symbol": "v",
        "error_formula_text": "\u0394v  =  v\u00b2 \u00b7 ( \u0394f/f\u00b2  +  \u0394u/u\u00b2 )",
        "error_note": "From 1/v = 1/f + 1/u for a single lens stage, propagate the errors in the measured "
                       "object distance u and the known/measured focal length f. Apply once per lens stage.",
        "variables": [
            {"key": "u", "label": "u", "name": "Object distance", "unit": "cm", "default": 15},
            {"key": "f", "label": "f", "name": "Focal length", "unit": "cm", "default": 10},
        ],
        "formula_js": "var v = (f.v*u.v)/(u.v-f.v); "
                       "var dv = Math.pow(v,2)*( f.lc/Math.pow(f.v,2) + u.lc/Math.pow(u.v,2) ); "
                       "return {Y: v, Yunit:'cm', dY: dv, pct: (dv/Math.abs(v))*100};",
    },
    {
        "file": "photoelectric-effect.md",
        "panel": "photoelectric",
        "graph_title": "Stopping Voltage vs Frequency",
        "x_label": "Frequency, \u03bd (\u00d710\u00b9\u2074 Hz)",
        "y_label": "Stopping voltage, V\u2080 (V)",
        "error_result_symbol": "V\u2080",
        "error_formula_text": "\u0394V\u2080  =  (h\u00b7\u0394\u03bd)/e  +  \u0394\u03c6/e   ,   \u0394\u03bd/\u03bd = \u0394\u03bb/\u03bb",
        "error_note": "V\u2080 = (h\u03bd \u2212 \u03c6)/e is an affine (not multiplicative) relation, so errors from "
                       "frequency (via the wavelength selector's least count) and from the work function "
                       "uncertainty simply add.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 400},
            {"key": "phi", "label": "\u03c6", "name": "Work function", "unit": "eV", "default": 2.3, "hasLC": False},
            {"key": "philc", "label": "\u0394\u03c6", "name": "Work function uncertainty", "unit": "eV", "default": 0.02, "isLC": True},
        ],
        "formula_js": "var c=2.998e8, h=4.1357e-15; var nu = c/(lam.v*1e-9); "
                       "var dnu = nu*(lam.lc/lam.v); var V0 = h*nu - phi.v; "
                       "var dV0 = h*dnu + philc.v; return {Y: V0, Yunit:'V', dY: dV0, pct: (dV0/Math.abs(V0))*100};",
    },
    {
        "file": "compton-scattering.md",
        "panel": "compton",
        "graph_title": "Wavelength Shift vs (1 \u2212 cos\u03b8)",
        "x_label": "1 \u2212 cos\u03b8",
        "y_label": "Wavelength shift, \u0394\u03bb (pm)",
        "error_result_symbol": "\u0394\u03bb",
        "error_formula_text": "\u0394(\u0394\u03bb)  =  \u03bb_C \u00b7 sin\u03b8 \u00b7 \u0394\u03b8",
        "error_note": "\u0394\u03bb = \u03bb_C(1\u2212cos\u03b8); differentiating with respect to the scattering angle "
                       "gives this term. The Compton wavelength \u03bb_C is a fundamental constant with negligible "
                       "uncertainty.",
        "variables": [
            {"key": "theta", "label": "\u03b8", "name": "Scattering angle", "unit": "\u00b0", "default": 90},
            {"key": "thetalc", "label": "\u0394\u03b8", "name": "Goniometer least count", "unit": "\u00b0", "default": 0.5, "isLC": True},
        ],
        "formula_js": "var lamC = 2.426; var th = theta.v*Math.PI/180, dth = theta.lc*Math.PI/180; "
                       "var dlam = lamC*(1-Math.cos(th)); var ddlam = lamC*Math.sin(th)*dth; "
                       "return {Y: dlam, Yunit:'pm', dY: ddlam, pct: (ddlam/dlam)*100};",
    },
    {
        "file": "single-photon-double-slit.md",
        "panel": "singlephoton",
        "graph_title": "Detected Counts vs Position (build-up)",
        "x_label": "Screen position, y (a.u.)",
        "y_label": "Photon counts, N",
        "error_result_symbol": "N",
        "error_formula_text": "\u0394N  =  \u221aN     (Poisson counting statistics)     \u2192     relative error = 1/\u221aN",
        "error_note": "This experiment is a qualitative demonstration, not an instrumental measurement \u2014 "
                       "its natural 'error' is the statistical counting uncertainty of accumulating discrete "
                       "photon detection events, which shrinks as more photons are collected.",
        "variables": [
            {"key": "N", "label": "N", "name": "Total photons detected", "unit": "counts", "default": 2500, "hasLC": False},
        ],
        "formula_js": "var dN = Math.sqrt(N.v); return {Y: N.v, Yunit:'counts', dY: dN, pct: (dN/N.v)*100};",
    },
    {
        "file": "coherence.md",
        "panel": "coherence",
        "graph_title": "Coherence Length vs Spectral Linewidth",
        "x_label": "Linewidth, \u0394\u03bd (Hz, log scale suggested)",
        "y_label": "Coherence length, L_c (m, log scale suggested)",
        "error_result_symbol": "L_c",
        "error_formula_text": "\u0394L_c / L_c  =  \u0394(\u0394\u03bd) / \u0394\u03bd",
        "error_note": "L_c = c/\u0394\u03bd (c is exact), so the fractional error in coherence length equals the "
                       "fractional error in your measurement of the source's spectral linewidth.",
        "variables": [
            {"key": "dnu", "label": "\u0394\u03bd", "name": "Spectral linewidth", "unit": "MHz", "default": 1.0, "hasLC": False},
            {"key": "dnulc", "label": "\u0394(\u0394\u03bd)", "name": "Linewidth measurement uncertainty", "unit": "MHz", "default": 0.05, "isLC": True},
        ],
        "formula_js": "var c=2.998e8; var Lc = c/(dnu.v*1e6); var rel = dnulc.v/dnu.v; "
                       "return {Y: Lc, Yunit:'m', dY: Lc*rel, pct: rel*100};",
    },
    {
        "file": "directionality-beam-quality.md",
        "panel": "directionality",
        "graph_title": "Spot Diameter vs Propagation Distance",
        "x_label": "Propagation distance, L (m)",
        "y_label": "Spot diameter, D_spot (mm)",
        "error_result_symbol": "D_spot",
        "error_formula_text": "\u0394D_spot  =  \u0394D\u2080  +  L\u00b7\u0394\u03b8_div  +  \u03b8_div\u00b7\u0394L",
        "error_note": "D_spot(L) = D\u2080 + \u03b8_div\u00b7L is a sum, so absolute (not fractional) errors add "
                       "directly, each weighted by the relevant partial derivative.",
        "variables": [
            {"key": "D0", "label": "D\u2080", "name": "Initial beam diameter", "unit": "mm", "default": 2},
            {"key": "thetadiv", "label": "\u03b8_div", "name": "Angular divergence", "unit": "mrad", "default": 1.5},
            {"key": "L", "label": "L", "name": "Propagation distance", "unit": "m", "default": 5},
        ],
        "formula_js": "var Dspot = D0.v + thetadiv.v*L.v; "
                       "var dDspot = D0.lc + L.v*thetadiv.lc + thetadiv.v*L.lc; "
                       "return {Y: Dspot, Yunit:'mm', dY: dDspot, pct: (dDspot/Dspot)*100};",
    },
    {
        "file": "monochromaticity-purity.md",
        "panel": "monochromaticity",
        "graph_title": "Spectral Purity Comparison",
        "x_label": "Source type (categorical)",
        "y_label": "Purity, \u0394\u03bb/\u03bb (log scale suggested)",
        "error_result_symbol": "\u0394\u03bb/\u03bb",
        "error_formula_text": "\u0394(purity) / purity  =  \u0394W/W  +  \u0394\u03bb/\u03bb",
        "error_note": "purity = W/\u03bb, where W is the measured spectral linewidth. Sum the fractional error "
                       "in the linewidth measurement and in the central-wavelength measurement.",
        "variables": [
            {"key": "W", "label": "W", "name": "Spectral linewidth", "unit": "nm", "default": 0.001},
            {"key": "lam", "label": "\u03bb", "name": "Central wavelength", "unit": "nm", "default": 632.8},
        ],
        "formula_js": "var purity = W.v/lam.v; var rel = W.lc/W.v + lam.lc/lam.v; "
                       "return {Y: purity, Yunit:'(dimensionless)', dY: purity*rel, pct: rel*100};",
    },
    {
        "file": "holography.md",
        "panel": "holography",
        "graph_title": None,
        "x_label": None,
        "y_label": None,
        "error_result_symbol": None,
        "error_formula_text": None,
        "error_note": "Holography as presented here is a qualitative recording/reconstruction demonstration, "
                       "not an instrumental measurement \u2014 there is no single numeric result with a "
                       "propagated maximum permissible error. Use the space below to sketch/note the four "
                       "stages instead.",
        "variables": [],
        "formula_js": None,
    },
    {
        "file": "wavelength-explorer.md",
        "panel": "wavelength",
        "graph_title": "Photon Energy vs Wavelength",
        "x_label": "Wavelength, \u03bb (nm)",
        "y_label": "Photon energy, E (eV)",
        "error_result_symbol": "E",
        "error_formula_text": "\u0394E / E  =  \u0394\u03bb / \u03bb",
        "error_note": "E = hc/\u03bb (h, c exact), so the fractional error in photon energy equals the "
                       "fractional error in the wavelength measurement/setting.",
        "variables": [
            {"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 500},
        ],
        "formula_js": "var hc_eVnm = 1239.84; var E = hc_eVnm/lam.v; var rel = lam.lc/lam.v; "
                       "return {Y: E, Yunit:'eV', dY: E*rel, pct: rel*100};",
    },
    {
        "file": "laser-doppler-vibrometry.md",
        "panel": "vibrometry",
        "graph_title": "Peak Doppler Shift vs Vibration Frequency",
        "x_label": "Vibration frequency, f (Hz)",
        "y_label": "Peak Doppler shift, f_D,max (kHz)",
        "error_result_symbol": "v_max",
        "error_formula_text": "\u0394v_max / v_max  =  \u0394A/A  +  \u0394f/f",
        "error_note": "v_max = A\u03c9 = A(2\u03c0f) is a simple product of the vibration amplitude and (angular) frequency, "
                       "so their fractional errors simply add.",
        "variables": [
            {"key": "A", "label": "A", "name": "Vibration amplitude", "unit": "\u00b5m", "default": 10},
            {"key": "f", "label": "f", "name": "Vibration frequency", "unit": "Hz", "default": 100},
        ],
        "formula_js": "var A=vars['A']; var f=vars['f']; var omega=2*Math.PI*f.v; var vmax=(A.v/1000)*omega; "
                       "var rel = A.lc/A.v + f.lc/f.v; return {Y: vmax, Yunit:'mm/s', dY: vmax*rel, pct: rel*100};",
    },
    {
        "file": "optical-fiber-na-attenuation.md",
        "panel": "fiberoptic",
        "graph_title": "Output Power vs Fiber Length",
        "x_label": "Fiber length, L (km)",
        "y_label": "Output power (1 mW input), P (\u00b5W)",
        "error_result_symbol": "NA",
        "error_formula_text": "\u0394(NA) \u2248 (n\u2081\u0394n\u2081 + n\u2082\u0394n\u2082) / NA",
        "error_note": "NA = \u221a(n\u2081\u00b2\u2212n\u2082\u00b2); since NA is a square root of a difference of squares, its absolute "
                       "error is dominated by whichever refractive index (core or cladding) carries the larger "
                       "measurement uncertainty, weighted by that index's own value.",
        "variables": [
            {"key": "n1", "label": "n\u2081", "name": "Core refractive index", "unit": "(dimensionless)", "default": 1.48},
            {"key": "n2", "label": "n\u2082", "name": "Cladding refractive index", "unit": "(dimensionless)", "default": 1.46},
        ],
        "formula_js": "var n1=vars['n1']; var n2=vars['n2']; var NA=Math.sqrt(Math.max(n1.v*n1.v-n2.v*n2.v,0)); "
                       "var dNA=(n1.v*n1.lc+n2.v*n2.lc)/Math.max(NA,1e-6); return {Y: NA, Yunit:'(dimensionless)', dY: dNA, pct: (dNA/NA)*100};",
    },
    {
        "file": "laser-speckle-metrology.md",
        "panel": "speckle",
        "graph_title": "Speckle Contrast vs Roughness/Wavelength Ratio",
        "x_label": "\u03c3/\u03bb (dimensionless)",
        "y_label": "Speckle contrast (0\u20131)",
        "error_result_symbol": "s",
        "error_formula_text": "\u0394s / s  =  \u0394z/z  +  \u0394D/D",
        "error_note": "The speckle grain size s = 1.22\u03bbz/D is a product/quotient of measured quantities (\u03bb taken "
                       "as exact for a stabilized laser source), so the fractional errors in the screen distance z "
                       "and beam diameter D simply add.",
        "variables": [
            {"key": "z", "label": "z", "name": "Screen distance", "unit": "cm", "default": 40},
            {"key": "D", "label": "D", "name": "Illuminated beam diameter", "unit": "mm", "default": 2},
        ],
        "formula_js": "var z=vars['z']; var D=vars['D']; var lam_nm=632.8; var s=1.22*(lam_nm/1000)*(z.v*10000)/(D.v*1000); "
                       "var rel = z.lc/z.v + D.lc/D.v; return {Y: s, Yunit:'\u00b5m', dY: s*rel, pct: rel*100};",
    },
]
