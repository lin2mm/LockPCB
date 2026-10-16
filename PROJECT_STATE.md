# Project State — matchbox-smart-lock-pcb

- Updated: 2026-10-16
- Status: PRE-CAD / KiCad source skeleton + mechanical placeholders + block-level architecture intent
- Authoritative source: GitHub repository `lin2mm/LockPCB`, current Arena branch `arena/3b84c22f-lockpcb`
- Workspace note: this environment checkout is `/home/user/LockPCB`; requested `/home/user/smart-lock-pcb/` did not exist.
- Main merge: not performed and must not be performed during this session.

## Current engineering state

- KiCad source files: `pcb/LockPCB.kicad_pro`, `pcb/LockPCB.kicad_sch`, `pcb/LockPCB.kicad_pcb`.
- PCB: four-copper-layer starting preference, provisional 17.5 × 60 mm board outline, mechanical/user-layer labels and one native temporary no-component keepout. No footprints, pads, copper pours, nets or tracks. All mechanical envelopes except the illustrative starting board rectangle are unscaled placeholders.
- Schematic: architecture text/block and signal-intent annotations only; no symbols, connected pins, or electrical netlist. It is not a completed schematic.
- Candidate architecture and power budget: `docs/POWER_TREE_AND_BUDGET.md`, `docs/CORE_ZONING.md`; no numeric loads, MPNs or footprints chosen.
- Draft interfaces: `docs/BOM_DRAFT.csv`, `docs/PINOUT_DRAFT.csv`, `docs/NETLIST_DRAFT.csv`.
- CI: `.github/workflows/kicad-ci.yml`, targeting KiCad 8.x on Ubuntu 24.04, runs version guard, ERC, DRC, placeholder parity, netlist unconnected marker check, structural checks and SVG exports; uploads artifacts on failure. Actions results must be checked after push.
- Decisions: `decisions/`; six input blockers in decision 0002.

## Blockers

1. Final 18650 model and holder/contact.
2. Maximum PCB length, width and thickness.
3. Motor part/rated voltage/start and stall current.
4. Shaft axis datum and top gearbox/coupler dimensions.
5. Whether USB-C board charging is required.
6. Metal enclosure/lockbody geometry.

No manufacturing release, hardware validation, real electrical closure, or “ready to fabricate” claim is permitted.

## Checks

- Local KiCad CLI is not installed in the workspace. Static source/CSV/script checks can be run locally; actual ERC/DRC and artifact outputs require the GitHub Actions runner and must be reported from its run.
- Record the actual branch HEAD and Actions run result in the session handoff at close; never merge main.
