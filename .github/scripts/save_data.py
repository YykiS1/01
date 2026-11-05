import json
import os
from pathlib import Path

raw = os.environ.get("FINANCE_PAYLOAD", "")
if not raw:
    raise SystemExit("Missing FINANCE_PAYLOAD input")

data = json.loads(raw)
if not isinstance(data, dict) or not isinstance(data.get("db"), dict) or not isinstance(data.get("settings"), dict):
    raise SystemExit("Invalid finance data structure")

required = ("income", "expense", "ipad", "commission", "adoptable")
for key in required:
    if key not in data["db"] or not isinstance(data["db"][key], list):
        raise SystemExit(f"Invalid or missing list: db.{key}")

Path("finance_data.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)
print("finance_data.json updated")
