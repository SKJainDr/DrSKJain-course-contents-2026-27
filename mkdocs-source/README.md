# Advanced Laser & Optics Learning Lab — MkDocs User Guide (source)

This folder is the **editable source** for the documentation published at
`docs/` in the root of this repository (served by GitHub Pages at
`https://skjaindr.github.io/DrSKJain-course-contents-2026-27/docs/`).

## What's in the guide

- **15 experiment pages** (`docs/experiments/`), each with Aim, Theory,
  Formulas, a **3-D apparatus schematic** (drag-to-rotate Three.js viewer),
  Simulator Controls, Procedure, Observation Table, Result, Precautions, a
  **4-question Self-Check Quiz**, and Viva-Voce Questions.
- **Formula Quick Reference** (`docs/formula-reference.md`) — every equation
  on one page.
- **Glossary** (`docs/glossary.md`) — alphabetical key-term definitions,
  cross-linked to the relevant experiment.
- **Printable Lab Record & Viva-Voce Booklet** (`docs/assets/lab-record-booklet.pdf`)
  — a 32-page, fill-by-hand PDF with a blank observation table, graph box,
  calculation space, result table and viva questions for all 15 experiments.
  Regenerate it after editing content with:
  ```bash
  cd mkdocs-source
  pip install reportlab --break-system-packages
  python3 tools/build_booklet.py
  ```
  The script reads directly from `docs/experiments/*.md`, so any edits to the
  Aim, Observation Table or Viva-Voce Questions sections are picked up
  automatically.
- Safety module + 7 industrial workshops (unchanged from the original guide).

## Editing content

- Page content lives under `docs/*.md`, `docs/experiments/`, `docs/workshops/`.
- Do **not** edit anything under the root-level `/docs` folder directly — that
  folder is *generated output*. Always edit the Markdown here and rebuild.
- The author/contact block at the bottom of every page is injected
  automatically by `hooks.py` — edit it once there and it updates everywhere.
- The 3-D apparatus schematics are driven by `docs/javascripts/apparatus3d.js`
  — each experiment's component layout is a small config object in that file
  (search for `CONFIGS`). Edit component positions/labels there; no per-page
  HTML editing needed beyond the existing `<div class="apparatus-3d" data-setup="...">`
  embed already placed in each experiment page.
- Colour scheme (deep royal blue `#1F3A93` / deep golden yellow `#C9A227`) and
  the university logo are configured in `docs/stylesheets/extra.css` and
  `mkdocs.yml` (`theme.logo`, `theme.favicon`).
- There are **15 documented experiments** (`docs/index.md` § Contents),
  including the Michelson Interferometer (#5) and the Red→UV Wavelength &
  Photon-Energy Explorer (#15).

## Build / preview locally

```bash
pip install mkdocs mkdocs-material
mkdocs serve      # live preview at http://127.0.0.1:8000
mkdocs build      # outputs the static site to ../docs (repo root /docs)
```

After running `mkdocs build`, commit the updated `/docs` folder along with
your Markdown changes and push — GitHub Pages will pick up the new build
automatically.

Theme: deep royal blue (`#1F3A93`) & deep golden yellow (`#C9A227`) palette
(see `docs/stylesheets/extra.css`).

Author: Dr. S. K. Jain, Associate Professor, Department of Physics,
Invertis University, Bareilly — sanjeev.j@invertis.org
