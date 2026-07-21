# How to publish this on your GitHub Pages site

Repo: **SKJainDr/DrSKJain-course-contents-2026-27**
Live docs will be at: **https://skjaindr.github.io/DrSKJain-course-contents-2026-27/docs/**

## To publish it

```bash
# from inside your local clone of the repo
cp -r /path/to/this/package/docs            ./docs
cp -r /path/to/this/package/mkdocs-source    ./mkdocs-source
cp    /path/to/this/package/index.html       ./index.html
cp    /path/to/this/package/README.md        ./README.md
cp    /path/to/this/package/site.webmanifest ./site.webmanifest
cp -r /path/to/this/package/assets           ./assets
cp -r /path/to/this/package/courses          ./courses
cp -r /path/to/this/package/labs             ./labs
cp -r /path/to/this/package/teacher-notes    ./teacher-notes
cp -r /path/to/this/package/task-settings    ./task-settings

git add docs mkdocs-source index.html README.md site.webmanifest assets courses labs teacher-notes task-settings
git commit -m "Add bidirectional links, error analysis, apparatus diagrams, new games"
git push
```

## What's new in this round

### 1. Bidirectional links between documentation and simulator
- Every simulator panel (all 23: 15 experiments + safety + 7 workshops) now has a
  **"Full theory, formulas & procedure"** link straight to its matching documentation page.
- Every documentation page now has a **"Launch in Simulator"** link that opens the
  simulator with that exact panel already active (e.g. `labs/advanced-laser-optics-lab.html#panel-michelson`).
  I added URL-hash routing to the simulator's JavaScript to make this work.

### 2. Reasonable, plottable graph space
- Replaced the old placeholder graph box with an actual **10×10 grid** (with a couple of
  minor gridlines per square, like real graph paper), a **graph title**, and **axis labels
  showing only the variable name and unit** (no pre-printed numeric scale) — so students
  choose their own scale, exactly as asked. This is in both the online docs (crisp inline
  SVG) and the printable PDF booklet (vector-drawn, prints cleanly).

### 3. Maximum Permissible Error
- Every experiment (except the two qualitative ones, Holography and — partially — Single-
  Photon Build-up, where I used Poisson counting statistics instead) now has a
  **"Maximum Permissible Error"** section with the correct error-propagation formula
  derived from that experiment's governing equation.
- **Online docs:** an interactive calculator — the student enters the measured value and
  least count (instrument resolution) for each quantity, and it computes the propagated
  error live in the browser.
- **PDF booklet:** the same formula, a fillable "Quantity / Measured Value / Least Count"
  table, and blank working space, for students filling it in by hand.

### 4. Apparatus illustrations
One clarification on what I actually delivered here: I looked into using real photographs,
but I don't have network access to Wikimedia or any general image host from this
environment, and — separately — a source link doesn't make a copyrighted photo legally
reusable regardless. So instead, every one of the 15 experiment pages now has an
**original, labelled 2-D apparatus diagram** (source → lens → slit → screen, etc., drawn
to scale with the correct component sequence for that experiment), sitting right above the
existing 3-D schematic for a clearer, more detailed picture. If you'd specifically like
real photographs added later, the cleanest path is for you (or the department) to supply
your own lab photos and I can slot them in — just share the image files.

### 5. One additional game per course (6 new games)
Each is on a **different topic** from that course's existing game, picked from later units
in the syllabus, with the same branding, footer and interactive scoring:

| Course | Existing game | New game (this round) |
|---|---|---|
| BAS101 | Interference Explorer | **Relativity Speed Lab** — match a mystery spacecraft's time dilation / length contraction to find its hidden v/c |
| BAS151 | Newton's Rings Virtual Lab | **Polarimeter Sugar Lab** — determine an unknown sugar concentration from optical rotation |
| BHP301 | Gauss's Law Explorer | **Solenoid Field Challenge** — design turns/current to hit a target B field (Ampere's law) |
| MPY301 | Population Inversion Simulator | **Laser Cavity Mode Challenge** — set mirror separation to hit a target mode spacing |
| MPY351 | Curve Tracer Challenge | **Oscillator Design Challenge** — choose L, C for an LC tank to hit a target frequency |
| VOI001 | Office Skills Sprint (matching quiz) | **Excel Formula Challenge** — type real formulas (SUM/AVERAGE/IF/MAX/MIN), evaluated live against a worksheet |

All six were tested end-to-end (not just written and assumed correct) — I ran each one
through a headless DOM, fed in the known-correct values, and confirmed the scoring logic
actually reports success, and separately confirmed wrong answers get useful, non-generic
feedback rather than a false "correct."

## Fixes from earlier rounds (still included)

- Experiment count corrected 14 → 15 (added the missing Wavelength Explorer documentation page).
- Curve Tracer Challenge (`courses/mpy351/game.html`) — the cut-in-voltage slider now
  actually affects the diode curve and scoring (it previously did nothing).
- University logo, deep-royal-blue/deep-golden-yellow branding, and your contact footer
  across all 60 original pages plus these 6 new games (66 pages total).

## If anything doesn't look right

- I haven't reviewed the other 5 original course games (beyond Curve Tracer Challenge) for
  bugs yet — say the word and I'll check those the same way.
- If you'd like the apparatus diagrams supplemented with real lab photographs, send me the
  image files and I'll slot them in alongside the illustrations.
