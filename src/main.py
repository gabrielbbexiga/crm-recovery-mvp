from __future__ import annotations

import argparse
import csv
from pathlib import Path

from .models import LeadRecord


def load_records(input_path: Path) -> list[LeadRecord]:
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return [LeadRecord.model_validate(row) for row in reader]


def export_records(records: list[LeadRecord], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for record in records:
        row = record.model_dump(mode="json")
        row["missing_fields"] = "|".join(record.missing_fields)
        rows.append(row)

    if not rows:
        raise ValueError("Input CSV contains no data rows.")

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def run(input_path: str, output_path: str) -> int:
    records = load_records(Path(input_path))
    export_records(records, Path(output_path))
    return len(records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize a synthetic dormant-lead CSV for the CRM Recovery MVP."
    )
    parser.add_argument("input_csv", help="Path to the input CSV")
    parser.add_argument("output_csv", help="Path for the normalized CSV")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = run(args.input_csv, args.output_csv)
    print(f"Normalized {count} records -> {args.output_csv}")


if __name__ == "__main__":
    main()
