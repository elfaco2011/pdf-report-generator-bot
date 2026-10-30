# PDF Report Generator Bot

## Problem
Turning a CSV table into a clean, printable PDF report by hand is repetitive.

## Example output
Generated from `examples/sample_input.csv` (full file: `examples/sample_output.pdf`):

![Sample PDF report](docs/sample_output.png)

## What it does
- Reads a CSV file; the first row is used as the table header.
- Renders all rows as a table on an A4 page, with a grey header row, grid lines and centred cells.
- Adds the title "Sales Report" above the table.
- Writes the result to `examples/sample_output.pdf`.

Values are printed as they appear in the CSV: no totals, sorting or number formatting.

## Quick start
Tested with Python 3.11.

```bash
pip install -r requirements.txt
python src/main.py
```

## Sample data
`examples/sample_input.csv` contains three customers with country and revenue.
If the file is missing, the script recreates it before running.

## Adapting it to your data
Replace `examples/sample_input.csv` with any CSV table (header in the first row, same number of columns in every row).
To change the title or the file paths, edit the `"Sales Report"` string and `INPUT_PATH` / `OUTPUT_PATH` in `src/main.py`.
