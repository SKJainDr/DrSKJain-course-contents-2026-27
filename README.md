# Course Study Material & Learning Lab — 2026–27

Course study material, a virtual laser & optics laboratory, and interactive
learning games prepared by **Dr. S. K. Jain**, Associate Professor in
Physics, Department of Applied Sciences and Humanities, Invertis University,
Bareilly, for the 2026–27 academic session.

**Live site:** `https://skjaindr.github.io/DrSKJain-course-contents-2026-27/`
*(the exact address depends on where this repository is published — see
`SETUP-INSTRUCTIONS.md` for deployment steps if you are setting this up for
the first time).*

This README has two parts: **Section 1** is for the teacher(s) maintaining
this site, **Section 2** is for students using it. Both can safely read the
whole document — there are no secrets here, just different jobs to do.

---

## Section 1 — For Teachers

### 1.1 What this site is made of

Opening the home page (`index.html`) gives you two things side by side:

1. **Six course cards** — one per course you teach, each linking to that
   course's own folder under `courses/<code>/`.
2. **A link to the Advanced Laser & Optics Learning Lab** — a single
   large interactive simulator (`labs/advanced-laser-optics-lab.html`)
   with its own companion **User Guide** (`docs/`, a full documentation
   site built with MkDocs) covering 18 optics/laser experiments and 7
   industrial laser-processing workshops. This is the practical component
   that sits alongside MPY301 (Laser Physics).
3. **A link to the Advanced Mechanics & Properties of Matter Lab** — a
   second, equally large interactive simulator
   (`labs/advanced-mechanics-matter-lab.html`) with its own companion
   **User Guide** (`docs-mechanics/`, another full MkDocs documentation
   site) covering 18 UG/PG mechanics experiments (rotational dynamics,
   elasticity, fluid properties, PG-level oscillations & acoustics, and
   3 practical-application experiments — a ballistic pendulum, a rolling
   race on an incline, and gyroscopic precession)
   and 6 industrial/applied-mechanics workshops. It extends the broader
   mechanics and properties-of-matter curriculum, without being tied to a
   single course.
4. **A link to the Advanced Electricity & Magnetism Learning Lab** — a
   third companion simulator
   (`labs/advanced-electricity-magnetism-lab.html`) with its own **User
   Guide** (`docs-em/`, built with MkDocs) covering 18 experiments across
   electrostatics, magnetostatics, electrodynamics, EM waves &
   propagation, and electric/magnetic materials, plus 7 industrial
   workshops. This is the practical component that sits alongside BHP301
   (Electricity & Magnetism).

| Code | Course | Programme |
|---|---|---|
| BAS101 | Physics | B.Tech. — Semester I (all branches) |
| BAS151 | Physics Lab | B.Tech. — Semester I (all branches) |
| BHP301 | Electricity & Magnetism | B.Sc. (Hons.) Physics — Semester III |
| MPY301 | Laser Physics | M.Sc. Physics (Electronics) — Semester III |
| MPY351 | Electronics Lab | M.Sc. Physics (Electronics) — Semester III |
| VOI001 | Introduction of MS Office | B.Sc. ZBC — Semester I (Skill Enhancement) |

### 1.2 What's inside a course folder

Every course under `courses/<code>/` has the same set of pages, reached
from resource cards on that course's own home page
(`courses/<code>/index.html`):

| Page | File | Contents |
|---|---|---|
| Syllabus | `syllabus.html` | Official unit-wise syllabus |
| Books | `books.html` | Recommended & reference books |
| Course Content | `content.html` | Overview, outcomes, study approach |
| Lecture Notes | `notes.html` | Detailed unit-wise notes |
| Quiz | `quiz.html` | Self-graded 50-MCQ quiz |
| Sample Exam Papers | `exam1.html`, `exam2.html` | Two full-length practice papers |
| External Resources | `resources.html` | Curated videos/links |
| Game 1 & Game 2 | `game.html`, `game2.html` | Interactive learning games (see 1.4) |
| Teacher's Notes & Links | (section on `index.html`) | Your own live links & files (see 1.3) |

**Do not** rename these files or move them to a different folder — every
card, link and script on the site points to these exact paths.

### 1.3 Adding your own links and files (Teacher's Notes)

Every course page has a **"Teacher's Notes & Suggested Links"** section
that you — and only you — control, without touching any other file on the
site. Each course has its own folder:

```
teacher-notes/
  bas101/   links.txt   files/
  bas151/   links.txt   files/
  bhp301/   links.txt   files/
  mpy301/   links.txt   files/
  mpy351/   links.txt   files/
  voi001/   links.txt   files/
```

**To share a link** (a YouTube video, a Google Drive/Docs link, a page you
host on GitHub Pages, a note to the class, etc.):

1. Open `teacher-notes/<your-course-code>/links.txt` on GitHub and click
   the pencil ("Edit this file") icon.
2. Add one line per resource, in the format:
   ```
   Title of the resource | https://full-web-address-here
   ```
   A line with just a title and no `| link` is shown as a plain note
   (e.g. "Bring your lab manual next class").
3. Commit the change. Reload the course page — it's live immediately.

**To share a file** (PDF, DOCX, PPTX, image, etc.):

1. Go to `teacher-notes/<your-course-code>/files/` on GitHub.
2. Use **Add file → Upload files** and drop your file(s) in.
3. Commit. The file appears automatically as a downloadable card — you do
   **not** need to list it anywhere or edit any other file.
4. To remove it later, delete it from the same folder.

**Do:**
- Keep one resource per line in `links.txt`; use `#` at the start of a
  line for your own comments/reminders — they're ignored by the page.
- Only ever touch your own course's folder.

**Don't:**
- Don't edit `assets/teacher-notes.js` — that's the shared script that
  reads every course's folder; changing it affects all six courses at once.
- Don't delete the `files/README.md` placeholder inside an empty `files/`
  folder — Git doesn't track empty folders, so that placeholder is what
  keeps the folder itself in the repository. It's ignored by the page.
- Note: the automatic file listing uses GitHub's public API, which allows
  60 anonymous requests/hour per visitor. That's normally plenty for a
  class, but if it's ever briefly exceeded, the uploaded-files list simply
  stops appearing for a few minutes (your links still show); nothing is
  lost or broken.

### 1.4 Changing game and workshop targets

Most of the games, and all 7 industrial workshops in the simulator, ask a
student to hit a hidden target value (a mystery wavelength, a design
frequency, an optimal machining setting, etc.). Every one of those targets
is read from a plain-text JSON file in **`task-settings/`**, not hard-coded
into the game — so you can set a **new target for the whole class** just
by editing one file on GitHub. No coding, no rebuilding the site, no
touching the game/workshop page itself.

**To change a target:**

1. Open the relevant file in `task-settings/` on GitHub (see the table in
   `task-settings/README.md` for exactly which file controls which
   game/workshop, and what each field means).
2. Click the pencil icon, change the number(s), and commit.
3. Reload the game or workshop page — the new target is live immediately
   for every student.

**Do:**
- Change only the numeric value(s) — leave the field names (the text in
  quotes before the `:`) exactly as they are.
- Keep the file valid JSON (numbers don't need quotes; text does; don't
  leave a trailing comma after the last field). If you're not sure, open
  one of the other course's settings files as a template for the format.

**Don't:**
- Don't rename or delete a `task-settings/*.json` file — the page that
  reads it is looking for that exact filename. If a file is ever missing,
  misspelled, or contains invalid JSON, the page quietly falls back to a
  safe built-in default rather than breaking, but your intended change
  won't take effect.
- Two games (BHP301's *Gauss's Law Explorer* and MPY301's *Population
  Inversion Simulator*) are free-exploration simulators with no hidden
  target — students check their own prediction against physics computed
  from values they chose, so there's nothing to set there. The same is
  true of VOI001's *Office Skills Sprint* and *Excel Formula Challenge*,
  which use a question bank / generic formula-checking instead of a
  single number.

*Why not a real "teacher login"?* This site is hosted as plain static
pages (GitHub Pages) with no server behind it, so there is no secure way
for a webpage itself to accept a password and then write a change back to
GitHub — any password typed into the page would be visible to anyone who
looks at the page's code. Editing the settings file directly on GitHub
(as above) achieves the same goal — you change a number, every student
sees it next time they load the page — without a false sense of security.
If your institution later adds a proper backend, this is the natural
place to upgrade to real per-teacher logins.

### 1.5 If a student asks for a different version or a harder/easier target

Students can't change anything themselves (see Section 2.8) — if a
student wants a different variation, a second attempt with new numbers,
or a class-wide reset, they will ask you directly (in class, by email, or
via a note you leave in your Teacher's Notes). You have two ways to
respond, depending on what they're asking for:

- **"Can we get a fresh/different challenge?"** → Edit the relevant
  `task-settings/*.json` file (Section 1.4) and let the class know to
  reload the page.
- **"Can you share the extra material you mentioned?"** → Add it to your
  `teacher-notes/<course>/` folder (Section 1.3).

### 1.6 General editing guidelines

- **Safe to edit any time:** anything under `teacher-notes/` and
  `task-settings/`, plus the content pages listed in Section 1.2
  (syllabus, notes, quiz, exam papers, resources, etc.) if you're
  comfortable with basic HTML.
- **Edit with care, and test after:** `index.html` and any
  `courses/<code>/index.html` (these hold the card layout and colours).
- **Best left alone unless you know JavaScript:** `assets/*.js`,
  `mkdocs-source/hooks.py`, `mkdocs-source/tools/*.py`,
  `mkdocs-source-mechanics/hooks.py`, `mkdocs-source-em/hooks.py`, and the
  simulators' internal code in `labs/advanced-laser-optics-lab.html`,
  `labs/advanced-mechanics-matter-lab.html`, and
  `labs/advanced-electricity-magnetism-lab.html`.
- **Never edit the `docs/`, `docs-mechanics/`, or `docs-em/` folders
  directly** — each is the *built* output of its matching
  `mkdocs-source*/` folder. Edit the Markdown files under
  `mkdocs-source/docs/`, `mkdocs-source-mechanics/docs/`, or
  `mkdocs-source-em/docs/` instead and rebuild with `mkdocs build`
  (see each `mkdocs-source*/` folder for the source of its User Guide,
  glossary, formula reference and printable lab-record booklet).
- Full publishing/deployment steps (what to copy where, `git` commands)
  are in **`SETUP-INSTRUCTIONS.md`** — read that before your first push.
- After any change, open the page in both light and dark mode (the
  🌙/☀ toggle in the top bar of every page) to make sure nothing you
  changed is hard to see in either theme.

---

## Section 2 — For Students

### 2.1 Getting started

No login, no installation, no app to download. Open the site's home page
in any modern web browser (Chrome, Edge, Firefox, Safari — desktop or
mobile all work) and you'll see:

- A card for each of your courses — click yours to go to its course page.
- A card for the **Advanced Laser & Optics Learning Lab** — the shared
  virtual laboratory used alongside Laser Physics (MPY301).
- A card for the **Advanced Mechanics & Properties of Matter Lab** — a
  second shared virtual laboratory covering rotational dynamics,
  elasticity, fluid properties, and PG-level oscillations & acoustics.
- A card for the **Advanced Electricity & Magnetism Learning Lab** — a
  third shared virtual laboratory used alongside Electricity & Magnetism
  (BHP301), covering electrostatics, magnetostatics, electrodynamics, EM
  waves & propagation, and electric/magnetic materials.

Every page has a small 🌙/☀ button near the top — use it to switch
between light and dark mode, whichever is easier on your eyes. Your choice
is remembered on that device.

### 2.2 Finding your way around a course page

Click your course's card and you'll land on that course's own page, with
a row of cards for:

**Syllabus · Books · Course Content · Lecture Notes · 50-MCQ Quiz ·
Sample Exam Paper I & II · External Learning Resources · two Interactive
Games · Teacher's Notes & Suggested Links**

Every page has a breadcrumb at the top (`Home › YOURCOURSE`) — click
**Home** any time to get back to the course list.

### 2.3 The Teacher's Notes section

Near the bottom of your course page is **"Teacher's Notes & Suggested
Links"**. This is content your instructor adds and updates directly —
extra links (videos, slides, other pages) and files (PDFs, slide decks,
images, etc.) they want to share with just your class. Check back here
during the term; it can change at any time without the rest of the site
changing. If it ever shows "No additional notes, links or files have been
posted for this course yet," your teacher simply hasn't added anything
there yet — check again later.

### 2.4 The Interactive Games

| Course | Game 1 | Game 2 |
|---|---|---|
| BAS101 | Interference Explorer | Relativity Speed Lab |
| BAS151 | Newton's Rings Virtual Lab | Polarimeter Sugar Lab |
| BHP301 | Gauss's Law Explorer | Solenoid Field Challenge |
| MPY301 | Population Inversion Simulator | Laser Cavity Mode Challenge |
| MPY351 | Diode & BJT Curve Tracer Game | Oscillator Design Challenge |
| VOI001 | Office Skills Sprint | Excel Formula Challenge |

Most of these ask you to adjust sliders/inputs to match a **hidden target**
your instructor has set (for example, a mystery wavelength or an optimal
machining setting) — read the on-screen instructions on each game, they
explain exactly what you're trying to match and how scoring works. A few
(Gauss's Law Explorer, Population Inversion Simulator, Office Skills
Sprint, Excel Formula Challenge) work a little differently — you set up
your own scenario or answer questions from a bank, rather than guessing a
hidden number.

Your instructor can change the hidden target at any time (Section 1.4) —
so if you retry a game a few weeks later, don't be surprised if the exact
number is different; that's expected and means your teacher has refreshed
the challenge for the class.

### 2.5 The Advanced Laser & Optics Learning Lab

This is a bigger, shared virtual lab used mainly alongside Laser Physics
(MPY301), with two connected parts:

- **The simulator** (`labs/advanced-laser-optics-lab.html`) — 18
  interactive experiment panels (including 3 practical-application
  experiments — laser Doppler vibrometry, optical fiber NA & attenuation,
  and laser speckle metrology) plus 7 industrial workshop panels, with
  real-time sliders and graphs.
- **The User Guide** (linked as "docs" from the home page) — the theory,
  formulas, step-by-step procedure, observation tables, and viva-voce
  questions for every one of those 18 experiments and 7 workshops, plus a
  **Formula Quick Reference**, a **Glossary**, and a **printable Lab
  Record & Viva-Voce Booklet (PDF)** with fill-by-hand observation sheets
  and graph grids for all 18 experiments.

Every simulator panel has a **"Full theory, formulas & procedure"** link
straight to its matching User Guide page, and every User Guide page has a
**"Launch in Simulator"** link back to that exact panel — so you can move
freely between "read the theory" and "try it live" without hunting
through menus. The User Guide also has its own search box (top of every
page) if you know roughly what you're looking for.

For workshops with a hidden numeric target (e.g. LiDAR ranging), the same
rule from Section 2.4 applies — your instructor sets it, and it can
change between attempts.

### 2.6 The Advanced Mechanics & Properties of Matter Lab

This is a second, equally large shared virtual lab, extending beyond any
one course into UG and PG mechanics and properties-of-matter topics more
broadly, with the same two connected parts as the laser lab:

- **The simulator** (`labs/advanced-mechanics-matter-lab.html`) — 18
  interactive experiment panels (rotational dynamics; elasticity of
  solids; fluid properties; PG-level oscillations, damping & acoustic
  methods; and 3 practical-application experiments — a ballistic
  pendulum, a rolling race on an incline, and gyroscopic precession)
  plus 6 industrial/applied-mechanics workshop panels, with
  real-time sliders, live readouts, and graphs.
- **The User Guide** (linked as "docs-mechanics" from the home page) —
  the theory, formulas, step-by-step procedure, observation tables, and
  viva-voce questions for every one of those 18 experiments and 6
  workshops, plus a dedicated **Safety & Good Practice** page, a
  **Formula Quick Reference**, a **Glossary**, and a **printable Lab
  Record & Viva-Voce Booklet (PDF)** with fill-by-hand observation sheets
  and graph grids for all 18 experiments.

Every simulator panel has an **"Open full theory & procedure in the User
Guide"** link straight to its matching User Guide page, and every User
Guide page has a **"Launch Simulator"** link back to that exact panel —
so, just as with the laser lab, you can move freely between theory and
live exploration without hunting through menus.

### 2.7 The Advanced Electricity & Magnetism Learning Lab

A third companion virtual lab, used mainly alongside Electricity &
Magnetism (BHP301), built the same way as the other two labs:

- **The simulator** (`labs/advanced-electricity-magnetism-lab.html`) — 18
  interactive experiment panels (Electrostatics, Magnetostatics,
  Electrodynamics, EM Waves & Propagation, Electric & Magnetic Materials)
  plus 7 industrial workshop panels (EMI/EMC testing, transformer design,
  antenna radiation patterns, eddy-current NDT, magnetic shielding, HV
  breakdown testing, RF impedance matching), with real-time sliders,
  live-computed readouts, and live sweep graphs.
- **The User Guide** (linked as "docs-em" from the home page) — the
  theory, formulas, step-by-step procedure, observation tables, and
  viva-voce questions for every one of those 18 experiments and 7
  workshops, plus a **Formula Reference**, a **Glossary**, a **Safety**
  page, and a **printable Lab Record & Viva-Voce Booklet (PDF)** with
  fill-by-hand observation sheets and 15×15 cm graph grids for all 18
  experiments.

Each workshop scores your control settings against an optimal target and
unlocks a printable completion certificate above 90%, exactly like the
other two labs' workshops.

### 2.8 What to do — and what not to do

**Do:**
- Use the 🌙/☀ toggle if a page is hard to read in your current mode.
- Use your browser's own zoom (Ctrl/Cmd + `+`/`-`) if text is too small.
- Download/print the Lab Record Booklet PDF if your course requires a
  physical/fill-by-hand record.
- Refresh the page if a game or the Teacher's Notes section seems stuck
  on "Loading…" — this is usually just a slow network request.
- Ask your teacher if something looks wrong, out of date, or if you'd
  like a fresh/different version of a game's target.

**Don't:**
- Don't expect the site to remember your quiz/exam/game answers between
  visits — nothing here saves your personal progress; it's meant for
  practice, not for submitting graded work (submit graded work the way
  your teacher has told you to, separately).
- Don't try to "log in" anywhere — there is no student or teacher login
  on this site (see Section 1.4 for why); if a page ever asks you for a
  password unexpectedly, that's not part of this site and you should
  close it.
- Don't rely on a single browser tab staying open for long study
  sessions on older/low-memory phones — the simulator and games are
  graphics-heavy; if a page feels sluggish, closing other tabs usually
  helps.

### 2.9 Requesting a different variation from your teacher

If you'd like a new challenge, a harder/easier target, or extra material
for your course, you can't change any of this yourself — by design,
nothing on this site can be edited by a student, which keeps it fair for
the whole class. Instead:

- **For a new/different game or workshop target:** ask your teacher in
  class or by email. They can update it (Section 1.4) and it will be live
  for everyone next time the page is reloaded — usually within a few
  minutes of asking.
- **For extra reading material, a recording, or a link:** ask your
  teacher to add it to the **Teacher's Notes & Suggested Links** section
  of your course page (Section 1.3).

There's no request form on the site itself — this is a small, personal
course site, and a direct message to your instructor is the fastest way
to get a change made.

---

## A few things worth knowing either way

- **No installation required.** Everything runs in the browser; nothing
  is installed on your device — though if you'd like a shortcut, most
  browsers let you **install it as a desktop or home-screen app** (look
  for an install icon in the address bar, or "Add to Home Screen" on
  mobile); it will show up with its own atom-motif icon, the same one
  used as the browser-tab favicon throughout the site.
- **Works offline once loaded**, except: the Teacher's Notes file listing
  and the "search" box in the User Guide, which need an internet
  connection.
- **All content is original instructional material** prepared for these
  courses by Dr. S. K. Jain for the 2026–27 session, except the official
  syllabus text, which is reproduced from Invertis University.
- **Feedback and questions:** sanjeev.j@invertis.org

*Prepared & maintained by Dr. S. K. Jain, Associate Professor in Physics,
Department of Applied Sciences and Humanities, Invertis University,
Bareilly, India.*
