"""
API Import Validator

Purpose:
- Validate imported contact records from API response examples.
- Detect duplicate IDs, missing required fields, and invalid email formats.
- Demonstrate that valid JSON can still contain defective business data.

How to run from the repository root:
    python validation/api_import_validator.py
"""

import json
import re
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
FILES_TO_VALIDATE = [
    REPO_ROOT / "datasets" / "api_contacts_response_valid.json",
    REPO_ROOT / "datasets" / "api_contacts_response_dirty.json",
]

REQUIRED_FIELDS = [
    "id",
    "name",
    "company",
    "email",
    "status",
]

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# ------------------------------------------------------------
# 3. Validate one API response file
# ------------------------------------------------------------
def validate_api_contacts(file_path: Path) -> list:
    """
    Validate one API contacts response file.

    Parameters:
    - file_path: path to a JSON API response.

    Returns:
    - A list of issue strings found during validation.
    """

    issues = []
    seen_ids = set()

    print("=" * 70)
    print(f"Checking: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8") as file_handle:
            payload = json.load(file_handle)

        contacts = payload.get("contacts", [])

        if not isinstance(contacts, list):
            issues.append("contacts field is missing or is not a list")
            return issues

        for index, contact in enumerate(contacts, start=1):
            contact_id = str(contact.get("id", "")).strip()

            for field in REQUIRED_FIELDS:
                value = str(contact.get(field, "")).strip()
                if not value:
                    issues.append(f"Contact {index}: missing required field '{field}'")

            if contact_id:
                if contact_id in seen_ids:
                    issues.append(f"Contact {index}: duplicate id {contact_id}")
                seen_ids.add(contact_id)

            email = str(contact.get("email", "")).strip()
            if email and not EMAIL_PATTERN.match(email):
                issues.append(f"Contact {index}: invalid email format: {email}")

    except FileNotFoundError:
        issues.append("File not found")

    except json.JSONDecodeError as error:
        issues.append(f"Invalid JSON: {error}")

    except Exception as error:
        issues.append(f"Unexpected validation problem: {error}")

    return issues


# ------------------------------------------------------------
# 4. Main execution
# ------------------------------------------------------------
total_issues = 0

for api_file in FILES_TO_VALIDATE:
    file_issues = validate_api_contacts(api_file)

    if not file_issues:
        print("[OK] No API import issues found")
    else:
        print("[WARN] API import issues found:")
        for issue in file_issues:
            print(f"- {issue}")

    total_issues += len(file_issues)

print("=" * 70)
print("[DONE] API import validation completed.")
print(f"[SUMMARY] Total issues found: {total_issues}")
