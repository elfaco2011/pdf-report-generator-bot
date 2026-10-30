from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

HERE = Path(__file__).resolve().parent
ROOT_DIR = HERE.parent
EXAMPLES_DIR = ROOT_DIR / "examples"
DEFAULT_INPUT = EXAMPLES_DIR / "sample_input.csv"
DEFAULT_OUTPUT = ROOT_DIR / "output" / "report.pdf"

logging.basicConfig(
    level=logging.INFO,
    format="[PDFReportGenerator] %(levelname)s - %(message)s",
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a CSV table as a PDF report.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT,
                        help="input CSV (default: examples/sample_input.csv)")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT,
                        help="output PDF (default: output/report.pdf)")
    return parser.parse_args()


def _ensure_demo_input() -> None:
    if DEFAULT_INPUT.exists():
        return
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    with DEFAULT_INPUT.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Customer", "Country", "Revenue"])
        writer.writerow(["Alice", "USA", "1200"])
        writer.writerow(["Bob", "Italy", "900"])
        writer.writerow(["Charlie", "Spain", "700"])


def _load_table(input_path: Path):
    with input_path.open(newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [], []
        rows = [row for row in reader]
    return header, rows


def _build_pdf(header, rows, output_path: Path) -> None:
    doc = SimpleDocTemplate(str(output_path), pagesize=A4)
    styles = getSampleStyleSheet()

    data = [header] + rows
    table = Table(data, repeatRows=1)
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
    args = _parse_args()
    if args.input == DEFAULT_INPUT:
        _ensure_demo_input()
    if not args.input.exists():
        logging.error("Input file not found: %s", args.input)
        sys.exit(1)

    header, rows = _load_table(args.input)
    if not header:
        logging.warning("Input is empty, nothing to render.")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)
    _build_pdf(header, rows, args.output)
    logging.info("PDF report generated at %s", args.output)


if __name__ == "__main__":
    run()
