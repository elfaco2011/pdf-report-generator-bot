# PDF Report Generator Bot

Minimal PDF report generator that converts a CSV table (e.g. sales data) into a nicely formatted PDF table using `reportlab`.

## What it does
- Reads `examples/sample_input.csv` with tabular data.
- Builds a styled table (header row, grid lines, basic alignment).
- Outputs a one-page PDF to `examples/sample_output.pdf`.

## How to run (DEMO)
```bash
cd pdf-report-generator-bot
python src/main.py
```

The bot will create a demo `sample_input.csv` with a few rows if needed.

## Inputs & outputs
- **Input:** `examples/sample_input.csv` (any simple table).
- **Output:** `examples/sample_output.pdf` (PDF report).

## Dependencies
- Python 3.x
- `reportlab` (install with `pip install reportlab`).
