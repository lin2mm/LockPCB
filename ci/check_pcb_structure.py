#!/usr/bin/env python3
"""Structural check of required KiCad placeholder layers and board geometry."""
import argparse
from pathlib import Path
import sys

REQUIRED = (
    "BATTERY_KEEP_OUT",
    "BATTERY_CONTACT_ZONE",
    "PCB_MAX_OUTLINE",
    "MOTOR_GEARBOX_ZONE",
    "SHAFT_AXIS",
    "NFC_ANTENNA_ZONE",
    "METAL_LOCKBODY_ZONE",
    "SERVICE_ACCESS_ZONE",
    "NO_COMPONENT_ZONE",
)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("pcb", type=Path)
    p.add_argument("report", type=Path)
    a = p.parse_args()
    errors = []
    if not a.pcb.is_file():
        errors.append(f"PCB file missing: {a.pcb}")
        content = ""
    else:
        content = a.pcb.read_text(encoding="utf-8")
    for zone in REQUIRED:
        if zone not in content:
            errors.append(f"Required zone label missing: {zone}")
    for layer in ('"F.Cu" signal', '"In1.Cu" signal', '"In2.Cu" signal', '"B.Cu" signal'):
        if layer not in content:
            errors.append(f"Four-layer placeholder stack missing layer {layer}")
    if '"Edge.Cuts"' not in content or "(gr_line (start 0 0)" not in content:
        errors.append("Edge.Cuts board-outline placeholder not found")
    if '(keepout ' not in content or '"NO_COMPONENT_ZONE_PLACEHOLDER"' not in content:
        errors.append("Native temporary NO_COMPONENT_ZONE keepout not found")
    if "NOT FOR FABRICATION" not in content and "NOT READY FOR FAB" not in content:
        errors.append("Board must carry a not-for-fabrication warning")
    result = ("FAIL\n" if errors else "PASS — required KiCad placeholders are present; dimensions remain unverified.\n")
    if errors:
        result += "\n".join(f"ERROR: {e}" for e in errors) + "\n"
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text(result, encoding="utf-8")
    print(result, end="")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
