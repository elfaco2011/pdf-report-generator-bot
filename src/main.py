from __future__ import annotations

import csv
import logging
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

HERE = Path(__file__).resolve().parent
EXAMPLES_DIR = HERE.parent / "examples"
INPUT_PATH = EXAMPLES_DIR / "sample_input.csv"
OUTPUT_PATH = EXAMPLES_DIR / "sample_output.pdf"

logging.basicConfig(
    level=logging.INFO,
    format="[PDFReportGenerator] %(levelname)s - %(message)s",
)


def _ensure_demo_input() -> None:
    if INPUT_PATH.exists():
        return
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    with INPUT_PATH.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Customer", "Country", "Revenue"])
        writer.writerow(["Alice", "USA", "1200"])
        writer.writerow(["Bob", "Italy", "900"])
        writer.writerow(["Charlie", "Spain", "700"])


def _load_table():
    with INPUT_PATH.open(newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [], []
        rows = [row for row in reader]
    return header, rows


def _build_pdf(header, rows) -> None:
    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4)
    styles = getSampleStyleSheet()

    data = [header] + rows
    table = Table(data)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    story = [Paragraph("Sales Report", styles["Title"]), Spacer(1, 12), table]
    doc.build(story)


def run() -> None:
    _ensure_demo_input()
    if not INPUT_PATH.exists():
        logging.error("Input file not found: %s", INPUT_PATH)
        return

    header, rows = _load_table()
    if not header:
        logging.warning("Input is empty, nothing to render.")
        return

    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    _build_pdf(header, rows)
    logging.info("PDF report generated at %s", OUTPUT_PATH)


if __name__ == "__main__":
    run()
