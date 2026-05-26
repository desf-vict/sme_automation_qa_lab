"""
CSV Inventory Validator

Purpose:
- Validate customer inventory CSV files.
- Detect common SME automation data-quality issues.
- Support QA checks before generating spreadsheet or report outputs.

How to run from the repository root:
    python validation/csv_inventory_validator.py
"""

import csv
from pathlib import Path


# ------------------------------------------------------------
# 1. Define repository paths
# ------------------------------------------------------------
# __file__ points to this script.
# Path(__file__).parent gives the validation folder.
VALIDATION_DIR = Path(__file__).parent

# The repository root is one folder above /validation.
REPO_ROOT = VALIDATION_DIR.parent


# ------------------------------------------------------------
# 2. Define input files
# ------------------------------------------------------------
# The clean file should produce no serious issues.
# The dirty file intentionally contains QA defects.
FILES_TO_VALIDATE = [
    REPO_ROOT / "datasets" / "customer_inventory_clean.csv",
    REPO_ROOT / "datasets" / "customer_inventory_dirty.csv",
]

REQUIRED_COLUMNS = [
    "item_id",
    "item_name",
    "quantity",
    "unit_price",
    "category",
]


# ------------------------------------------------------------
# 3. Helper validation functions
# ------------------------------------------------------------
def is_integer(value: str) -> bool:
    """
    Check whether a value can be safely interpreted as an integer.

    Parameters:
    - value: text value from the CSV.

    Returns:
    - True if the value is an integer.
    - False otherwise.
    """

    try:
        int(value)
        return True
    except ValueError:
        return False


def is_decimal(value: str) -> bool:
    """
    Check whether a value can be safely interpreted as a decimal number.

    Parameters:
    - value: text value from the CSV.

    Returns:
    - True if the value is numeric.
    - False otherwise.
    """

    try:
        float(value)
        return True
    except ValueError:
        return False


# ------------------------------------------------------------
# 4. Validate one CSV file
# ------------------------------------------------------------
def validate_inventory_csv(file_path: Path) -> list:
    """
    Validate one inventory CSV file.

    Parameters:
    - file_path: path to the CSV file.

    Returns:
    - A list of issue strings found during validation.
    """

    issues = []
    seen_item_ids = set()

    print("=" * 70)
    print(f"Checking: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8", newline="") as file_handle:
            reader = csv.DictReader(file_handle)

            # Confirm that all required columns exist.
            missing_columns = [
                column for column in REQUIRED_COLUMNS
                if column not in (reader.fieldnames or [])
            ]

            if missing_columns:
                issues.append(f"Missing required columns: {missing_columns}")
                return issues

            for row_number, row in enumerate(reader, start=2):
                item_id = (row.get("item_id") or "").strip()
                item_name = (row.get("item_name") or "").strip()
                quantity = (row.get("quantity") or "").strip()
                unit_price = (row.get("unit_price") or "").strip()

                if not item_id:
                    issues.append(f"Row {row_number}: missing item_id")

                if item_id in seen_item_ids:
                    issues.append(f"Row {row_number}: duplicate item_id {item_id}")

                if item_id:
                    seen_item_ids.add(item_id)

                if not item_name:
                    issues.append(f"Row {row_number}: missing item_name")

                if not quantity:
                    issues.append(f"Row {row_number}: missing quantity")
                elif not is_integer(quantity):
                    issues.append(f"Row {row_number}: quantity is not an integer: {quantity}")
                elif int(quantity) < 0:
                    issues.append(f"Row {row_number}: quantity is negative: {quantity}")

                if not unit_price:
                    issues.append(f"Row {row_number}: missing unit_price")
                elif not is_decimal(unit_price):
                    issues.append(f"Row {row_number}: unit_price is not numeric: {unit_price}")
                elif float(unit_price) < 0:
                    issues.append(f"Row {row_number}: unit_price is negative: {unit_price}")

    except FileNotFoundError:
        issues.append("File not found")

    except Exception as error:
        issues.append(f"Unexpected validation problem: {error}")

    return issues


# ------------------------------------------------------------
# 5. Main execution
# ------------------------------------------------------------
# Print a clear result for each file.
total_issues = 0

for csv_file in FILES_TO_VALIDATE:
    file_issues = validate_inventory_csv(csv_file)

    if not file_issues:
        print("[OK] No CSV data-quality issues found")
    else:
        print("[WARN] CSV data-quality issues found:")
        for issue in file_issues:
            print(f"- {issue}")

    total_issues += len(file_issues)

print("=" * 70)
print("[DONE] CSV inventory validation completed.")
print(f"[SUMMARY] Total issues found: {total_issues}")
