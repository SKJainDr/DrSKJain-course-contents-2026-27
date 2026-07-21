/* ============================================================================
   Maximum Permissible Error Calculator — Advanced Electricity & Magnetism
   Learning Lab. A reusable widget: the student enters the measured value
   and least count (instrument resolution) for each quantity in an
   experiment's governing formula, and the widget computes the propagated
   maximum permissible error live, using the same error-propagation rule
   printed above it.
   ============================================================================ */
(function () {
  "use strict";

  /* CONFIGS is generated from em_data.py and spliced in below. */
  var CONFIGS = {
    "coulombs-law": {
      resultSymbol: "F",
      formulaText: "ΔF/F = Δq₁/q₁ + Δq₂/q₂ + 2Δr/r",
      note: "F ∝ q₁q₂/r² is a product/quotient of measured quantities, with r entering squared, so its fractional error carries a factor of 2.",
      variables: [{"key": "q1", "label": "q₁", "name": "Charge 1", "unit": "nC", "default": 10}, {"key": "q2", "label": "q₂", "name": "Charge 2", "unit": "nC", "default": 10}, {"key": "r", "label": "r", "name": "Separation", "unit": "cm", "default": 10}],
      compute: function(vars) {
        var q1 = vars["q1"];
        var q2 = vars["q2"];
        var r = vars["r"];
        var k=8.988; var F=k*q1.v*q2.v/(r.v*r.v); var rel=q1.lc/q1.v+q2.lc/q2.v+2*r.lc/r.v; return {Y:F,Yunit:'×10⁻⁹ N (scaled)',dY:F*rel,pct:rel*100};
      }
    },
    "dipole-field-potential": {
      resultSymbol: "E_axial",
      formulaText: "ΔE/E = Δq/q + Δ(2a)/(2a) + 3Δr/r",
      note: "E_axial = 2kp/r³ with p=q·(2a) varies as r⁻³, so its fractional uncertainty carries a factor of 3 from r.",
      variables: [{"key": "q", "label": "q", "name": "Charge magnitude", "unit": "nC", "default": 5}, {"key": "a2", "label": "2a", "name": "Charge separation", "unit": "cm", "default": 4}, {"key": "r", "label": "r", "name": "Probe distance", "unit": "cm", "default": 20}],
      compute: function(vars) {
        var q = vars["q"];
        var a2 = vars["a2"];
        var r = vars["r"];
        var k=8.988e9; var p=q.v*1e-9*a2.v*1e-2; var rm=r.v*1e-2; var E=2*k*p/(rm*rm*rm); var rel=q.lc/q.v+a2.lc/a2.v+3*r.lc/r.v; return {Y:E,Yunit:'N/C',dY:E*rel,pct:rel*100};
      }
    },
    "gauss-law-flux": {
      resultSymbol: "Φ",
      formulaText: "ΔΦ/Φ = ΔQ_enc/Q_enc",
      note: "Since Φ = Q_enc/ε₀ with ε₀ an exact constant, the fractional error in flux equals the fractional error in the enclosed charge measurement.",
      variables: [{"key": "Qenc", "label": "Q_enc", "name": "Enclosed charge", "unit": "nC", "default": 10}],
      compute: function(vars) {
        var Qenc = vars["Qenc"];
        var eps=8.854; var phi=Qenc.v/eps*1000; var rel=Qenc.lc/Qenc.v; return {Y:phi,Yunit:'N·m²/C (scaled)',dY:phi*rel,pct:rel*100};
      }
    },
    "parallel-plate-capacitor": {
      resultSymbol: "C",
      formulaText: "ΔC/C = Δεr/εr + ΔA/A + Δd/d",
      note: "C = εrε₀A/d is a product/quotient of three measured quantities, so fractional errors add.",
      variables: [{"key": "epsr", "label": "εr", "name": "Dielectric constant", "unit": "", "default": 5}, {"key": "A", "label": "A", "name": "Area", "unit": "cm²", "default": 200}, {"key": "d", "label": "d", "name": "Separation", "unit": "mm", "default": 2}],
      compute: function(vars) {
        var epsr = vars["epsr"];
        var A = vars["A"];
        var d = vars["d"];
        var eps0=8.854e-12; var Am2=A.v*1e-4; var dm=d.v*1e-3; var C=epsr.v*eps0*Am2/dm*1e12; var rel=epsr.lc/epsr.v+A.lc/A.v+d.lc/d.v; return {Y:C,Yunit:'pF',dY:C*rel,pct:rel*100};
      }
    },
    "conductors-charge-distribution": {
      resultSymbol: "V",
      formulaText: "ΔV/V = Δrate/rate + Δt/t + ΔR/R",
      note: "V = kQ/R with Q = rate×t (charging rate times time), so fractional errors in rate, time and R all add.",
      variables: [{"key": "rate", "label": "rate", "name": "Belt charging rate", "unit": "nC/s", "default": 5}, {"key": "time", "label": "t", "name": "Charging time", "unit": "s", "default": 20}, {"key": "R", "label": "R", "name": "Dome radius", "unit": "cm", "default": 25}],
      compute: function(vars) {
        var rate = vars["rate"];
        var time = vars["time"];
        var R = vars["R"];
        var k=8.988e9; var Qc=rate.v*time.v*1e-9; var Rm=R.v*1e-2; var V=k*Qc/Rm/1000; var rel=rate.lc/rate.v+time.lc/time.v+R.lc/R.v; return {Y:V,Yunit:'kV',dY:V*rel,pct:rel*100};
      }
    },
    "biot-savart-wire": {
      resultSymbol: "B",
      formulaText: "ΔB/B = ΔI/I + Δa/a",
      note: "For the infinite-wire limit B = μ₀I/2πa, a simple quotient, so fractional errors in I and a add.",
      variables: [{"key": "I", "label": "I", "name": "Current", "unit": "A", "default": 2}, {"key": "a", "label": "a", "name": "Distance", "unit": "cm", "default": 10}],
      compute: function(vars) {
        var I = vars["I"];
        var a = vars["a"];
        var mu0=4*Math.PI*1e-7; var am=a.v*1e-2; var B=mu0*I.v/(2*Math.PI*am)*1e5; var rel=I.lc/I.v+a.lc/a.v; return {Y:B,Yunit:'×10⁻⁵ T',dY:B*rel,pct:rel*100};
      }
    },
    "circular-coil-helmholtz": {
      resultSymbol: "B₀",
      formulaText: "ΔB₀/B₀ = ΔN/N + ΔI/I + ΔR/R",
      note: "B₀ = μ₀NI/2R at the coil centre is a simple product/quotient, so fractional errors add.",
      variables: [{"key": "N", "label": "N", "name": "Turns", "unit": "", "default": 100}, {"key": "I", "label": "I", "name": "Current", "unit": "A", "default": 1}, {"key": "R", "label": "R", "name": "Radius", "unit": "cm", "default": 10}],
      compute: function(vars) {
        var N = vars["N"];
        var I = vars["I"];
        var R = vars["R"];
        var mu0=4*Math.PI*1e-7; var Rm=R.v*1e-2; var B=mu0*N.v*I.v/(2*Rm)*1e4; var rel=N.lc/N.v+I.lc/I.v+R.lc/R.v; return {Y:B,Yunit:'×10⁻⁴ T',dY:B*rel,pct:rel*100};
      }
    },
    "ampere-law-solenoid-toroid": {
      resultSymbol: "B",
      formulaText: "ΔB/B = Δn/n + ΔI/I",
      note: "B = μ₀nI is a simple product, so fractional errors in n and I add directly.",
      variables: [{"key": "n", "label": "n", "name": "Turns density", "unit": "turns/cm", "default": 30}, {"key": "I", "label": "I", "name": "Current", "unit": "A", "default": 1}],
      compute: function(vars) {
        var n = vars["n"];
        var I = vars["I"];
        var mu0=4*Math.PI*1e-7; var ncm=n.v*100; var B=mu0*ncm*I.v*1000; var rel=n.lc/n.v+I.lc/I.v; return {Y:B,Yunit:'×10⁻³ T',dY:B*rel,pct:rel*100};
      }
    },
    "force-parallel-conductors": {
      resultSymbol: "F/L",
      formulaText: "Δ(F/L)/(F/L) = ΔI₁/I₁ + ΔI₂/I₂ + Δd/d",
      note: "F/L = μ₀I₁I₂/2πd is a product/quotient of three measured quantities.",
      variables: [{"key": "I1", "label": "I₁", "name": "Current 1", "unit": "A", "default": 5}, {"key": "I2", "label": "I₂", "name": "Current 2", "unit": "A", "default": 5}, {"key": "d", "label": "d", "name": "Separation", "unit": "cm", "default": 5}],
      compute: function(vars) {
        var I1 = vars["I1"];
        var I2 = vars["I2"];
        var d = vars["d"];
        var mu0=4*Math.PI*1e-7; var dm=d.v*1e-2; var F=mu0*I1.v*I2.v/(2*Math.PI*dm)*1e5; var rel=I1.lc/I1.v+I2.lc/I2.v+d.lc/d.v; return {Y:F,Yunit:'×10⁻⁵ N/m',dY:F*rel,pct:rel*100};
      }
    },
    "faraday-induction": {
      resultSymbol: "ε",
      formulaText: "Δε/ε = ΔN/N + ΔB_max/B_max + Δv/v",
      note: "For a magnet swept through at speed v, peak EMF scales with N, the field's peak value and its rate of change (∝ v), so fractional errors add.",
      variables: [{"key": "N", "label": "N", "name": "Turns", "unit": "", "default": 100}, {"key": "Bmax", "label": "B_max", "name": "Peak field", "unit": "mT", "default": 30}, {"key": "speed", "label": "v", "name": "Speed", "unit": "cm/s", "default": 10}],
      compute: function(vars) {
        var N = vars["N"];
        var Bmax = vars["Bmax"];
        var speed = vars["speed"];
        var eps=N.v*Bmax.v*speed.v/1000; var rel=N.lc/N.v+Bmax.lc/Bmax.v+speed.lc/speed.v; return {Y:eps,Yunit:'mV (model units)',dY:eps*rel,pct:rel*100};
      }
    },
    "motional-emf-lenz": {
      resultSymbol: "ε",
      formulaText: "Δε/ε = ΔB/B + ΔL/L + Δv/v",
      note: "ε = BLv is a simple product of three measured quantities.",
      variables: [{"key": "B", "label": "B", "name": "Field", "unit": "mT", "default": 100}, {"key": "L", "label": "L", "name": "Rail separation", "unit": "cm", "default": 20}, {"key": "v", "label": "v", "name": "Velocity", "unit": "m/s", "default": 1}],
      compute: function(vars) {
        var B = vars["B"];
        var L = vars["L"];
        var v = vars["v"];
        var Bt=B.v*1e-3; var Lm=L.v*1e-2; var eps=Bt*Lm*v.v*1000; var rel=B.lc/B.v+L.lc/L.v+v.lc/v.v; return {Y:eps,Yunit:'mV',dY:eps*rel,pct:rel*100};
      }
    },
    "rc-rl-transients": {
      resultSymbol: "τ",
      formulaText: "Δτ/τ = ΔR/R + ΔC/C  (RC circuit)",
      note: "τ = RC is a simple product, so fractional errors in R and C add directly.",
      variables: [{"key": "R", "label": "R", "name": "Resistance", "unit": "kΩ", "default": 10}, {"key": "C", "label": "C", "name": "Capacitance", "unit": "μF", "default": 10}],
      compute: function(vars) {
        var R = vars["R"];
        var C = vars["C"];
        var tau=R.v*1000*C.v*1e-6*1000; var rel=R.lc/R.v+C.lc/C.v; return {Y:tau,Yunit:'ms',dY:tau*rel,pct:rel*100};
      }
    },
    "lcr-resonance": {
      resultSymbol: "f₀",
      formulaText: "Δf₀/f₀ = ½(ΔL/L + ΔC/C)",
      note: "f₀ = 1/(2π√LC) involves a square root of the product LC, halving the summed fractional errors.",
      variables: [{"key": "L", "label": "L", "name": "Inductance", "unit": "mH", "default": 100}, {"key": "C", "label": "C", "name": "Capacitance", "unit": "μF", "default": 1}],
      compute: function(vars) {
        var L = vars["L"];
        var C = vars["C"];
        var Lh=L.v*1e-3; var Cf=C.v*1e-6; var f0=1/(2*Math.PI*Math.sqrt(Lh*Cf)); var rel=0.5*(L.lc/L.v+C.lc/C.v); return {Y:f0,Yunit:'Hz',dY:f0*rel,pct:rel*100};
      }
    },
    "maxwell-plane-waves": {
      resultSymbol: "B₀",
      formulaText: "ΔB₀/B₀ = ΔE₀/E₀",
      note: "Since B₀ = E₀/c with c an exact constant, the fractional error in B₀ equals the fractional error in the measured E₀.",
      variables: [{"key": "E0", "label": "E₀", "name": "E amplitude", "unit": "V/m", "default": 30}],
      compute: function(vars) {
        var E0 = vars["E0"];
        var c=2.998e8; var B0=E0.v/c*1e9; var rel=E0.lc/E0.v; return {Y:B0,Yunit:'nT',dY:B0*rel,pct:rel*100};
      }
    },
    "wave-propagation-media-skindepth": {
      resultSymbol: "δ",
      formulaText: "Δδ/δ = ½(Δf/f + Δσ/σ)",
      note: "δ ∝ 1/√(fσ), so the fractional errors in f and σ are each halved before summing.",
      variables: [{"key": "freq", "label": "f", "name": "Frequency", "unit": "MHz", "default": 100}, {"key": "sigma", "label": "σ", "name": "Conductivity", "unit": "MS/m", "default": 6}],
      compute: function(vars) {
        var freq = vars["freq"];
        var sigma = vars["sigma"];
        var w=2*Math.PI*freq.v*1e6; var mu0=4*Math.PI*1e-7; var sig=sigma.v*1e6; var delta=Math.sqrt(2/(w*mu0*sig))*1e6; var rel=0.5*(freq.lc/freq.v+sigma.lc/sigma.v); return {Y:delta,Yunit:'μm',dY:delta*rel,pct:rel*100};
      }
    },
    "reflection-refraction-brewster": {
      resultSymbol: "θ_B",
      formulaText: "Δθ_B ≈ [1/(1+(n₂/n₁)²)]·(n₂/n₁)·(Δn₂/n₂ + Δn₁/n₁)",
      note: "Obtained by differentiating θ_B = arctan(n₂/n₁) with respect to the ratio n₂/n₁.",
      variables: [{"key": "n1", "label": "n₁", "name": "n1", "unit": "", "default": 1}, {"key": "n2", "label": "n₂", "name": "n2", "unit": "", "default": 1.5}],
      compute: function(vars) {
        var n1 = vars["n1"];
        var n2 = vars["n2"];
        var ratio=n2.v/n1.v; var thB=Math.atan(ratio)*180/Math.PI; var relratio=n2.lc/n2.v+n1.lc/n1.v; var dthB=(1/(1+ratio*ratio))*ratio*relratio*180/Math.PI; return {Y:thB,Yunit:'°',dY:dthB,pct:(dthB/thB)*100};
      }
    },
    "dielectric-polarization-clausius-mossotti": {
      resultSymbol: "εr",
      formulaText: "via Clausius–Mossotti; Δεr estimated numerically from ΔN/N + Δα/α",
      note: "εr is a nonlinear function of Nα, so its propagated error is evaluated numerically from the fractional errors of N and α rather than a simple closed form.",
      variables: [{"key": "N", "label": "N", "name": "Number density", "unit": "×10²⁸ m⁻³", "default": 20}, {"key": "alpha", "label": "α", "name": "Polarizability", "unit": "×10⁻⁴⁰ C·m²/V", "default": 15}],
      compute: function(vars) {
        var N = vars["N"];
        var alpha = vars["alpha"];
        var eps0=8.854; var x=(N.v*1e28*alpha.v*1e-40)/(3*eps0*1e-12); var epsr=(1+2*x)/(1-x); var rel=N.lc/N.v+alpha.lc/alpha.v; return {Y:epsr,Yunit:'(dimensionless)',dY:epsr*rel*0.3,pct:rel*30};
      }
    },
    "magnetic-hysteresis-bh-curve": {
      resultSymbol: "H_c",
      formulaText: "H_c ≈ 0.15×H_max (model estimate); ΔH_c/H_c = ΔH_max/H_max",
      note: "In this model, coercivity is estimated as a fixed fraction of the peak applied field; its uncertainty tracks the peak-field setting's fractional uncertainty.",
      variables: [{"key": "Hmax", "label": "H_max", "name": "Peak applied field", "unit": "A/m", "default": 500}],
      compute: function(vars) {
        var Hmax = vars["Hmax"];
        var Hc=0.15*Hmax.v; var rel=Hmax.lc/Hmax.v; return {Y:Hc,Yunit:'A/m',dY:Hc*rel,pct:rel*100};
      }
    }
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
