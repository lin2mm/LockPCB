# Decision 0003 — KiCad Source and CI Contract

- Date: 2026-10-16
- Status: implementation baseline; CI workflow must report actual tool results.

## Source and KiCad baseline

- GitHub branch source is authoritative; Drive is for handoff/reference/feedback/backup.
- KiCad 8 is the CI major-version target; workflow must check `kicad-cli version` and fail when the major differs. No `latest` container/tag.
- The board file uses a four-copper-layer placeholder per the current soft preference. Do not infer board thickness, copper weight, outline or stackup approval from it.
- The schematic is presently an annotated architecture/net-intent placeholder without symbols, pin-level wires, or actual electrical nets. This is stated on the schematic and in reports.

## Required checks and honest placeholder behavior

1. Run `kicad-cli version` and enforce KiCad 8.x.
2. Run `kicad-cli sch erc` and `kicad-cli pcb drc`; preserve command failures and output reports.
3. Compare the schematic's explicit `NET_NAME` and `SCHEMATIC_REF` intent annotations against the CSV net/BOM draft. Report as **block-level intent parity**, not electrical-netlist parity.
4. Export schematic netlist and inspect unconnected-net markers. With zero placed electrical symbols/pins, report `N/A — no electrical pins exist yet`, not a fabricated connectivity pass. Once pins are added, orphan nets cause failure.
5. Verify critical placeholder RefDes, BOM entries, TP1–TP5, and every TBD state exist in both plan and schematic annotations.
6. Upload ERC, DRC, version, parity/unconnected reports, netlist, and SVG previews even if a check fails. CI must not filter or downgrade real violations to get green.

A passing structural placeholder check is not evidence that the design is electrically complete, routable, mechanically fitted or ready to fabricate.

## CI observation

The first pushed workflow run on Ubuntu 24.04 installed KiCad 7 from the base Ubuntu repository. The explicit version guard failed (as intended), and the CLI showed `sch erc` was unavailable in that major. The workflow was corrected to add the KiCad 8.0 release PPA before installing KiCad, while retaining the runtime major-version guard. This first run is an honest failure, not a design pass; rerun CI after this change and report the actual KiCad 8 ERC/DRC result.
