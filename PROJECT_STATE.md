# Project State — matchbox-smart-lock-pcb

Updated: 2026-10-16. Status: PRE-CAD / KiCad source skeleton + mechanical placeholders + block-level electrical intent.

## Source / scope

- GitHub private repository: `lin2mm/LockPCB`; work only on `arena/3b84c22f-lockpcb`.
- The assigned checkout is `/home/user/LockPCB`; `/home/user/smart-lock-pcb/` is absent.
- GitHub branch is authoritative for KiCad/electrical source. Google Drive remains handoff/reference/feedback/backup.
- No merge to `main`. No firmware flashing, purchasing, fabrication, or real hardware testing.

## Engineering state

- KiCad project: `pcb/LockPCB.kicad_pro`, `.kicad_sch`, `.kicad_pcb`.
- PCB: four-copper-layer starting preference; provisional 17.5 × 60 mm nominal outline and 20 × 65 mm review envelope. No components, pads, copper pours, nets, or tracks. All required mechanical labels are present; most zone graphics are not-to-scale placeholders. No verified mechanical fit or fabrication readiness.
- Schematic: A3 text-only architecture/signal-intent sheet. It lists 24 planning RefDes and 31 logical signal names but has no symbols, assigned pins, or connected electrical nets. Intent parity must not be reported as circuit/netlist completion.
- BOM MPNs and footprints remain TBD. Existing candidates are recommendations only. The interface draft now preserves conditional battery protection, motor sleep/fault/current feedback, lock/door/tamper sensing, and optional NFC/keypad/fingerprint interfaces. Wi-Fi and USB-C charging remain outside the baseline by default.
- Technical docs: `docs/POWER_TREE_AND_BUDGET.md`, `docs/CORE_ZONING.md`, `docs/MECHANICAL_INPUTS.md`, CSV drafts, decision records, and `docs/CAD_SOURCE_RECONCILIATION.md`.
- Earlier Drive CAD records include a candidate aluminum shell with conflicting historical envelope reports: `sx-db-4.stp` at 39.800 × 22.500 × 90.500 mm versus an FCStd-derived assembly bound of approximately 43.09 × 22.51 × 92.56 mm. The mismatch and product/revision identity are unresolved; neither replaces a current `TBD` or implies board fit. See `docs/CAD_SOURCE_RECONCILIATION.md`.
- Visual preview: [engineering overview on GitHub](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/docs/previews/engineering-overview.png). It is illustrative only, not to scale.

## Blocking inputs

1. Exact 18650 cell and holder/contact, including true envelope and protection approach.
2. Verified maximum PCB length, width, thickness, and internal housing clearance.
3. Motor model, operating voltage, startup/stall current, duty and torque requirements.
4. Gearbox/coupler/output-shaft geometry and axis datum.
5. Whether USB-C/on-board charging is required.
6. Confirmation and current geometry of enclosure/lockbody metal, antenna area, service access, and product revision.

Unknown dimensions and values remain TBD. No manufacturing release, electrical closure, or hardware validation is claimed.

## Validation

- Local KiCad CLI is unavailable. Local static checks passed on engineering source commit `6b22eba`: placeholder structure, CSV/schematic intent parity (24 RefDes / 31 names), MPN/footprint TBD checks, and balanced S-expressions.
- GitHub Actions run [38884689186](https://github.com/lin2mm/LockPCB/actions/runs/38884689186) passed on commit `9daf63d39e440f646d36b590c77d434e418ae063`. KiCad 8 install/version gate, ERC, DRC, netlist export, intent parity, structure checks, and SVG exports all completed. The no-electrical-pins status remains N/A by design. CI success validates only this PRE-CAD placeholder state.
- Artifact: `kicad-reports-38884689186` (artifact ID `12039496470`), available from the Actions run page.

Never merge `main`; push only to `arena/3b84c22f-lockpcb`.
