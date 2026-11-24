"""Loading Screen Gold: a tip in 200 characters.

Deterministic, no network. Writes the single entry line to /output/entry.txt.
"""

import hashlib
import os

ENTRY_LINE = "Tip: if it works and you don't know why, don't touch it. That's not a bug, that's a pet."

assert len(ENTRY_LINE) <= 200, f"entry is {len(ENTRY_LINE)} chars, over the 200-char limit"
assert "\n" not in ENTRY_LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY_LINE)

print(f"entry ({len(ENTRY_LINE)} chars, sha256 {hashlib.sha256(ENTRY_LINE.encode()).hexdigest()}):")
print(ENTRY_LINE)
