# Task Settings — Teacher-Editable Targets

Every game and workshop that asks a student to hit a specific hidden target
(a mystery wavelength, a design frequency, a machining tolerance, etc.)
reads that number from a small JSON file in this folder instead of having
it baked into the page's code. That means a teacher can set a **new
target for the whole class at any time** by editing one plain-text file on
GitHub — no coding, no touching any game/workshop file, no site rebuild.

## How to change a target

1. Open the relevant file below directly on GitHub (in the `task-settings/`
   folder of the repository).
2. Click the pencil ("Edit this file") icon.
3. Change the number(s) you want and commit the change (the default
   commit message is fine).
4. Reload the game or workshop page — the new target is live immediately
   for every student.

If a file is ever missing, misspelled in a URL, or contains invalid JSON,
the page quietly falls back to its own built-in default values — nothing
breaks.

## Files and what they control

| File | Course / Page | Values a teacher can change |
|---|---|---|
| `bas101-game.json` | BAS101 — Young's Double Slit game (`game.html`) | `wavelength_nm`, `screen_distance_m`, `slit_separation_um` — the λ, D, d used in the fringe-width challenge |
| `bas101-game2.json` | BAS101 — Relativity Speed Lab (`game2.html`) | `mysteryV` — hidden spacecraft speed as a fraction of *c* (0–1) |
| `bas151-game.json` | BAS151 — Newton's Rings Virtual Lab (`game.html`) | `mysteryLam` — hidden wavelength (nm), `mysteryR` — hidden lens radius of curvature (cm) |
| `bas151-game2.json` | BAS151 — Polarimeter Sugar Lab (`game2.html`) | `mysteryL` — tube length (dm), `mysteryC` — hidden sugar concentration (g/mL) |
| `bhp301-game2.json` | BHP301 — Solenoid Field Mystery (`game2.html`) | `mysteryN` — turns per metre, `mysteryI` — hidden current (A) |
| `mpy301-game2.json` | MPY301 — Laser Cavity Mode Spacing (`game2.html`) | `mysteryDnu` — hidden mode spacing (MHz) |
| `mpy351-game.json` | MPY351 — Curve Tracer Challenge (`game.html`) | `targetVg` — cut-in voltage (V), `targetI0` — reverse saturation current (A), `targetEta` — ideality factor |
| `mpy351-game2.json` | MPY351 — Oscillator Design Challenge (`game2.html`) | `targetF_kHz` — target LC oscillator frequency (kHz) |
| `workshops.json` | All 7 laser/photonics workshops in the Advanced Laser & Optics Lab simulator (`labs/advanced-laser-optics-lab.html`) | For each workshop (drilling, cutting, welding, alloying, LCVD, hardening, LiDAR): the `optimal` value and allowed `tolerance` for every slider (power, speed, energy, gas flow, focus, spot size, etc.) — a student scores 100% at optimal, 0% once they're `tolerance` away. LiDAR also has `trueDistance_m`, the hidden true target range in metres |

Two games — BHP301's original *Gauss's Law Explorer* (`game.html`) and
MPY301's original *Population Inversion Simulator* (`game.html`) — are
free-exploration simulators with no hidden target to hit (the student
checks their own prediction against physics computed from values they
chose), so they have no settings file. The same is true of VOI001's
*Office Skills Sprint* and *Excel Formula Challenge* games, which use a
fixed question bank / generic formula checking rather than a single
hidden numeric target.

## Adding a new game or workshop later

1. Add `assets/task-settings.js` (already on every page that needs it) and
   a `<script>const TASK = loadTaskSettings('.../task-settings/your-file.json');</script>`
   near the top of the page's inline script, before the target value is
   first used.
2. Read each value with a safe fallback, e.g.
   `const mysteryV = typeof TASK.mysteryV === 'number' ? TASK.mysteryV : 0.8;`
3. Add the new `.json` file here with a `_comment` explaining each field,
   and a row to the table above.
