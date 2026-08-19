# -*- coding: utf-8 -*-
"""
Regenerates docs-em/assets/lab-record-booklet-em.pdf (via mkdocs-source-em/docs/
assets/lab-record-booklet-em.pdf) from the current content of
mkdocs-source-em/docs/experiments/*.md and the EM_PANELS controls defined in
labs/advanced-electricity-magnetism-lab.html.

Usage:
    cd mkdocs-source-em
    python3 tools/build_booklet_em.py
"""
import re
import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 PageBreak, Image, HRFlowable, KeepTogether, Flowable)
from reportlab.lib.enums import TA_CENTER

sys.path.insert(0, str(Path(__file__).resolve().parent))
import em_formulas as EF

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = Path(__file__).resolve().parent.parent  # mkdocs-source-em/
FONT_DIR = Path(__file__).resolve().parent / "fonts"
pdfmetrics.registerFont(TTFont("DejaVuSans", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans-Bold",
                               italic="DejaVuSans", boldItalic="DejaVuSans-Bold")

DOCS_EXPERIMENTS = HERE / "docs" / "experiments"
LAB_HTML = HERE.parent / "labs" / "advanced-electricity-magnetism-lab.html"
LOGO = str(HERE / "docs" / "assets" / "invertis-logo-trimmed.png")
OUT = str(HERE / "docs" / "assets" / "lab-record-booklet-em.pdf")

ORDER = ["coulombs-law.md","dipole-field-potential.md","gauss-law-flux.md","parallel-plate-capacitor.md",
"conductors-charge-distribution.md","image-charge-grounded-plane.md","multipole-expansion-quadrupole.md",
"biot-savart-wire.md","circular-coil-helmholtz.md","ampere-law-solenoid-toroid.md","force-parallel-conductors.md",
"magnetic-vector-potential-dipole.md","cyclotron-velocity-selector.md",
"faraday-induction.md","motional-emf-lenz.md","rc-rl-transients.md","lcr-resonance.md",
"eddy-current-damping.md","rlc-filter-response.md","poynting-vector-coaxial-cable.md",
"maxwell-plane-waves.md","wave-propagation-media-skindepth.md","reflection-refraction-brewster.md",
"waveguide-cutoff-frequency.md","transmission-line-impedance-vswr.md","faraday-cage-shielding-effectiveness.md",
"dielectric-polarization-clausius-mossotti.md","magnetic-hysteresis-bh-curve.md",
"hall-effect-carrier-density.md","meissner-effect-flux-expulsion.md"]

# ---------------- extract per-experiment DATA from the .md files ----------------
def extract_data():
    data = []
    for fname in ORDER:
        text = (DOCS_EXPERIMENTS / fname).read_text(encoding="utf-8")
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

        # graph title / axis labels from the embedded SVG
        graph_title = x_label = y_label = None
        gm = re.search(r'<text[^>]*font-size="1[4-8]"[^>]*font-weight="700"[^>]*>(.+?)</text>', text)
        if gm:
            graph_title = re.sub(r"&#8594;|&rarr;", "", gm.group(1)).strip()
        axis_texts = re.findall(r'<text ([^>]*)>(.+?)</text>', text)
        for attrs, content in axis_texts:
            if 'font-weight="700"' in attrs:
                continue
            label = re.sub(r"&#8594;|&rarr;", "", content).strip()
            if "rotate(-90" in attrs:
                y_label = label
            elif 'text-anchor="middle"' in attrs and label:
                x_label = label

        # Maximum Permissible Error formula + note
        err_m = re.search(r"## Maximum Permissible Error\n\n\$\$ (.+?) \$\$\n\n(.+?)\n\n<div class=\"error-calc\"", text, re.S)
        error_formula_text = err_m.group(1).strip() if err_m else None
        error_note = err_m.group(2).strip() if err_m else ""
        # strip a handful of LaTeX macros that may appear in the error formula for plain-text display
        if error_formula_text:
            error_formula_text = latex_to_text(error_formula_text)

        data.append({"file": fname, "title": title, "aim": aim, "obs_headers": headers,
                     "result_headers": result_headers, "viva": viva_qs,
                     "graph_title": graph_title, "x_label": x_label, "y_label": y_label,
                     "error_formula_text": error_formula_text, "error_note": error_note})
    return data


def latex_to_text(s):
    s = re.sub(r"\\dfrac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)", s)
    s = re.sub(r"\\dfrac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)", s)  # nested pass
    s = re.sub(r"\\tfrac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)", s)
    s = s.replace("\\Delta", "\u0394").replace("\\lambda", "\u03bb").replace("\\sigma", "\u03c3")
    s = s.replace("\\cdot", "\u00b7").replace("\\,", " ").replace("\\;", " ")
    s = s.replace("\\left(", "(").replace("\\right)", ")")
    s = re.sub(r"\\text\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\qquad", "   ").replace("\\quad", "  ")
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("_{", "_").replace("}", "").replace("{", "")
    return s.strip()


# ---------------- extract controls (variables + defaults) from the lab HTML ----------------
def extract_controls():
    html = LAB_HTML.read_text(encoding="utf-8")
    result = {}
    # split on each experiment block by id
    for m in re.finditer(r'id:"([a-z0-9-]+)", kind:"experiment".*?controls:\[(.*?)\],\s*\n\s*resultSymbol', html, re.S):
        exp_id, controls_blob = m.group(1), m.group(2)
        ctrls = []
        for cm in re.finditer(r'\{key:"(\w+)",label:"([^"]*)",name:"([^"]*)",unit:"([^"]*)",min:([\d.\-]+),max:([\d.\-]+),default:([\d.\-]+)', controls_blob):
            key, label, name, unit, mn, mx, default = cm.groups()
            ctrls.append({"key": key, "label": label, "name": name, "unit": unit,
                          "min": mn, "max": mx, "default": default})
        result[exp_id] = ctrls
    return result

CONTROLS_BY_ID = extract_controls()
DATA = extract_data()

# ---------------- styling (mirrors the Laser & Optics booklet) ----------------
NAVY = colors.HexColor("#0B173A")
ROYAL_BLUE = colors.HexColor("#3C5283")
ROYAL_BLUE_DARK = colors.HexColor("#243a66")
GOLD = colors.HexColor("#C9A227")
GOLD_LIGHT = colors.HexColor("#FBF6E3")
INK = colors.HexColor("#1a2338")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontSize=20, leading=25, textColor=NAVY,
                           fontName="DejaVuSans-Bold", alignment=TA_CENTER, spaceAfter=4))
styles.add(ParagraphStyle(name="CoverSub", fontSize=10.5, leading=15, textColor=ROYAL_BLUE_DARK,
                           fontName="DejaVuSans", alignment=TA_CENTER))
styles.add(ParagraphStyle(name="ExpTitle", fontSize=14, leading=18, textColor=colors.white,
                           fontName="DejaVuSans-Bold"))
styles.add(ParagraphStyle(name="SectionHead", fontSize=11, leading=14, textColor=ROYAL_BLUE_DARK,
                           fontName="DejaVuSans-Bold", spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle(name="Body", fontSize=9.3, leading=13, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="FieldLine", fontSize=9.3, leading=16, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="VivaQ", fontSize=9.3, leading=15, textColor=INK, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="CellHdr", fontSize=7.4, leading=9, textColor=colors.white,
                           fontName="DejaVuSans-Bold", alignment=TA_CENTER))
styles.add(ParagraphStyle(name="CellBody", fontSize=8.2, leading=10, textColor=INK, alignment=TA_CENTER, fontName="DejaVuSans"))
styles.add(ParagraphStyle(name="FormulaText", parent=styles["Body"], fontSize=12, leading=16,
                           textColor=ROYAL_BLUE_DARK, fontName="DejaVuSans-Bold", spaceAfter=3))

PAGE_W, PAGE_H = A4


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def footer(canvas, doc):
    canvas.saveState()
    try:
        logo_h = 9 * mm
        logo_w = logo_h * (2560 / 1185)
        canvas.drawImage(LOGO, (PAGE_W - logo_w) / 2, PAGE_H - logo_h - 6 * mm,
                          width=logo_w, height=logo_h, mask="auto", preserveAspectRatio=True)
    except Exception:
        pass
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.4)
    canvas.line(20 * mm, 16 * mm, PAGE_W - 20 * mm, 16 * mm)
    canvas.setFont("DejaVuSans", 7.3)
    canvas.setFillColor(colors.HexColor("#5a6b85"))
    left = "Advanced Electricity & Magnetism Learning Lab — Lab Record & Viva-Voce Booklet · Invertis University, Bareilly"
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
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#c9c2a8"))]))
    return t


class GraphGrid(Flowable):
    GRID_SIZE = 150 * mm

    def __init__(self, width, height, title, x_label, y_label):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.title = title or "Graph"
        self.x_label = x_label or "x"
        self.y_label = y_label or "y"

    def draw(self):
        c = self.canv
        gw = gh = self.GRID_SIZE
        margin_bottom, label_gutter = 11 * mm, 8 * mm
        gx = (self.width - gw) / 2
        gy = margin_bottom

        c.setFont("DejaVuSans-Bold", 10.5)
        c.setFillColor(NAVY)
        c.drawCentredString(self.width / 2, gy + gh + 6 * mm, self.title)

        c.setStrokeColor(colors.HexColor("#EDE3C2")); c.setLineWidth(0.15)
        fine_step = 1 * mm; fine_n = int(round(gw / fine_step))
        for i in range(fine_n + 1):
            x = gx + i * fine_step; y = gy + i * fine_step
            c.line(x, gy, x, gy + gh); c.line(gx, y, gx + gw, y)

        c.setStrokeColor(colors.HexColor("#E3D6A0")); c.setLineWidth(0.3)
        half_step = 5 * mm; half_n = int(round(gw / half_step))
        for i in range(half_n + 1):
            x = gx + i * half_step; y = gy + i * half_step
            c.line(x, gy, x, gy + gh); c.line(gx, y, gx + gw, y)

        c.setStrokeColor(ROYAL_BLUE); c.setLineWidth(0.7)
        major_step = 10 * mm; major_n = int(round(gw / major_step))
        for i in range(major_n + 1):
            x = gx + i * major_step; y = gy + i * major_step
            c.line(x, gy, x, gy + gh); c.line(gx, y, gx + gw, y)

        c.setStrokeColor(NAVY); c.setLineWidth(1.3)
        c.rect(gx, gy, gw, gh, fill=0, stroke=1)

        c.setFont("DejaVuSans-Bold", 8.5)
        c.setFillColor(ROYAL_BLUE_DARK)
        c.drawCentredString(gx + gw / 2, 2.5 * mm, self.x_label)
        c.saveState()
        c.translate(gx - label_gutter, gy + gh / 2)
        c.rotate(90)
        c.drawCentredString(0, 0, self.y_label)
        c.restoreState()


story = []

# ---------------- COVER PAGE ----------------
story.append(Spacer(1, 18 * mm))
try:
    story.append(Image(LOGO, width=90 * mm, height=90 * mm * (1201/2576)))
except Exception:
    pass
story.append(Spacer(1, 10 * mm))
story.append(Paragraph("Advanced Electricity &amp; Magnetism Learning Lab", styles["CoverTitle"]))
story.append(Paragraph("Lab Record &amp; Viva-Voce Booklet", styles["CoverTitle"]))
story.append(Spacer(1, 4 * mm))
story.append(Paragraph(f"{len(DATA)} Experiments — printable, fill-by-hand observation, calculation, result and viva sheets",
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
    f"This booklet mirrors the {len(DATA)} experiments in the online <b>User Guide</b> and the interactive simulator. "
    "For each experiment: run the simulator panel as instructed in the guide, record your readings directly "
    "in the observation table below, plot your graph on the provided 15&times;15 grid (choose your own scale "
    "per square), complete the calculation and result sections, work out the maximum permissible error using "
    "the least counts of the instruments you used, and prepare written answers to the viva-voce questions "
    "before your practical examination. Full theoretical background, governing formulas and step-by-step "
    "procedure for every experiment are available in the online guide — this booklet intentionally contains "
    "only the record-keeping sheets, not the theory, to keep it compact for printing.", styles["Body"]))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Contents", styles["SectionHead"]))
toc_rows = [[Paragraph(f"{i+1}.", styles["CellBody"]), Paragraph(d["title"], styles["Body"])]
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

    story.append(section_head("Formula Used"))
    formula_info = EF.FORMULAS.get(d["file"])
    if formula_info:
        formula_text, terms = formula_info
        story.append(Paragraph(formula_text, styles["FormulaText"]))
        for sym, meaning in terms:
            story.append(Paragraph(f"<b>{sym}</b> = {meaning}", styles["Body"]))
    else:
        story.append(Paragraph("See the governing formula in the online User Guide for this experiment.", styles["Body"]))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph("Labelled diagram of the experimental apparatus:", styles["FieldLine"]))
    diagram_box = Table([[""]], colWidths=[PAGE_W - 40*mm], rowHeights=[0.35*PAGE_H])
    diagram_box.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, ROYAL_BLUE)]))
    story.append(diagram_box)
    story.append(Spacer(1, 3*mm))

    story.append(section_head("Observation Table"))
    if d["obs_headers"]:
        story.append(make_blank_table(d["obs_headers"], n_rows=6))
    else:
        story.append(Paragraph("(Record your step-by-step observations/sketches below.)", styles["Body"]))
        story.append(blank_lines(6))
    story.append(Spacer(1, 3*mm))

    if d.get("graph_title"):
        story.append(KeepTogether([
            section_head("Graph"),
            GraphGrid(PAGE_W - 40 * mm, 178 * mm, d["graph_title"], d["x_label"], d["y_label"]),
        ]))
    else:
        story.append(section_head("Graph"))
        story.append(Paragraph("(Use this space to sketch the process/stages.)", styles["Body"]))
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
    ctrls = CONTROLS_BY_ID.get(d["file"][:-3], [])
    if d.get("error_formula_text") and ctrls:
        story.append(Paragraph("<b>Formula:</b> " + d["error_formula_text"], styles["Body"]))
        story.append(Spacer(1, 1.5*mm))
        story.append(Paragraph(d["error_note"], styles["Body"]))
        story.append(Spacer(1, 2*mm))
        lc_headers = ["Quantity", "Measured Value", "Least Count (LC)"]
        lc_rows = [lc_headers]
        for v in ctrls:
            qty = f'{esc(v["label"])} \u2014 {esc(v["name"])}' + (f' ({esc(v["unit"])})' if v.get("unit") else "")
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
        story.append(Paragraph(d.get("error_note") or "See the online User Guide for the error-propagation formula.", styles["Body"]))
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
                         title="Advanced Electricity & Magnetism Learning Lab — Lab Record & Viva-Voce Booklet",
                         author="Dr. S. K. Jain")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Built:", OUT)
