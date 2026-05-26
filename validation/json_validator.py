"""
JSON Validator

Purpose:
- Validate JSON files used in the SME Automation QA Lab.
- Detect malformed JSON before downstream processing.
- Support QA review of API responses and AI-assisted automation outputs.

How to run from the repository root:
    python validation/json_validator.py
"""

import json
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
# 2. Define files to validate
# ------------------------------------------------------------
# These files are expected to be valid JSON.
# Some may still be defective from a business or QA perspective,
# but this script only checks JSON syntax.
FILES_TO_VALIDATE = [
    REPO_ROOT / "datasets" / "api_contacts_response_valid.json",
    REPO_ROOT / "datasets" / "api_contacts_response_dirty.json",
    REPO_ROOT / "outputs" / "email_to_crm_expected_output.json",
    REPO_ROOT / "outputs" / "email_to_crm_defective_output.json",
    REPO_ROOT / "outputs" / "api_import_expected_summary.json",
    REPO_ROOT / "outputs" / "api_import_defective_summary.json",
]


# ------------------------------------------------------------
# 3. Validate JSON files
# ------------------------------------------------------------
# Each file is opened and parsed with json.load().
# If parsing fails, the file is not valid JSON.
def validate_json_file(file_path: Path) -> bool:
    """
    Validate one JSON file.

    Parameters:
    - file_path: path to the JSON file.

    Returns:
    - True if the file is valid JSON.
    - False if the file is missing or invalid.
    """

    print("=" * 70)
    print(f"Checking: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8") as file_handle:
            json.load(file_handle)

        print("[OK] Valid JSON")
        return True

    except FileNotFoundError:
        print("[ERROR] File not found")
        return False

    except json.JSONDecodeError as error:
        print("[ERROR] Invalid JSON")
        print(f"Reason: {error}")
        return False

    except Exception as error:
        print("[ERROR] Unexpected validation problem")
        print(f"Reason: {error}")
        return False


# ------------------------------------------------------------
# 4. Main execution
# ------------------------------------------------------------
# Track how many files pass or fail syntax validation.
passed = 0
failed = 0

for json_file in FILES_TO_VALIDATE:
    if validate_json_file(json_file):
        passed += 1
    else:
        failed += 1

print("=" * 70)
print("[DONE] JSON validation completed.")
print(f"[SUMMARY] Passed: {passed}")
print(f"[SUMMARY] Failed: {failed}")

if failed > 0:
    raise SystemExit(1)
