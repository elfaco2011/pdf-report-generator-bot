# PDF Report Generator Bot – Architecture

## Overview

This bot reads a CSV file with simple sales data and generates a PDF report
containing a table and a total amount summary.

- Input: `examples/sample_input.csv`
- Output: `examples/sample_output.pdf`
- Mode: DEMO only (no external APIs, no credentials).

## Components

- `src/main.py`
  - Entry point (`main()`)
  - Logging configuration
  - Path resolution (relative to the bot root)
  - CSV reading and validation
  - PDF generation using ReportLab

- `examples/`
  - `sample_input.csv` – sample data for the demo run
  - `sample_output.pdf` – generated report
  - `sample_output.csv` – optional, initially empty placeholder

## Data Flow

1. User runs `python src/main.py` from the bot root.
2. `main()` resolves the `examples/` directory relative to `src/`.
3. The bot reads `sample_input.csv` using `csv.DictReader`.
4. Rows are validated and cleaned (header check, numeric `amount`, corrupted rows skipped).
5. Valid rows are passed to the PDF generator.
6. The PDF is written to `examples/sample_output.pdf`.
7. Log messages describe each step and any issues found.

## Error Handling

- Missing input file: logged as an error, no PDF generated.
- CSV without header or missing required columns: error and abort.
- Corrupted rows (e.g. non-numeric amount): logged as warnings and skipped.
- No valid data rows: error and abort.

## Future Improvements

- Support for different report titles and output filenames via a config file.
- Support for multiple currencies and locales.
- CLI arguments for selecting input/output paths.
- Styling improvements in the PDF (branding, colors, logo).
