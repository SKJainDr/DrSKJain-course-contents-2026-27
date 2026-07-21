/* ============================================================================
   3-D Apparatus Viewer — Advanced Laser & Optics Learning Lab
   A lightweight, reusable Three.js "optical bench" schematic renderer.
   Renders a simplified 3-D layout of the apparatus for each experiment so
   students can see how the components are physically arranged in space,
   complementing the 2-D graphs/animations in the interactive simulator.
   ============================================================================ */
(function () {
  "use strict";

  var COLORS = {
    bench: 0x0b173a,
    benchTop: 0x142b66,
    grid: 0x33529e,
    source: 0xa8452f,
    beam: 0xff5a3c,
    beamDim: 0xc9a227,
    lens: 0xbfe3ff,
    lensRim: 0x1f3a93,
    plate: 0x334155,
    screen: 0xf4f1e9,
    screenGlow: 0xfff6da,
    mirror: 0xd7e6ff,
    beamsplitter: 0x9fc6ff,
    gold: 0xc9a227,
    prism: 0xdfeeff,
    label: 0x0b173a
  };

  function makeLabelSprite(text) {
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    var fontSize = 40;
    ctx.font = "bold " + fontSize + "px Inter, Helvetica, sans-serif";
    var metrics = ctx.measureText(text);
    var padX = 22, padY = 14;
    canvas.width = Math.ceil(metrics.width) + padX * 2;
    canvas.height = fontSize + padY * 2;
    ctx.font = "bold " + fontSize + "px Inter, Helvetica, sans-serif";
    // background chip
    ctx.fillStyle = "rgba(11,23,58,0.92)";
    roundRect(ctx, 0, 0, canvas.width, canvas.height, 12);
    ctx.fill();
    ctx.strokeStyle = "#C9A227";
    ctx.lineWidth = 3;
    roundRect(ctx, 1.5, 1.5, canvas.width - 3, canvas.height - 3, 12);
    ctx.stroke();
    ctx.fillStyle = "#FFFFFF";
    ctx.textBaseline = "middle";
    ctx.fillText(text, padX, canvas.height / 2 + 2);

    var texture = new THREE.CanvasTexture(canvas);
    texture.minFilter = THREE.LinearFilter;
    var material = new THREE.SpriteMaterial({ map: texture, depthTest: false, transparent: true });
    var sprite = new THREE.Sprite(material);
    var scale = 0.011;
    sprite.scale.set(canvas.width * scale, canvas.height * scale, 1);
    sprite.renderOrder = 999;
    return sprite;
  }

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  function group(x, z) {
    var g = new THREE.Group();
    g.position.set(x, 0, z || 0);
    return g;
  }

  function addLabel(g, text, height) {
    var s = makeLabelSprite(text);
    s.position.set(0, height || 2.1, 0);
    g.add(s);
  }

  /* ---- component builders ---- */
  function buildSource(x, label, colorHex) {
    var g = group(x);
    var body = new THREE.Mesh(
      new THREE.BoxGeometry(0.9, 0.7, 0.7),
      new THREE.MeshStandardMaterial({ color: colorHex || COLORS.source, metalness: 0.3, roughness: 0.5 })
    );
    body.position.y = 0.45;
    g.add(body);
    var nozzle = new THREE.Mesh(
      new THREE.CylinderGeometry(0.09, 0.09, 0.3, 16),
      new THREE.MeshStandardMaterial({ color: COLORS.gold, metalness: 0.6, roughness: 0.3 })
    );
    nozzle.rotation.z = Math.PI / 2;
    nozzle.position.set(0.6, 0.45, 0);
    g.add(nozzle);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildLens(x, label, wide) {
    var g = group(x);
    var geo = new THREE.SphereGeometry(0.62, 24, 24);
    var mat = new THREE.MeshPhysicalMaterial({
      color: COLORS.lens, transparent: true, opacity: 0.45, roughness: 0.05
    });
    var lens = new THREE.Mesh(geo, mat);
    lens.scale.set(wide ? 0.34 : 0.22, 0.62, 0.62);
    lens.position.y = 0.55;
    g.add(lens);
    var rim = new THREE.Mesh(
      new THREE.TorusGeometry(0.6, 0.035, 8, 32),
      new THREE.MeshStandardMaterial({ color: COLORS.lensRim, metalness: 0.5, roughness: 0.4 })
    );
    rim.rotation.y = Math.PI / 2;
    rim.position.y = 0.55;
    g.add(rim);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildSlitPlate(x, label, nSlits) {
    var g = group(x);
    var plateW = 1.3, plateH = 1.1;
    var n = nSlits || 1;
    var mat = new THREE.MeshStandardMaterial({ color: COLORS.plate, metalness: 0.4, roughness: 0.6 });
    var totalGaps = n * 0.14;
    var barW = (plateW - totalGaps) / (n + 1);
    var cursor = -plateW / 2;
    for (var j = 0; j <= n; j++) {
      var barMesh = new THREE.Mesh(new THREE.BoxGeometry(0.06, plateH, barW), mat);
      barMesh.position.set(0, 0.55, cursor + barW / 2);
      g.add(barMesh);
      cursor += barW + 0.14;
    }
    addLabel(g, label, 1.35);
    return g;
  }

  function buildScreen(x, label, glow) {
    var g = group(x);
    var screen = new THREE.Mesh(
      new THREE.PlaneGeometry(1.6, 1.3),
      new THREE.MeshStandardMaterial({
        color: glow ? COLORS.screenGlow : COLORS.screen, side: THREE.DoubleSide,
        emissive: glow ? 0x8a6a10 : 0x000000, emissiveIntensity: glow ? 0.25 : 0
      })
    );
    screen.rotation.y = Math.PI / 2;
    screen.position.y = 0.65;
    g.add(screen);
    var frame = new THREE.Mesh(
      new THREE.BoxGeometry(0.06, 1.36, 1.66),
      new THREE.MeshStandardMaterial({ color: COLORS.lensRim, metalness: 0.5, roughness: 0.4 })
    );
    frame.position.y = 0.65;
    g.add(frame);
    addLabel(g, label, 1.5);
    return g;
  }

  function buildMirror(x, label, angleDeg) {
    var g = group(x);
    var mirror = new THREE.Mesh(
      new THREE.BoxGeometry(0.05, 1.0, 1.0),
      new THREE.MeshStandardMaterial({ color: COLORS.mirror, metalness: 0.9, roughness: 0.15 })
    );
    mirror.position.y = 0.6;
    mirror.rotation.y = ((angleDeg || 45) * Math.PI) / 180;
    g.add(mirror);
    addLabel(g, label, 1.3);
    return g;
  }

  function buildBeamsplitter(x, label) {
    var g = group(x);
    var bs = new THREE.Mesh(
      new THREE.BoxGeometry(0.04, 0.95, 0.95),
      new THREE.MeshPhysicalMaterial({ color: COLORS.beamsplitter, transparent: true, opacity: 0.55, metalness: 0.3, roughness: 0.2 })
    );
    bs.position.y = 0.6;
    bs.rotation.y = Math.PI / 4;
    g.add(bs);
    addLabel(g, label, 1.3);
    return g;
  }

  function buildPrism(x, label) {
    var g = group(x);
    var shape = new THREE.Shape();
    shape.moveTo(-0.5, 0);
    shape.lineTo(0.5, 0);
    shape.lineTo(0, 0.8);
    shape.lineTo(-0.5, 0);
    var geo = new THREE.ExtrudeGeometry(shape, { depth: 0.8, bevelEnabled: false });
    geo.center();
    var mat = new THREE.MeshPhysicalMaterial({ color: COLORS.prism, transparent: true, opacity: 0.55, roughness: 0.05 });
    var mesh = new THREE.Mesh(geo, mat);
    mesh.rotation.x = -Math.PI / 2;
    mesh.position.y = 0.4;
    g.add(mesh);
    addLabel(g, label, 1.3);
    return g;
  }

  function buildPolarizer(x, label) {
    var g = group(x);
    var disc = new THREE.Mesh(
      new THREE.CylinderGeometry(0.62, 0.62, 0.05, 32),
      new THREE.MeshStandardMaterial({ color: COLORS.beamsplitter, transparent: true, opacity: 0.4, metalness: 0.2, roughness: 0.3 })
    );
    disc.rotation.z = Math.PI / 2;
    disc.position.y = 0.55;
    g.add(disc);
    var rim = new THREE.Mesh(
      new THREE.TorusGeometry(0.62, 0.04, 8, 32),
      new THREE.MeshStandardMaterial({ color: COLORS.gold, metalness: 0.6, roughness: 0.3 })
    );
    rim.rotation.y = Math.PI / 2;
    rim.position.y = 0.55;
    g.add(rim);
    // axis tick
    var tick = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.7, 0.04), new THREE.MeshStandardMaterial({ color: COLORS.gold }));
    tick.position.set(0, 0.55, 0);
    g.add(tick);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildVacuumTube(x, label) {
    var g = group(x);
    var tube = new THREE.Mesh(
      new THREE.CylinderGeometry(0.5, 0.5, 1.4, 24, 1, true),
      new THREE.MeshPhysicalMaterial({ color: 0xbfe3ff, transparent: true, opacity: 0.25, side: THREE.DoubleSide, roughness: 0.1 })
    );
    tube.rotation.z = Math.PI / 2;
    tube.position.y = 0.55;
    g.add(tube);
    var cathode = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.7, 0.7),
      new THREE.MeshStandardMaterial({ color: COLORS.source, metalness: 0.5 }));
    cathode.position.set(-0.55, 0.55, 0);
    g.add(cathode);
    var anode = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.7, 0.7),
      new THREE.MeshStandardMaterial({ color: COLORS.lensRim, metalness: 0.5 }));
    anode.position.set(0.55, 0.55, 0);
    g.add(anode);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildAtomTarget(x, label) {
    var g = group(x);
    var nucleus = new THREE.Mesh(new THREE.SphereGeometry(0.18, 16, 16),
      new THREE.MeshStandardMaterial({ color: COLORS.source, metalness: 0.4, roughness: 0.4 }));
    nucleus.position.y = 0.6;
    g.add(nucleus);
    var orbitR = 0.45;
    var electron = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 12),
      new THREE.MeshStandardMaterial({ color: COLORS.gold, emissive: 0x6b5410, emissiveIntensity: 0.4 }));
    electron.position.set(orbitR, 0.6, 0);
    g.add(electron);
    var ring = new THREE.Mesh(new THREE.TorusGeometry(orbitR, 0.008, 6, 40),
      new THREE.MeshBasicMaterial({ color: COLORS.gold, transparent: true, opacity: 0.5 }));
    ring.rotation.x = Math.PI / 2.3;
    ring.position.y = 0.6;
    g.add(ring);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildPhotoPlate(x, label) {
    var g = group(x);
    var plate = new THREE.Mesh(new THREE.BoxGeometry(0.06, 1.2, 1.2),
      new THREE.MeshStandardMaterial({ color: 0x5b4a12, metalness: 0.3, roughness: 0.6 }));
    plate.position.y = 0.6;
    g.add(plate);
    var sheen = new THREE.Mesh(new THREE.PlaneGeometry(1.1, 1.1),
      new THREE.MeshStandardMaterial({ color: COLORS.gold, transparent: true, opacity: 0.25, side: THREE.DoubleSide }));
    sheen.rotation.y = Math.PI / 2;
    sheen.position.set(0.04, 0.6, 0);
    g.add(sheen);
    addLabel(g, label, 1.35);
    return g;
  }

  function buildBeam(fromX, toX, opts) {
    opts = opts || {};
    var len = toX - fromX;
    if (Math.abs(len) < 0.05) return null;
    var geo = new THREE.CylinderGeometry(opts.r || 0.025, opts.r || 0.025, Math.abs(len), 8);
    var mat = new THREE.MeshBasicMaterial({ color: opts.color || COLORS.beam, transparent: true, opacity: opts.opacity || 0.85 });
    var mesh = new THREE.Mesh(geo, mat);
    mesh.rotation.z = Math.PI / 2;
    mesh.position.set(fromX + len / 2, opts.y || 0.55, opts.z || 0);
    return mesh;
  }

  var BUILDERS = {
    source: function (item) { return buildSource(item.x, item.label, item.color); },
    lens: function (item) { return buildLens(item.x, item.label, item.wide); },
    slit: function (item) { return buildSlitPlate(item.x, item.label, item.n || 1); },
    screen: function (item) { return buildScreen(item.x, item.label, item.glow); },
    mirror: function (item) { return buildMirror(item.x, item.label, item.angle); },
    beamsplitter: function (item) { return buildBeamsplitter(item.x, item.label); },
    prism: function (item) { return buildPrism(item.x, item.label); },
    polarizer: function (item) { return buildPolarizer(item.x, item.label); },
    tube: function (item) { return buildVacuumTube(item.x, item.label); },
    atom: function (item) { return buildAtomTarget(item.x, item.label); },
    plate: function (item) { return buildPhotoPlate(item.x, item.label); }
  };

  /* ---- experiment configurations ---- */
  var CONFIGS = {
    "youngs-double-slit": [
      { type: "source", x: -5.2, label: "Laser" },
      { type: "lens", x: -3, label: "Collimator" },
      { type: "slit", x: -0.6, n: 2, label: "Double Slit" },
      { type: "screen", x: 4.4, label: "Screen", glow: true }
    ],
    "slit-diffraction": [
      { type: "source", x: -5.2, label: "Laser" },
      { type: "slit", x: -1, n: 3, label: "N-Slit Grating" },
      { type: "screen", x: 4.4, label: "Screen", glow: true }
    ],
    "polarization-malus": [
      { type: "source", x: -5.2, label: "Unpolarized Source" },
      { type: "polarizer", x: -1.8, label: "Polarizer" },
      { type: "polarizer", x: 1.4, label: "Analyzer" },
      { type: "screen", x: 4.6, label: "Detector" }
    ],
    "prism-dispersion": [
      { type: "source", x: -5, label: "White Light" },
      { type: "slit", x: -2.6, n: 1, label: "Slit" },
      { type: "prism", x: 0, label: "Prism" },
      { type: "screen", x: 4.2, label: "Spectrum Screen", glow: true }
    ],
    "michelson-interferometer": [
      { type: "source", x: -5, label: "Laser" },
      { type: "beamsplitter", x: -1, label: "Beamsplitter" },
      { type: "mirror", x: -1, z: 3, label: "Fixed Mirror M2", angle: 0 },
      { type: "mirror", x: 2.6, label: "Movable Mirror M1", angle: 90 },
      { type: "screen", x: -1, z: -3.2, label: "Detector", glow: true }
    ],
    "convex-lens-focusing": [
      { type: "source", x: -5, label: "Collimated Beam" },
      { type: "lens", x: -0.5, wide: true, label: "Convex Lens" },
      { type: "screen", x: 3, label: "Focal Screen", glow: true }
    ],
    "compound-lens-system": [
      { type: "source", x: -5.4, label: "Object" },
      { type: "lens", x: -2.4, label: "Lens 1" },
      { type: "lens", x: 1.2, label: "Lens 2" },
      { type: "screen", x: 4.6, label: "Final Image", glow: true }
    ],
    "photoelectric-effect": [
      { type: "source", x: -4.6, label: "Light Source" },
      { type: "tube", x: -0.6, label: "Vacuum Photocell" },
      { type: "screen", x: 3.4, label: "Ammeter / Voltmeter" }
    ],
    "compton-scattering": [
      { type: "source", x: -5, label: "X-ray Source" },
      { type: "atom", x: -0.6, label: "Target Electron" },
      { type: "screen", x: 3.2, z: 2.2, label: "Detector (angle θ)", glow: true }
    ],
    "single-photon-double-slit": [
      { type: "source", x: -5.2, label: "Attenuated Source\n(1 photon at a time)" },
      { type: "slit", x: -0.6, n: 2, label: "Double Slit" },
      { type: "screen", x: 4.4, label: "Photon-Counting Screen", glow: true }
    ],
    "coherence": [
      { type: "source", x: -5, label: "Source" },
      { type: "beamsplitter", x: -1, label: "Beamsplitter" },
      { type: "mirror", x: -1, z: 3, label: "Mirror (fixed path)", angle: 0 },
      { type: "mirror", x: 2.6, label: "Mirror (variable path)", angle: 90 },
      { type: "screen", x: -1, z: -3.2, label: "Fringe Detector", glow: true }
    ],
    "directionality-beam-quality": [
      { type: "source", x: -5, label: "Laser" },
      { type: "screen", x: 4.6, label: "Distant Screen" }
    ],
    "monochromaticity-purity": [
      { type: "source", x: -5, label: "Light Source" },
      { type: "prism", x: -0.8, label: "Grating / Prism" },
      { type: "screen", x: 4, label: "Spectrum Analyzer", glow: true }
    ],
    "holography": [
      { type: "source", x: -5.4, label: "Laser" },
      { type: "beamsplitter", x: -2.4, label: "Beamsplitter" },
      { type: "atom", x: 1.2, z: 2.4, label: "Object" },
      { type: "plate", x: 3.6, label: "Holographic Plate" }
    ],
    "wavelength-explorer": [
      { type: "source", x: -4, label: "Tunable Source" },
      { type: "prism", x: 0, label: "Dispersing Element" },
      { type: "screen", x: 3.6, label: "Spectrum Bar", glow: true }
    ]
  };

  function buildBench(scene, minX, maxX) {
    var len = maxX - minX + 2;
    var bench = new THREE.Mesh(
      new THREE.BoxGeometry(len, 0.12, 2.4),
      new THREE.MeshStandardMaterial({ color: COLORS.bench, metalness: 0.3, roughness: 0.7 })
    );
    bench.position.set((minX + maxX) / 2, -0.06, 0);
    scene.add(bench);

    var grid = new THREE.GridHelper(Math.max(len, 4), 12, COLORS.grid, COLORS.grid);
    grid.position.set((minX + maxX) / 2, 0.01, 0);
    grid.material.opacity = 0.35;
    grid.material.transparent = true;
    scene.add(grid);
  }

  function initOne(container) {
    var setupKey = container.getAttribute("data-setup");
    var config = CONFIGS[setupKey];
    if (!config || typeof THREE === "undefined") return;

    var width = container.clientWidth || 600;
    var height = container.clientHeight || 300;

    var scene = new THREE.Scene();
    scene.background = null;

    var camera = new THREE.PerspectiveCamera(38, width / height, 0.1, 100);
    camera.position.set(2, 4.2, 9.5);

    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    container.innerHTML = "";
    container.appendChild(renderer.domElement);

    var ambient = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambient);
    var dir = new THREE.DirectionalLight(0xffffff, 0.9);
    dir.position.set(4, 8, 6);
    scene.add(dir);
    var dir2 = new THREE.DirectionalLight(0x6699ff, 0.3);
    dir2.position.set(-4, 3, -6);
    scene.add(dir2);

    var xs = config.map(function (c) { return c.x; });
    buildBench(scene, Math.min.apply(null, xs), Math.max.apply(null, xs));

    var built = [];
    config.forEach(function (item) {
      var builder = BUILDERS[item.type];
      if (!builder) return;
      var mesh = builder(item);
      mesh.position.z = item.z || 0;
      scene.add(mesh);
      built.push(item);
    });

    // connect consecutive same-row (z ~ 0) components with a beam
    var mainRow = built.filter(function (b) { return !b.z; }).sort(function (a, b) { return a.x - b.x; });
    for (var i = 0; i < mainRow.length - 1; i++) {
      var b = buildBeam(mainRow[i].x + 0.55, mainRow[i + 1].x - 0.55, { y: 0.55 });
      if (b) scene.add(b);
    }

    var controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.08;
    controls.minDistance = 4;
    controls.maxDistance = 20;
    controls.maxPolarAngle = Math.PI / 2.05;
    controls.target.set((Math.min.apply(null, xs) + Math.max.apply(null, xs)) / 2, 0.5, 0);
    controls.update();

    var frameId;
    function animate() {
      frameId = requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    }
    animate();

    function onResize() {
      var w = container.clientWidth || width;
      var h = container.clientHeight || height;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }
    window.addEventListener("resize", onResize);

    container._apparatus3dCleanup = function () {
      cancelAnimationFrame(frameId);
      window.removeEventListener("resize", onResize);
    };
  }

  function initAll() {
    var containers = document.querySelectorAll(".apparatus-3d[data-setup]");
    containers.forEach(function (c) {
      if (c._apparatus3dCleanup) { c._apparatus3dCleanup(); }
      initOne(c);
    });
  }

  if (document.readyState === "complete" || document.readyState === "interactive") {
    setTimeout(initAll, 30);
  } else {
    document.addEventListener("DOMContentLoaded", function () { setTimeout(initAll, 30); });
  }
  // mkdocs-material instant-navigation hook (harmless no-op if absent)
  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(function () { setTimeout(initAll, 30); });
  }
})();
