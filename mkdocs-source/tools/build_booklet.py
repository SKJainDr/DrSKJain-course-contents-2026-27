# -*- coding: utf-8 -*-
"""
Regenerates docs/assets/lab-record-booklet.pdf from the current content of
docs/experiments/*.md. Run this from within mkdocs-source/ after editing any
experiment's Aim, Observation Table or Viva-Voce Questions section.

Usage:
    cd mkdocs-source
    pip install reportlab --break-system-packages
    python3 tools/build_booklet.py
"""
import re
import sys
import json
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 PageBreak, Image, HRFlowable, KeepTogether, Flowable)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

sys.path.insert(0, str(Path(__file__).resolve().parent))
import experiment_data as ED

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = Path(__file__).resolve().parent.parent  # mkdocs-source/
FONT_DIR = Path(__file__).resolve().parent / "fonts"
pdfmetrics.registerFont(TTFont("DejaVuSans", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans-Bold",
                               italic="DejaVuSans", boldItalic="DejaVuSans-Bold")
# Every governing formula uses Greek letters, subscripts and math symbols
# (λ, θ, β, δ, ν, μ, ₀, √, ×, ±, →, ≈, cot, etc.) that the base-14 PDF fonts
# (Helvetica) do not contain glyphs for — they would silently render as
# blank boxes. DejaVu Sans has full coverage for all of these, so it is used
# everywhere in this document instead of Helvetica.
DOCS_EXPERIMENTS = HERE / "docs" / "experiments"
LOGO = str(HERE / "docs" / "assets" / "invertis-logo-trimmed.png")
OUT = str(HERE / "docs" / "assets" / "lab-record-booklet.pdf")

ORDER = ["youngs-double-slit.md","slit-diffraction.md","polarization-malus.md","prism-dispersion.md",
"michelson-interferometer.md","convex-lens-focusing.md","compound-lens-system.md","photoelectric-effect.md",
"compton-scattering.md","single-photon-double-slit.md","coherence.md","directionality-beam-quality.md",
"monochromaticity-purity.md","holography.md","wavelength-explorer.md",
"laser-doppler-vibrometry.md","optical-fiber-na-attenuation.md","laser-speckle-metrology.md"]

def extract_data():
    data = []
    for fname in ORDER:
        text = (DOCS_EXPERIMENTS / fname).read_text()
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        aim = re.search(r"## Aim\n\n(.+?)\n\n##", text, re.S).group(1).strip()
        obs_sec = re.search(r"## Observation Table\n(.+?)\n## ", text, re.S).group(1)
        header_line = None
        for line in obs_sec.splitlines():
            if line.strip().startswith("|") and re.search(r"S\.\s*No", line):
                header_line = line
                break
        headers = [h.strip() for h in header_line.strip().strip("|").split("|")] if header_line else []
        result_sec_m = re.search(r"## Result\n(.+?)\n## ", text, re.S)
        result_headers = []
        if result_sec_m:
            result_sec = result_sec_m.group(1)
            for line in result_sec.splitlines():
                if line.strip().startswith("|") and not re.match(r"^\|[\s\-\|]+\|$", line.strip()):
                    result_headers = [h.strip() for h in line.strip().strip("|").split("|")]
                    break
        viva_match = re.search(r"## Viva-Voce Questions\n\n(.+?)$", text, re.S)
        viva_block = viva_match.group(1).strip() if viva_match else ""
        viva_qs = re.findall(r"^\d+\.\s+(.+)$", viva_block, re.M)
        data.append({"file": fname, "title": title, "aim": aim, "obs_headers": headers,
                     "result_headers": result_headers, "viva": viva_qs})
    return data

DATA = extract_data()
ERR_BY_FILE = {e["file"]: e for e in ED.EXPERIMENTS}

# Primary governing formula (plain-text/Unicode, since the base PDF has no
# LaTeX renderer) plus a brief description of each symbol, for the new
# "Formula Used" section that appears after the Aim and before the
# Observation Table on every experiment's page.
FORMULAS = {
    "youngs-double-slit.md": ("β = λD / d", [
        ("β", "fringe width measured on the screen (mm)"),
        ("λ", "wavelength of the laser light (nm)"),
        ("D", "distance from the double slit to the screen (m)"),
        ("d", "separation between the two slits (mm)"),
    ]),
    "slit-diffraction.md": ("a sinθ = mλ", [
        ("a", "width of the single slit (μm)"),
        ("θ", "angle of diffraction at which a minimum is observed"),
        ("m", "order of the diffraction minimum (m = ±1, ±2, …)"),
        ("λ", "wavelength of the light used (nm)"),
    ]),
    "polarization-malus.md": ("I(θ) = I₀ cos²θ", [
        ("I(θ)", "intensity transmitted through the analyzer"),
        ("I₀", "intensity after the first polarizer (θ = 0)"),
        ("θ", "angle between the polarizer and analyzer transmission axes"),
    ]),
    "prism-dispersion.md": ("μ = sin[(A+δm)/2] / sin(A/2)", [
        ("μ", "refractive index of the prism material"),
        ("A", "apex (prism) angle"),
        ("δm", "angle of minimum deviation"),
    ]),
    "michelson-interferometer.md": ("ΔL = Δm·λ / 2", [
        ("ΔL", "displacement of the movable mirror"),
        ("Δm", "number of fringes shifted, counted at the detector"),
        ("λ", "wavelength of the laser light"),
    ]),
    "convex-lens-focusing.md": ("r ≈ 1.22 λf / D", [
        ("r", "radius of the diffraction-limited focal spot (Airy disc)"),
        ("λ", "wavelength of light"),
        ("f", "focal length of the convex lens"),
        ("D", "diameter of the collimated beam entering the lens (aperture)"),
    ]),
    "compound-lens-system.md": ("1/v − 1/u = 1/f   (each lens);  m_total = m₁ × m₂", [
        ("v", "image distance from the lens"),
        ("u", "object distance from the lens"),
        ("f", "focal length of that lens"),
        ("m₁, m₂", "magnification produced by Lens 1 and Lens 2 respectively"),
    ]),
    "photoelectric-effect.md": ("eV₀ = hν − φ", [
        ("V₀", "stopping potential"),
        ("h", "Planck's constant"),
        ("ν", "frequency of the incident light"),
        ("φ", "work function of the photocathode material"),
        ("e", "charge on the electron"),
    ]),
    "compton-scattering.md": ("Δλ = λC (1 − cosθ)", [
        ("Δλ", "wavelength shift of the scattered photon"),
        ("λC", "Compton wavelength of the electron (= 2.426 pm)"),
        ("θ", "scattering angle of the photon"),
    ]),
    "single-photon-double-slit.md": ("P(y) ∝ cos²(π d y / λD)", [
        ("P(y)", "probability of detecting a photon at position y on the screen"),
        ("d", "separation between the two slits"),
        ("λ", "wavelength of the light"),
        ("D", "slit-to-screen distance"),
    ]),
    "coherence.md": ("L_c = c·τc ≈ c / Δν", [
        ("L_c", "coherence length"),
        ("c", "speed of light"),
        ("τc", "coherence time"),
        ("Δν", "frequency bandwidth (linewidth) of the source"),
    ]),
    "directionality-beam-quality.md": ("D_spot(L) ≈ D₀ + θ_div · L", [
        ("D_spot", "beam spot diameter after travelling a distance L"),
        ("D₀", "initial beam diameter at the source"),
        ("θ_div", "beam divergence (full angle)"),
        ("L", "propagation distance"),
    ]),
    "monochromaticity-purity.md": ("Purity = Δλ / λ", [
        ("Δλ", "spectral linewidth of the source"),
        ("λ", "central wavelength of the source"),
    ]),
    "holography.md": ("I = |E_obj + E_ref|²", [
        ("I", "intensity recorded at the photographic (holographic) plate"),
        ("E_obj", "object-beam field (carries amplitude & phase of the object)"),
        ("E_ref", "reference-beam field"),
    ]),
    "wavelength-explorer.md": ("E = hν = hc / λ", [
        ("E", "photon energy"),
        ("h", "Planck's constant"),
        ("c", "speed of light"),
        ("λ", "wavelength of the light"),
    ]),
    "laser-doppler-vibrometry.md": ("f_D = 2v cosθ / λ   ;   v_max = Aω", [
        ("v", "instantaneous velocity of the vibrating surface"),
        ("θ", "angle of incidence of the probe beam"),
        ("A, ω", "vibration amplitude and angular frequency"),
    ]),
    "optical-fiber-na-attenuation.md": ("NA = √(n₁²−n₂²)   ;   P_out = P_in·10^(−αL/10)", [
        ("n₁, n₂", "core and cladding refractive indices"),
        ("α", "attenuation coefficient of the fiber"),
        ("L", "fiber length"),
    ]),
    "laser-speckle-metrology.md": ("s = 1.22λz/D   ;   Contrast ≈ 1−exp[−(2πσ/λ)²]", [
        ("z", "distance from the illuminated spot to the observation screen"),
        ("D", "diameter of the illuminated beam/aperture"),
        ("σ", "RMS surface roughness"),
    ]),
}

ROYAL_BLUE = colors.HexColor("#1F3A93")
ROYAL_BLUE_DARK = colors.HexColor("#142B66")
GOLD = colors.HexColor("#C9A227")
GOLD_LIGHT = colors.HexColor("#FBF3DC")
NAVY = colors.HexColor("#0B173A")
INK = colors.HexColor("#132A3A")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontSize=22, leading=27, textColor=NAVY,
                           fontName="DejaVuSans-Bold", alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name="CoverSub", fontSize=12.5, leading=17, textColor=ROYAL_BLUE_DARK,
                           fontName="DejaVuSans", alignment=TA_CENTER, spaceAfter=4))
styles.add(ParagraphStyle(name="ExpTitle", fontSize=15, leading=19, textColor=colors.white,
                           fontName="DejaVuSans-Bold"))
styles.add(ParagraphStyle(name="ExpModule", fontSize=9, leading=12, textColor=GOLD,
                           fontName="DejaVuSans-Bold"))
styles.add(ParagraphStyle(name="SectionHead", fontSize=11, leading=14, textColor=ROYAL_BLUE_DARK,
                           fontName="DejaVuSans-Bold", spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle(name="Body", fontSize=9.3, leading=13, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="FieldLine", fontSize=9.3, leading=16, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="VivaQ", fontSize=9.3, leading=15, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="TinyFoot", fontSize=7.3, leading=10, textColor=colors.HexColor("#5a6b85"),
                           fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="CellHdr", fontSize=7.6, leading=9, textColor=colors.white,
                           fontName="DejaVuSans-Bold", alignment=TA_CENTER))
styles.add(ParagraphStyle(name="CellBody", fontSize=8.2, leading=10, textColor=INK, alignment=TA_CENTER))

PAGE_W, PAGE_H = A4


def footer(canvas, doc):
    canvas.saveState()
    # University logo, top centre of every page.
    try:
        logo_h = 9 * mm
        logo_w = logo_h * (2560 / 1185)  # matches the actual logo image's aspect ratio
        canvas.drawImage(LOGO, (PAGE_W - logo_w) / 2, PAGE_H - logo_h - 6 * mm,
                          width=logo_w, height=logo_h, mask="auto", preserveAspectRatio=True)
    except Exception:
        pass
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.4)
    canvas.line(20 * mm, 16 * mm, PAGE_W - 20 * mm, 16 * mm)
    canvas.setFont("DejaVuSans", 7.3)
    canvas.setFillColor(colors.HexColor("#5a6b85"))
    left = "Advanced Laser & Optics Learning Lab — Lab Record & Viva-Voce Booklet · Invertis University, Bareilly"
    right = f"Page {doc.page}"
    canvas.drawString(20 * mm, 11 * mm, left)
    canvas.drawRightString(PAGE_W - 20 * mm, 11 * mm, right)
    canvas.setFont("DejaVuSans", 7.3)
    canvas.drawString(20 * mm, 7 * mm,
                       "Prepared & maintained by Dr. S. K. Jain, Associate Professor in Physics, "
                       "Department of Applied Sciences and Humanities, Invertis University, Bareilly, India · sanjeev.j@invertis.org")
    canvas.restoreState()


def make_blank_table(headers, n_rows, col_widths=None):
    data = [[Paragraph(h, styles["CellHdr"]) for h in headers]]
    for _ in range(n_rows):
        data.append([Paragraph("&nbsp;", styles["CellBody"]) for _ in headers])
    if col_widths is None:
        avail = PAGE_W - 40 * mm
        col_widths = [avail / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ROYAL_BLUE),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#c9c2a8")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GOLD_LIGHT]),
    ]))
    return t


def section_head(text):
    return Paragraph(text, styles["SectionHead"])


def blank_lines(n, height_mm=7):
    rows = [[""] for _ in range(n)]
    t = Table(rows, colWidths=[PAGE_W - 40 * mm], rowHeights=[height_mm * mm] * n)
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#c9c2a8")),
    ]))
    return t


class GraphGrid(Flowable):
    """A blank graph grid, printed at an EXACT fixed physical size of
    15 cm x 15 cm when the booklet is printed at 100% scale on A4, with a
    title and axis labels (variable name + unit only, no numeric scale) so
    the student can choose their own scale and plot straight onto a
    printout of this page.

    Three tiers of ruling, matching standard mm graph paper:
      - fine mesh      every  1 mm  (light)
      - half-way grid  every  5 mm  (medium)
      - major grid     every 10 mm  (bold, royal blue)
    """

    GRID_SIZE = 150 * mm  # exactly 15 cm x 15 cm, as requested

    def __init__(self, width, height, title, x_label, y_label):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def draw(self):
        c = self.canv
        gw = gh = self.GRID_SIZE
        # Grid is a fixed physical size - never stretched or squeezed to
        # fill the container box. Simply centre it horizontally in the
        # available width, with fixed clearance below for the x-axis label
        # and above for the title.
        margin_bottom, label_gutter = 11 * mm, 8 * mm
        gx = (self.width - gw) / 2
        gy = margin_bottom

        c.setFont("DejaVuSans-Bold", 10.5)
        c.setFillColor(NAVY)
        c.drawCentredString(self.width / 2, gy + gh + 6 * mm, self.title)

        # fine mesh every 1 mm
        c.setStrokeColor(colors.HexColor("#EDE3C2"))
        c.setLineWidth(0.15)
        fine_step = 1 * mm
        fine_n = int(round(gw / fine_step))
        for i in range(fine_n + 1):
            x = gx + i * fine_step
            y = gy + i * fine_step
            c.line(x, gy, x, gy + gh)
            c.line(gx, y, gx + gw, y)

        # half-way grid every 5 mm
        c.setStrokeColor(colors.HexColor("#E3D6A0"))
        c.setLineWidth(0.3)
        half_step = 5 * mm
        half_n = int(round(gw / half_step))
        for i in range(half_n + 1):
            x = gx + i * half_step
            y = gy + i * half_step
            c.line(x, gy, x, gy + gh)
            c.line(gx, y, gx + gw, y)

        # major grid every 1 cm
        c.setStrokeColor(ROYAL_BLUE)
        c.setLineWidth(0.7)
        major_step = 10 * mm
        major_n = int(round(gw / major_step))
        for i in range(major_n + 1):
            x = gx + i * major_step
            y = gy + i * major_step
            c.line(x, gy, x, gy + gh)
            c.line(gx, y, gx + gw, y)

        # border
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.3)
        c.rect(gx, gy, gw, gh, fill=0, stroke=1)

        # axis labels
        c.setFont("DejaVuSans-Bold", 8.5)
        c.setFillColor(ROYAL_BLUE_DARK)
        c.drawCentredString(gx + gw / 2, 2.5 * mm, self.x_label)
        c.saveState()
        c.translate(gx - label_gutter, gy + gh / 2)
        c.rotate(90)
        c.drawCentredString(0, 0, self.y_label)
        c.restoreState()


def graph_box():
    """Fallback plain box for conceptual (non-quantitative) experiments."""
    t = Table([[""]], colWidths=[PAGE_W - 40 * mm], rowHeights=[45 * mm])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, ROYAL_BLUE),
        ("LINEBELOW", (0,0),(-1,-1), 0.3, colors.HexColor("#e3d6a0")),
    ]))
    return t


story = []

# ---------------- COVER PAGE ----------------
story.append(Spacer(1, 18 * mm))
try:
    story.append(Image(LOGO, width=90 * mm, height=90 * mm * (1201/2576)))
except Exception:
    pass
story.append(Spacer(1, 10 * mm))
story.append(Paragraph("Advanced Laser &amp; Optics Learning Lab", styles["CoverTitle"]))
story.append(Paragraph("Lab Record &amp; Viva-Voce Booklet", styles["CoverTitle"]))
story.append(Spacer(1, 4 * mm))
story.append(Paragraph("15 Experiments — printable, fill-by-hand observation, calculation, result and viva sheets",
                        styles["CoverSub"]))
story.append(Paragraph("Companion to the interactive simulator and online User Guide", styles["CoverSub"]))
story.append(Spacer(1, 14 * mm))
story.append(HRFlowable(width="70%", thickness=1.4, color=GOLD, hAlign="CENTER"))
story.append(Spacer(1, 10 * mm))

field_style = ParagraphStyle(name="FieldRow", fontSize=11, leading=22, textColor=INK)
for label in ["Student Name:", "Roll / Enrolment No.:", "Course & Section:"]:
    story.append(Paragraph(f"{label} " + "_" * 46, field_style))
story.append(Paragraph("Academic Session: 2026&ndash;27", field_style))
story.append(Spacer(1, 16 * mm))
story.append(Paragraph("Invertis University, Bareilly, India", styles["CoverSub"]))
story.append(Paragraph("Prepared &amp; maintained by Dr. S. K. Jain, Associate Professor in Physics, Department of Applied Sciences and Humanities, Invertis University, Bareilly, India",
                        styles["CoverSub"]))
story.append(Paragraph("sanjeev.j@invertis.org", styles["CoverSub"]))
story.append(PageBreak())

# ---------------- HOW TO USE ----------------
story.append(section_head("How to Use This Booklet"))
story.append(Paragraph(
    "This booklet mirrors the 15 experiments in the online <b>User Guide</b> and the interactive simulator. "
    "For each experiment: run the simulator panel as instructed in the guide, record your readings directly "
    "in the observation table below, plot your graph on the provided 15&times;15 grid (choose your own scale "
    "per square), complete the calculation and result sections, work out the maximum permissible error using "
    "the least counts of the instruments you used, and prepare written answers to the viva-voce questions "
    "before your practical examination. Full theoretical background, governing formulas and step-by-step "
    "procedure for every experiment are available in the online guide — this booklet intentionally contains "
    "only the record-keeping sheets, not the theory, to keep it compact for printing.", styles["Body"]))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Contents", styles["SectionHead"]))
toc_rows = [[Paragraph(f"{i+1}.", styles["CellBody"]), Paragraph(d["title"].split(". ",1)[-1], styles["Body"])]
            for i, d in enumerate(DATA)]
toc_table = Table(toc_rows, colWidths=[10*mm, PAGE_W-50*mm])
toc_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
]))
story.append(toc_table)
story.append(PageBreak())

# ---------------- PER-EXPERIMENT SHEETS ----------------
for idx, d in enumerate(DATA, start=1):
    block = []
    # Title banner
    banner_data = [[Paragraph(d["title"], styles["ExpTitle"])]]
    banner = Table(banner_data, colWidths=[PAGE_W - 40*mm])
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEBELOW", (0,0), (-1,-1), 3, GOLD),
    ]))
    block.append(banner)
    block.append(Spacer(1, 4*mm))

    block.append(section_head("Aim"))
    block.append(Paragraph(d["aim"], styles["Body"]))
    block.append(Spacer(1, 2*mm))

    block.append(Paragraph("Date performed: " + "_"*20 + "&nbsp;&nbsp;&nbsp; Simulator panel used: " + "_"*30,
                            styles["FieldLine"]))
    story.append(KeepTogether(block))

    # ---- Formula Used (with a labelled-diagram space) — after Aim, before
    # the Observation Table, as requested. ----
    story.append(section_head("Formula Used"))
    formula_info = FORMULAS.get(d["file"])
    if formula_info:
        formula_text, terms = formula_info
        story.append(Paragraph(formula_text, ParagraphStyle(
            name="FormulaText", parent=styles["Body"], fontSize=12, leading=16,
            textColor=ROYAL_BLUE_DARK, fontName="DejaVuSans-Bold", spaceAfter=3)))
        for sym, meaning in terms:
            story.append(Paragraph(f"<b>{sym}</b> = {meaning}", styles["Body"]))
    else:
        story.append(Paragraph("(Conceptual experiment — no single numerical formula; "
                                "describe the physical principle in your own words.)", styles["Body"]))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph("Labelled diagram of the experimental apparatus:", styles["FieldLine"]))
    diagram_box = Table([[""]], colWidths=[PAGE_W - 40*mm], rowHeights=[0.35*PAGE_H])
    diagram_box.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, ROYAL_BLUE),
    ]))
    story.append(diagram_box)
    story.append(Spacer(1, 3*mm))

    story.append(section_head("Observation Table"))
    if d["obs_headers"]:
        story.append(make_blank_table(d["obs_headers"], n_rows=6))
    else:
        story.append(Paragraph("(Conceptual experiment — record your step-by-step observations/sketches below.)",
                                styles["Body"]))
        story.append(blank_lines(6))
    story.append(Spacer(1, 3*mm))

    err_info = ERR_BY_FILE.get(d["file"], {})
    if err_info.get("graph_title"):
        story.append(KeepTogether([
            section_head("Graph"),
            GraphGrid(PAGE_W - 40 * mm, 178 * mm, err_info["graph_title"],
                      err_info["x_label"], err_info["y_label"]),
        ]))
    else:
        story.append(section_head("Graph"))
        story.append(Paragraph("(Qualitative experiment — use this space to sketch the process/stages.)",
                                styles["Body"]))
        story.append(graph_box())
    story.append(Spacer(1, 3*mm))

    story.append(section_head("Calculation"))
    story.append(blank_lines(5))
    story.append(Spacer(1, 2*mm))

    story.append(section_head("Result"))
    if d["result_headers"]:
        story.append(make_blank_table(d["result_headers"], n_rows=3))
    else:
        story.append(blank_lines(3))
    story.append(Spacer(1, 3*mm))

    story.append(section_head("Maximum Permissible Error"))
    if err_info.get("error_formula_text"):
        story.append(Paragraph("<b>Formula:</b> " + err_info["error_formula_text"], styles["Body"]))
        story.append(Spacer(1, 1.5*mm))
        story.append(Paragraph(err_info["error_note"], styles["Body"]))
        story.append(Spacer(1, 2*mm))
        lc_headers = ["Quantity", "Measured Value", "Least Count (LC)"]
        lc_rows = [lc_headers]
        for v in err_info["variables"]:
            qty = f'{v["label"]} \u2014 {v["name"]}' + (f' ({v["unit"]})' if v.get("unit") else "")
            lc_rows.append([qty, "", ""])
        lc_table_data = [[Paragraph(c, styles["CellHdr"] if i == 0 else styles["CellBody"]) for c in row]
                          for i, row in enumerate(lc_rows)]
        avail = PAGE_W - 40*mm
        lc_table = Table(lc_table_data, colWidths=[avail*0.5, avail*0.25, avail*0.25], repeatRows=1)
        lc_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), ROYAL_BLUE),
            ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#c9c2a8")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0,0),(0,-1), "LEFT"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GOLD_LIGHT]),
        ]))
        story.append(lc_table)
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph("Calculation of maximum permissible error:", styles["Body"]))
        story.append(blank_lines(3))
    else:
        story.append(Paragraph(err_info.get("error_note",
            "Not applicable \u2014 qualitative experiment."), styles["Body"]))
    story.append(Spacer(1, 3*mm))

    viva_block = [section_head("Viva-Voce Questions")]
    for qi, q in enumerate(d["viva"], start=1):
        viva_block.append(Paragraph(f"{qi}. {q}", styles["VivaQ"]))
        viva_block.append(Spacer(1, 6*mm))
        viva_block.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#d8d2c2")))
        viva_block.append(Spacer(1, 2*mm))
    story.append(KeepTogether(viva_block[:3]))
    for extra in viva_block[3:]:
        story.append(extra)

    if idx < len(DATA):
        story.append(PageBreak())

doc = SimpleDocTemplate(OUT, pagesize=A4,
                         leftMargin=20*mm, rightMargin=20*mm, topMargin=26*mm, bottomMargin=22*mm,
                         title="Advanced Laser & Optics Learning Lab — Lab Record & Viva-Voce Booklet",
                         author="Dr. S. K. Jain")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Built:", OUT)
