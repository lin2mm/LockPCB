#!/usr/bin/env python3
"""Validate placeholder-level schematic/BOM/net intent and report netlist status honestly."""
from __future__ import annotations
import argparse
import csv
import re
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--schematic", type=Path, required=True)
    ap.add_argument("--bom", type=Path, required=True)
    ap.add_argument("--nets", type=Path, required=True)
    ap.add_argument("--netlist", type=Path, required=True)
    ap.add_argument("--report", type=Path, required=True)
    args = ap.parse_args()
    errors: list[str] = []
    notes: list[str] = []
    for path in (args.schematic, args.bom, args.nets, args.netlist):
        if not path.is_file():
            errors.append(f"Missing required input: {path}")
    if errors:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text("FAIL\n" + "\n".join(errors) + "\n")
        print(args.report.read_text(), end="")
        return 1

    schematic = args.schematic.read_text(encoding="utf-8")
    bom_rows = list(csv.DictReader(args.bom.open(encoding="utf-8", newline="")))
    net_rows = list(csv.DictReader(args.nets.open(encoding="utf-8", newline="")))

    bom_refs = {r["refdes"].strip() for r in bom_rows if r.get("refdes", "").strip()}
    ref_annotation = re.search(r'\(text "SCHEMATIC_REF: ([^"]+)"', schematic)
    if not ref_annotation:
        errors.append("Schematic has no SCHEMATIC_REF intent annotation")
        schematic_refs: set[str] = set()
    else:
        schematic_refs = set(ref_annotation.group(1).split())
    if bom_refs != schematic_refs:
        errors.append(
            "BOM/schematic placeholder RefDes mismatch: "
            f"BOM-only={sorted(bom_refs - schematic_refs)}; "
            f"schematic-only={sorted(schematic_refs - bom_refs)}"
        )
    required_tps = {f"TP{i}" for i in range(1, 8)}
    if not required_tps.issubset(bom_refs):
        errors.append(f"BOM missing critical test points: {sorted(required_tps - bom_refs)}")
    if not required_tps.issubset(schematic_refs):
        errors.append(f"Schematic intent missing critical test points: {sorted(required_tps - schematic_refs)}")
    if not re.search(r'\(text "BLOCK REFERENCES: [^"]+"', schematic):
        errors.append("Schematic block reference inventory annotation missing")

    planned_nets = {r["signal"].strip() for r in net_rows if r.get("signal", "").strip()}
    schematic_nets = set(re.findall(r'\(text "NET_NAME: ([^"]+)"', schematic))
    if planned_nets != schematic_nets:
        errors.append(
            "Net-intent label parity mismatch: "
            f"CSV-only={sorted(planned_nets - schematic_nets)}; "
            f"schematic-only={sorted(schematic_nets - planned_nets)}"
        )
    notes.append(
        f"PASS: block-level schematic intent parity ({len(schematic_refs)} RefDes placeholders, "
        f"{len(planned_nets)} planned signal names). This is not pin-level/electrical connectivity parity."
    )

    for row in bom_rows:
        ref = row.get("refdes", "?")
        if row.get("manufacturer_part_number", "").strip().upper() != "TBD":
            errors.append(f"{ref}: MPN must remain TBD until selected")
        if row.get("footprint", "").strip().upper() != "TBD":
            errors.append(f"{ref}: footprint must remain TBD until selected")
    notes.append("PASS: BOM MPNs/footprints remain explicitly TBD; no unapproved package data was added.")

    netlist = args.netlist.read_text(encoding="utf-8", errors="replace")
    component_refs = set(re.findall(r'\(comp\s+\(ref\s+"([^"]+)"\)', netlist))
    unconnected = sorted(set(re.findall(r'\(name\s+"(unconnected-[^"]+)"', netlist, re.IGNORECASE)))
    if unconnected:
        errors.append(f"Unconnected net markers found in exported netlist: {unconnected}")
    elif not component_refs:
        notes.append(
            "N/A: exported KiCad netlist contains no electrical component pins; schematic is currently a text-only architecture placeholder."
        )
    else:
        notes.append(f"PASS: no KiCad unconnected-net markers found across {len(component_refs)} netlisted references.")

    args.report.parent.mkdir(parents=True, exist_ok=True)
    report = ("FAIL\n" if errors else "PASS WITH EXPLICIT PRE-CAD LIMITATIONS\n") + "\n".join(notes + [f"ERROR: {e}" for e in errors]) + "\n"
    args.report.write_text(report, encoding="utf-8")
    print(report, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
