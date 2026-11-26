from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

source = Path("outputs/Authority Swap - Research Workflow.md")
target = source.with_suffix(".pdf")
font_dir = Path("C:/Windows/Fonts")
for name, file in [("PlanSans", "arial.ttf"), ("PlanSansBold", "arialbd.ttf"), ("PlanSansItalic", "ariali.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / file)))
pdfmetrics.registerFontFamily("PlanSans", normal="PlanSans", bold="PlanSansBold", italic="PlanSansItalic")

ink = colors.HexColor("#202B36")
navy = colors.HexColor("#142A42")
blue = colors.HexColor("#245674")
muted = colors.HexColor("#4C6273")
body = ParagraphStyle("Body", fontName="PlanSans", fontSize=10, leading=13.4,
                      textColor=ink, spaceAfter=7, alignment=TA_LEFT)
title = ParagraphStyle("Title", parent=body, fontName="PlanSansBold", fontSize=22,
                       leading=26, textColor=navy, spaceAfter=5)
meta = ParagraphStyle("Meta", parent=body, fontSize=9, leading=11.5,
                      textColor=muted, spaceAfter=9)
heading = ParagraphStyle("Heading", parent=body, fontName="PlanSansBold", fontSize=11,
                         leading=14, textColor=blue, spaceBefore=4, spaceAfter=4,
                         keepWithNext=True)
cell = ParagraphStyle("Cell", parent=body, fontSize=9.1, leading=11.6, spaceAfter=0)
header = ParagraphStyle("TableHead", parent=cell, fontName="PlanSansBold", textColor=colors.white)

def inline(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
                  r'<link href="\2" color="#245674"><u>\1</u></link>', text)

elements = []
rows = []

def flush_table():
    if not rows:
        return
    paragraphs = [[Paragraph(inline(value), header if index == 0 else cell)
                   for value in row] for index, row in enumerate(rows)]
    table = Table(paragraphs, colWidths=[138, 49, 324.27], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), blue),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#EDF3F7"), colors.white]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, -1), (-1, -1), 0.5, colors.HexColor("#CBD7DF")),
    ]))
    table.spaceAfter = 8
    elements.append(table)
    rows.clear()

for raw in source.read_text(encoding="utf-8-sig").splitlines():
    line = raw.strip()
    if line.startswith("|"):
        values = [value.strip() for value in line.strip("|").split("|")]
        if not all(re.fullmatch(r":?-+:?", value) for value in values):
            rows.append(values)
        continue
    flush_table()
    if line == "<!-- pagebreak -->":
        elements.append(PageBreak())
    elif line.startswith("# "):
        elements.append(Paragraph(inline(line[2:].replace(" | ", "  |  ")), title))
    elif line.startswith("## "):
        elements.append(Paragraph(inline(line[3:]), heading))
    elif line.startswith("**14 November"):
        elements.append(Paragraph(inline(line), meta))
    elif line:
        elements.append(Paragraph(inline(line), body))
flush_table()

def add_page_number(canvas, document):
    canvas.setFont("PlanSans", 8)
    canvas.setFillColor(muted)
    canvas.drawRightString(A4[0] - 42, 25, f"Authority Swap  /  {document.page}")


document = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=42, rightMargin=42,
                             topMargin=36, bottomMargin=38, title="Authority Swap | Revised study plan")
document.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
