/* ============================================================================
   Maximum Permissible Error Calculator — Advanced Laser & Optics Learning Lab
   A reusable widget: the student enters the measured value and least count
   (instrument resolution) for each quantity in an experiment's governing
   formula, and the widget computes the propagated maximum permissible error
   live, using the same error-propagation rule printed above it.
   ============================================================================ */
(function () {
  "use strict";

  /* CONFIGS is generated from experiment_data.py and spliced in below. */
  var CONFIGS = {
    "youngs-double-slit": {
      resultSymbol: "\u03b2",
      formulaText: "\u0394\u03b2 / \u03b2  =  \u0394\u03bb/\u03bb  +  \u0394D/D  +  \u0394d/d",
      note: "\u03b2 = \u03bbD/d is a simple product/quotient of three measured quantities, so the maximum fractional error is the sum of the fractional errors (least count / measured value) of each.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8}, {"key": "D", "label": "D", "name": "Slit-to-screen distance", "unit": "cm", "default": 100}, {"key": "d", "label": "d", "name": "Slit separation", "unit": "\u03bcm", "default": 500}],
      compute: function(vars) {
        var lam = vars["lam"];
        var D = vars["D"];
        var d = vars["d"];
        var beta = (lam.v*D.v)/d.v; var rel = lam.lc/lam.v + D.lc/D.v + d.lc/d.v; return {Y: beta, Yunit:'mm (scale-dependent; treat as relative)', dY: beta*rel, pct: rel*100};
      }
    },
    "slit-diffraction": {
      resultSymbol: "(a+b)",
      formulaText: "\u0394(a+b) / (a+b)  =  \u0394\u03bb/\u03bb  +  cot\u03b8 \u00b7 \u0394\u03b8",
      note: "From (a+b) sin\u03b8 = n\u03bb, differentiating gives a cot\u03b8 term for the angle uncertainty in addition to the wavelength's fractional error.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8}, {"key": "theta", "label": "\u03b8", "name": "Diffraction angle", "unit": "\u00b0", "default": 20}],
      compute: function(vars) {
        var lam = vars["lam"];
        var theta = vars["theta"];
        var th = theta.v*Math.PI/180; var dth = theta.lc*Math.PI/180; var rel = lam.lc/lam.v + (Math.cos(th)/Math.sin(th))*dth; var ab = lam.v/Math.sin(th); return {Y: ab, Yunit:'nm (arbitrary order n=1)', dY: ab*rel, pct: rel*100};
      }
    },
    "polarization-malus": {
      resultSymbol: "I",
      formulaText: "\u0394I / I  =  \u0394I\u2080/I\u2080  +  2 tan\u03b8 \u00b7 \u0394\u03b8",
      note: "I = I\u2080cos\u00b2\u03b8, so d(ln I) = d(ln I\u2080) \u2212 2 tan\u03b8\u00b7d\u03b8; the angle term grows rapidly as \u03b8 \u2192 90\u00b0, so avoid taking your reading very close to the crossed-polarizer position.",
      variables: [{"key": "I0", "label": "I\u2080", "name": "Reference intensity", "unit": "%", "default": 100}, {"key": "theta", "label": "\u03b8", "name": "Analyzer angle", "unit": "\u00b0", "default": 30}],
      compute: function(vars) {
        var I0 = vars["I0"];
        var theta = vars["theta"];
        var th = theta.v*Math.PI/180; var dth = theta.lc*Math.PI/180; var rel = I0.lc/I0.v + 2*Math.tan(th)*dth; var I = I0.v*Math.pow(Math.cos(th),2); return {Y: I, Yunit:'%', dY: I*rel, pct: rel*100};
      }
    },
    "prism-dispersion": {
      resultSymbol: "n",
      formulaText: "\u0394n  \u2248  \u00bd\u00b7cot[(A+\u03b4m)/2]\u00b7(\u0394A+\u0394\u03b4m)  +  \u00bd\u00b7cot(A/2)\u00b7\u0394A",
      note: "From n = sin[(A+\u03b4m)/2] / sin(A/2), where A is the prism apex angle and \u03b4m the angle of minimum deviation. Both are read off the same spectrometer circular scale, so use its vernier least count for both \u0394A and \u0394\u03b4m.",
      variables: [{"key": "A", "label": "A", "name": "Apex angle", "unit": "\u00b0", "default": 60, "hasLC": false}, {"key": "dm", "label": "\u03b4m", "name": "Angle of minimum deviation", "unit": "\u00b0", "default": 40, "hasLC": false}, {"key": "lc", "label": "LC", "name": "Spectrometer vernier least count", "unit": "\u00b0", "default": 0.083, "isLC": true}],
      compute: function(vars) {
        var A = vars["A"];
        var dm = vars["dm"];
        var lc = vars["lc"];
        var Ar = A.v*Math.PI/180, dmr = dm.v*Math.PI/180, lcr = lc.v*Math.PI/180; var n = Math.sin((Ar+dmr)/2)/Math.sin(Ar/2); var dn = 0.5*(1/Math.tan((Ar+dmr)/2))*(2*lcr) + 0.5*(1/Math.tan(Ar/2))*lcr; return {Y: n, Yunit:'(dimensionless)', dY: dn, pct: (dn/n)*100};
      }
    },
    "michelson-interferometer": {
      resultSymbol: "\u0394L",
      formulaText: "\u0394(\u0394L)  =  (\u03bb/2)\u00d7(fringe-counting uncertainty)  +  \u0394L\u00d7(\u0394\u03bb/\u03bb)",
      note: "\u0394L = \u0394m\u00b7\u03bb/2. The dominant error is usually miscounting fringes by \u00b11 near the start/end of a sweep, contributing \u00b1\u03bb/2 directly; the source's own spectral uncertainty adds a smaller relative term.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8, "hasLC": false}, {"key": "lamlc", "label": "\u0394\u03bb", "name": "Source spectral uncertainty", "unit": "nm", "default": 0.01, "isLC": true}, {"key": "dm", "label": "\u0394m", "name": "Fringes counted", "unit": "fringes", "default": 500, "hasLC": false}, {"key": "dmlc", "label": "\u00b1", "name": "Counting uncertainty", "unit": "fringes", "default": 1, "isLC": true}],
      compute: function(vars) {
        var lam = vars["lam"];
        var lamlc = vars["lamlc"];
        var dm = vars["dm"];
        var dmlc = vars["dmlc"];
        var DL = (dm.v*lam.v)/2; var errFromCount = (lam.v/2)*dmlc.v; var errFromLam = DL*(lamlc.v/lam.v); var dDL = errFromCount + errFromLam; return {Y: DL, Yunit:'nm', dY: dDL, pct: (dDL/DL)*100};
      }
    },
    "convex-lens-focusing": {
      resultSymbol: "r",
      formulaText: "\u0394r / r  =  \u0394\u03bb/\u03bb  +  \u0394f/f  +  \u0394D/D",
      note: "r = 1.22\u03bbf/D is a product/quotient of three measured quantities \u2014 sum the fractional (least count / value) errors of each.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 632.8}, {"key": "f", "label": "f", "name": "Focal length", "unit": "cm", "default": 10}, {"key": "D", "label": "D", "name": "Aperture diameter", "unit": "cm", "default": 2.5}],
      compute: function(vars) {
        var lam = vars["lam"];
        var f = vars["f"];
        var D = vars["D"];
        var r = 1.22*lam.v*f.v/D.v; var rel = lam.lc/lam.v + f.lc/f.v + D.lc/D.v; return {Y: r, Yunit:'nm (convert to μm by /1000)', dY: r*rel, pct: rel*100};
      }
    },
    "compound-lens-system": {
      resultSymbol: "v",
      formulaText: "\u0394v  =  v\u00b2 \u00b7 ( \u0394f/f\u00b2  +  \u0394u/u\u00b2 )",
      note: "From 1/v = 1/f + 1/u for a single lens stage, propagate the errors in the measured object distance u and the known/measured focal length f. Apply once per lens stage.",
      variables: [{"key": "u", "label": "u", "name": "Object distance", "unit": "cm", "default": 15}, {"key": "f", "label": "f", "name": "Focal length", "unit": "cm", "default": 10}],
      compute: function(vars) {
        var u = vars["u"];
        var f = vars["f"];
        var v = (f.v*u.v)/(u.v-f.v); var dv = Math.pow(v,2)*( f.lc/Math.pow(f.v,2) + u.lc/Math.pow(u.v,2) ); return {Y: v, Yunit:'cm', dY: dv, pct: (dv/Math.abs(v))*100};
      }
    },
    "photoelectric-effect": {
      resultSymbol: "V\u2080",
      formulaText: "\u0394V\u2080  =  (h\u00b7\u0394\u03bd)/e  +  \u0394\u03c6/e   ,   \u0394\u03bd/\u03bd = \u0394\u03bb/\u03bb",
      note: "V\u2080 = (h\u03bd \u2212 \u03c6)/e is an affine (not multiplicative) relation, so errors from frequency (via the wavelength selector's least count) and from the work function uncertainty simply add.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 400}, {"key": "phi", "label": "\u03c6", "name": "Work function", "unit": "eV", "default": 2.3, "hasLC": false}, {"key": "philc", "label": "\u0394\u03c6", "name": "Work function uncertainty", "unit": "eV", "default": 0.02, "isLC": true}],
      compute: function(vars) {
        var lam = vars["lam"];
        var phi = vars["phi"];
        var philc = vars["philc"];
        var c=2.998e8, h=4.1357e-15; var nu = c/(lam.v*1e-9); var dnu = nu*(lam.lc/lam.v); var V0 = h*nu - phi.v; var dV0 = h*dnu + philc.v; return {Y: V0, Yunit:'V', dY: dV0, pct: (dV0/Math.abs(V0))*100};
      }
    },
    "compton-scattering": {
      resultSymbol: "\u0394\u03bb",
      formulaText: "\u0394(\u0394\u03bb)  =  \u03bb_C \u00b7 sin\u03b8 \u00b7 \u0394\u03b8",
      note: "\u0394\u03bb = \u03bb_C(1\u2212cos\u03b8); differentiating with respect to the scattering angle gives this term. The Compton wavelength \u03bb_C is a fundamental constant with negligible uncertainty.",
      variables: [{"key": "theta", "label": "\u03b8", "name": "Scattering angle", "unit": "\u00b0", "default": 90}, {"key": "thetalc", "label": "\u0394\u03b8", "name": "Goniometer least count", "unit": "\u00b0", "default": 0.5, "isLC": true}],
      compute: function(vars) {
        var theta = vars["theta"];
        var thetalc = vars["thetalc"];
        var lamC = 2.426; var th = theta.v*Math.PI/180, dth = theta.lc*Math.PI/180; var dlam = lamC*(1-Math.cos(th)); var ddlam = lamC*Math.sin(th)*dth; return {Y: dlam, Yunit:'pm', dY: ddlam, pct: (ddlam/dlam)*100};
      }
    },
    "single-photon-double-slit": {
      resultSymbol: "N",
      formulaText: "\u0394N  =  \u221aN     (Poisson counting statistics)     \u2192     relative error = 1/\u221aN",
      note: "This experiment is a qualitative demonstration, not an instrumental measurement \u2014 its natural 'error' is the statistical counting uncertainty of accumulating discrete photon detection events, which shrinks as more photons are collected.",
      variables: [{"key": "N", "label": "N", "name": "Total photons detected", "unit": "counts", "default": 2500, "hasLC": false}],
      compute: function(vars) {
        var N = vars["N"];
        var dN = Math.sqrt(N.v); return {Y: N.v, Yunit:'counts', dY: dN, pct: (dN/N.v)*100};
      }
    },
    "coherence": {
      resultSymbol: "L_c",
      formulaText: "\u0394L_c / L_c  =  \u0394(\u0394\u03bd) / \u0394\u03bd",
      note: "L_c = c/\u0394\u03bd (c is exact), so the fractional error in coherence length equals the fractional error in your measurement of the source's spectral linewidth.",
      variables: [{"key": "dnu", "label": "\u0394\u03bd", "name": "Spectral linewidth", "unit": "MHz", "default": 1.0, "hasLC": false}, {"key": "dnulc", "label": "\u0394(\u0394\u03bd)", "name": "Linewidth measurement uncertainty", "unit": "MHz", "default": 0.05, "isLC": true}],
      compute: function(vars) {
        var dnu = vars["dnu"];
        var dnulc = vars["dnulc"];
        var c=2.998e8; var Lc = c/(dnu.v*1e6); var rel = dnulc.v/dnu.v; return {Y: Lc, Yunit:'m', dY: Lc*rel, pct: rel*100};
      }
    },
    "directionality-beam-quality": {
      resultSymbol: "D_spot",
      formulaText: "\u0394D_spot  =  \u0394D\u2080  +  L\u00b7\u0394\u03b8_div  +  \u03b8_div\u00b7\u0394L",
      note: "D_spot(L) = D\u2080 + \u03b8_div\u00b7L is a sum, so absolute (not fractional) errors add directly, each weighted by the relevant partial derivative.",
      variables: [{"key": "D0", "label": "D\u2080", "name": "Initial beam diameter", "unit": "mm", "default": 2}, {"key": "thetadiv", "label": "\u03b8_div", "name": "Angular divergence", "unit": "mrad", "default": 1.5}, {"key": "L", "label": "L", "name": "Propagation distance", "unit": "m", "default": 5}],
      compute: function(vars) {
        var D0 = vars["D0"];
        var thetadiv = vars["thetadiv"];
        var L = vars["L"];
        var Dspot = D0.v + thetadiv.v*L.v; var dDspot = D0.lc + L.v*thetadiv.lc + thetadiv.v*L.lc; return {Y: Dspot, Yunit:'mm', dY: dDspot, pct: (dDspot/Dspot)*100};
      }
    },
    "monochromaticity-purity": {
      resultSymbol: "\u0394\u03bb/\u03bb",
      formulaText: "\u0394(purity) / purity  =  \u0394W/W  +  \u0394\u03bb/\u03bb",
      note: "purity = W/\u03bb, where W is the measured spectral linewidth. Sum the fractional error in the linewidth measurement and in the central-wavelength measurement.",
      variables: [{"key": "W", "label": "W", "name": "Spectral linewidth", "unit": "nm", "default": 0.001}, {"key": "lam", "label": "\u03bb", "name": "Central wavelength", "unit": "nm", "default": 632.8}],
      compute: function(vars) {
        var W = vars["W"];
        var lam = vars["lam"];
        var purity = W.v/lam.v; var rel = W.lc/W.v + lam.lc/lam.v; return {Y: purity, Yunit:'(dimensionless)', dY: purity*rel, pct: rel*100};
      }
    },
    "wavelength-explorer": {
      resultSymbol: "E",
      formulaText: "\u0394E / E  =  \u0394\u03bb / \u03bb",
      note: "E = hc/\u03bb (h, c exact), so the fractional error in photon energy equals the fractional error in the wavelength measurement/setting.",
      variables: [{"key": "lam", "label": "\u03bb", "name": "Wavelength", "unit": "nm", "default": 500}],
      compute: function(vars) {
        var lam = vars["lam"];
        var hc_eVnm = 1239.84; var E = hc_eVnm/lam.v; var rel = lam.lc/lam.v; return {Y: E, Yunit:'eV', dY: E*rel, pct: rel*100};
      }
    },
    "laser-doppler-vibrometry": {
      resultSymbol: "v_max",
      formulaText: "\u0394v_max / v_max  =  \u0394A/A  +  \u0394f/f",
      note: "v_max = A\u03c9 = A(2\u03c0f) is a simple product of the vibration amplitude and (angular) frequency, so their fractional errors simply add.",
      variables: [{"key": "A", "label": "A", "name": "Vibration amplitude", "unit": "\u00b5m", "default": 10}, {"key": "f", "label": "f", "name": "Vibration frequency", "unit": "Hz", "default": 100}],
      compute: function(vars) {
        var A=vars['A'], f=vars['f']; var omega=2*Math.PI*f.v; var vmax=(A.v/1000)*omega; var rel = A.lc/A.v + f.lc/f.v; return {Y: vmax, Yunit:'mm/s', dY: vmax*rel, pct: rel*100};
      }
    },
    "optical-fiber-na-attenuation": {
      resultSymbol: "NA",
      formulaText: "\u0394(NA) \u2248 (n\u2081\u0394n\u2081 + n\u2082\u0394n\u2082) / NA",
      note: "NA = \u221a(n\u2081\u00b2\u2212n\u2082\u00b2); since NA is a square root of a difference of squares, its absolute error is dominated by whichever refractive index (core or cladding) carries the larger measurement uncertainty, weighted by that index's own value.",
      variables: [{"key": "n1", "label": "n\u2081", "name": "Core refractive index", "unit": "(dimensionless)", "default": 1.48}, {"key": "n2", "label": "n\u2082", "name": "Cladding refractive index", "unit": "(dimensionless)", "default": 1.46}],
      compute: function(vars) {
        var n1=vars['n1'], n2=vars['n2']; var NA=Math.sqrt(Math.max(n1.v*n1.v-n2.v*n2.v,0)); var dNA=(n1.v*n1.lc+n2.v*n2.lc)/Math.max(NA,1e-6); return {Y: NA, Yunit:'(dimensionless)', dY: dNA, pct: (dNA/NA)*100};
      }
    },
    "laser-speckle-metrology": {
      resultSymbol: "s",
      formulaText: "\u0394s / s  =  \u0394z/z  +  \u0394D/D",
      note: "The speckle grain size s = 1.22\u03bbz/D is a product/quotient of measured quantities (\u03bb taken as exact for a stabilized laser source), so the fractional errors in the screen distance z and beam diameter D simply add.",
      variables: [{"key": "z", "label": "z", "name": "Screen distance", "unit": "cm", "default": 40}, {"key": "D", "label": "D", "name": "Illuminated beam diameter", "unit": "mm", "default": 2}],
      compute: function(vars) {
        var z=vars['z'], D=vars['D']; var lam_nm=632.8; var s=1.22*(lam_nm/1000)*(z.v*10000)/(D.v*1000); var rel = z.lc/z.v + D.lc/D.v; return {Y: s, Yunit:'\u00b5m', dY: s*rel, pct: rel*100};
      }
    },
  };

  function fmt(x) {
    if (x === 0) return "0";
    var ax = Math.abs(x);
    if (ax >= 1000 || ax < 0.001) return x.toExponential(3);
    return parseFloat(x.toPrecision(4)).toString();
  }

  function renderVarRow(v) {
    var row = document.createElement("div");
    row.className = "ec-row";
    var nameLabel = document.createElement("div");
    nameLabel.className = "ec-varname";
    nameLabel.innerHTML = "<b>" + v.label + "</b> &mdash; " + v.name + (v.unit ? " (" + v.unit + ")" : "");
    row.appendChild(nameLabel);

    var inputs = document.createElement("div");
    inputs.className = "ec-inputs";

    var valInput = document.createElement("input");
    valInput.type = "number";
    valInput.step = "any";
    valInput.value = v.default;
    valInput.className = "ec-input ec-input-value";
    valInput.setAttribute("data-key", v.key);
    valInput.setAttribute("data-role", "v");
    valInput.title = v.isLC ? "Value" : "Measured value";
    inputs.appendChild(valInput);

    var hasLC = v.hasLC !== false && !v.isLC;
    var lcInput = null;
    if (hasLC) {
      var lcWrap = document.createElement("span");
      lcWrap.className = "ec-lc-wrap";
      lcWrap.innerHTML = "&nbsp;&plusmn;&nbsp;";
      lcInput = document.createElement("input");
      lcInput.type = "number";
      lcInput.step = "any";
      lcInput.value = Math.max(v.default * 0.002, 0.001).toPrecision(2);
      lcInput.className = "ec-input ec-input-lc";
      lcInput.setAttribute("data-key", v.key);
      lcInput.setAttribute("data-role", "lc");
      lcInput.title = "Least count (instrument resolution)";
      lcWrap.appendChild(lcInput);
      inputs.appendChild(lcWrap);
      var lcTag = document.createElement("span");
      lcTag.className = "ec-lc-tag";
      lcTag.textContent = "LC";
      inputs.appendChild(lcTag);
    }
    row.appendChild(inputs);
    return row;
  }

  function initOne(container) {
    var slug = container.getAttribute("data-exp");
    var cfg = CONFIGS[slug];
    if (!cfg) return;

    container.innerHTML = "";
    var formulaBox = document.createElement("div");
    formulaBox.className = "ec-formula";
    formulaBox.innerHTML = "<b>Error formula:</b> " + cfg.formulaText;
    container.appendChild(formulaBox);

    var noteBox = document.createElement("div");
    noteBox.className = "ec-note";
    noteBox.textContent = cfg.note;
    container.appendChild(noteBox);

    var form = document.createElement("div");
    form.className = "ec-form";
    cfg.variables.forEach(function (v) {
      form.appendChild(renderVarRow(v));
    });
    container.appendChild(form);

    var resultBox = document.createElement("div");
    resultBox.className = "ec-result";
    container.appendChild(resultBox);

    function recompute() {
      var vars = {};
      cfg.variables.forEach(function (v) {
        var valEl = form.querySelector('.ec-input-value[data-key="' + v.key + '"]');
        var lcEl = form.querySelector('.ec-input-lc[data-key="' + v.key + '"]');
        var val = parseFloat(valEl.value);
        var lc = lcEl ? parseFloat(lcEl.value) : 0;
        vars[v.key] = { v: val, lc: lc };
      });
      try {
        var out = cfg.compute(vars);
        resultBox.innerHTML =
          "<div class='ec-result-main'>" + cfg.resultSymbol + " = " + fmt(out.Y) +
          " &nbsp;&plusmn;&nbsp; " + fmt(out.dY) + " " + (out.Yunit || "") + "</div>" +
          "<div class='ec-result-pct'>Maximum permissible error &asymp; " + out.pct.toFixed(2) + " %</div>";
      } catch (e) {
        resultBox.innerHTML = "<div class='ec-result-error'>Check your inputs (" + e.message + ")</div>";
      }
    }

    form.addEventListener("input", recompute);
    recompute();
  }

  function initAll() {
    document.querySelectorAll(".error-calc[data-exp]").forEach(initOne);
  }

  if (document.readyState === "complete" || document.readyState === "interactive") {
    setTimeout(initAll, 30);
  } else {
    document.addEventListener("DOMContentLoaded", function () { setTimeout(initAll, 30); });
  }
  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(function () { setTimeout(initAll, 30); });
  }
})();
