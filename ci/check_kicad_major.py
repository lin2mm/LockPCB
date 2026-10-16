#!/usr/bin/env python3
import re
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: check_kicad_major.py <version-output> <expected-major>", file=sys.stderr)
    sys.exit(2)
path = Path(sys.argv[1])
expected = int(sys.argv[2])
if not path.is_file():
    print(f"FAIL: missing KiCad version report: {path}")
    sys.exit(1)
output = path.read_text(encoding="utf-8", errors="replace")
match = re.search(r"(?:KiCad\s+)?(\d+)\.(\d+)(?:\.\d+)?", output, re.IGNORECASE)
if not match:
    print(f"FAIL: could not parse kicad-cli version output: {output.strip()!r}")
    sys.exit(1)
actual = int(match.group(1))
if actual != expected:
    print(f"FAIL: expected KiCad major {expected}, got {actual}; refusing an unpinned toolchain.")
    sys.exit(1)
print(f"PASS: KiCad major is pinned to {actual}; full version: {output.strip()}")
