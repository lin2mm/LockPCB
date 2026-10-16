# Project State — matchbox-smart-lock-pcb

Updated: 2026-10-16. Status: PRE-CAD / KiCad source skeleton + mechanical placeholders + block-level electrical intent.

## Source / scope

- GitHub private repository: `lin2mm/LockPCB`; work only on `arena/3b84c22f-lockpcb`.
- The assigned checkout is `/home/user/LockPCB`; `/home/user/smart-lock-pcb/` is absent.
- GitHub branch is authoritative for KiCad/electrical source. Google Drive remains handoff/reference/feedback/backup.
- No merge to `main`. No firmware flashing, purchasing, fabrication, or real hardware testing.

## Engineering state

- KiCad project: `pcb/LockPCB.kicad_pro`, `.kicad_sch`, `.kicad_pcb`.
- PCB: four-copper-layer starting preference. KiCad `Edge.Cuts` now uses the designer-DWG-derived notched 14 × 50 mm contour, with source-reference rings for two 3.1 mm holes; hole drilling/plating/contact pads are deliberately not yet implemented. DWG calls out 1.20 mm board thickness. Motor/RF/service/metal zones remain Agent proposals. The DXF conversion warning/unit-header inconsistency requires native-CAD verification before fabrication. No components, electrical pads, copper pours, nets, or tracks. No verified fit to the user's sampled/assembled housing, cell or motor; no fabrication readiness.
- Schematic: A3 text-only architecture/signal-intent sheet. It lists 24 planning RefDes and 31 logical signal names but has no symbols, assigned pins, or connected electrical nets. Intent parity must not be reported as circuit/netlist completion.
- BOM MPNs and footprints remain TBD. Existing candidates are recommendations only. The interface draft now preserves conditional battery protection, motor sleep/fault/current feedback, lock/door/tamper sensing, and optional NFC/keypad/fingerprint interfaces. Wi-Fi and USB-C charging remain outside the baseline by default.
- Technical docs: `docs/POWER_TREE_AND_BUDGET.md`, `docs/CORE_ZONING.md`, `docs/MECHANICAL_INPUTS.md`, CSV drafts, decision records, `docs/CAD_SOURCE_RECONCILIATION.md`, and parsed source measurements in `docs/FACTORY_PROTOTYPE_GEOMETRY_REPORT.md`.
- User confirms the designer-approved enclosure part CAD has been sampled and the shell parts assembled. The factory-prototype STEP's `SX-DB-4` mesh is 39.80 × 22.50 × 90.494 mm, agreeing with the designer-confirmed standalone shell STEP (39.800 × 22.500 × 90.500 mm). A separate designer-confirmed FCStd assembly yields about 43.09 × 22.51 × 92.56 mm overall in the inherited handoff; assembly placement/revision mapping remains to be reconciled. The physical enclosure is confirmed assembled, but the Agent's updated PCB/cell/contact/motor fit has not been demonstrated.
- User clarified that all eight files in Drive folder `锁-PCB-外壳设计稿-260729` are designer-confirmed prototype documents already sent to the factory, and CAD/DWG/STEP files inside designer-provided ZIPs are also confirmed drawings. DWG, JPG and STEP geometry agree on a 14 × 50 mm PCB, 1.20 mm thickness and two Ø3.10 mm end holes. The STEP node `DC-18650-SX` is modeled at 18 × 18 × 50 mm (18500-sized) despite its 18650 label; this supports the TXT's 18500 entry, while the earlier user-confirmed 18650 baseline still needs sample/BOM confirmation. Previous-session agent PCB layouts are capability-test placeholders, not product geometry. Full contour migration and surface-clearance validation remain open. See `docs/FACTORY_PROTOTYPE_GEOMETRY_REPORT.md` and `docs/CAD_SOURCE_RECONCILIATION.md`.
- Visual preview: [engineering overview on GitHub](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/docs/previews/engineering-overview.png). It is illustrative only, not to scale.

## Blocking inputs

1. Confirm the actual factory-sampled cell SKU/BOM and terminal/contact/protection design. Current STEP geometry (18 × 18 × 50 mm) supports 18500 despite the `DC-18650-SX` label; earlier project baseline still says 18650.
2. Verify the imported 14 × 50 mm contour/notch datums against a clean native-mm export; implement the two through-holes/contact pads only after drill, plating and polarity are approved; then perform true surface/tolerance checks against the sampled/assembled housing. STEP AABBs show a preliminary 0.6 mm board-to-cell separation on one axis, not a fit pass.
3. Motor model, operating voltage, startup/stall current, duty and torque requirements.
4. Gearbox/coupler/output-shaft geometry and axis datum.
5. Whether USB-C/on-board charging is required.
6. Confirmation and current geometry of enclosure/lockbody metal, antenna area, service access, and product revision.

Unknown dimensions and values remain TBD. No manufacturing release, electrical closure, or hardware validation is claimed.

## Validation

- Local KiCad CLI is unavailable. Local static checks passed on engineering source commit `6b22eba`: placeholder structure, CSV/schematic intent parity (24 RefDes / 31 names), MPN/footprint TBD checks, and balanced S-expressions.
- Latest completed GitHub Actions run [38893183352](https://github.com/lin2mm/LockPCB/actions/runs/38893183352) passed on earlier commit `50c56a25067d4e2783efe6894af1a555608f478c`, when the board still had the Agent test outline. It does not validate the newly imported DWG contour. Local KiCad CLI is unavailable; current verification is limited to structural checks and source-coordinate checks, not ERC/DRC or a KiCad GUI parse.
- Artifact: `kicad-reports-38892456638` (artifact ID `12042730600`), available from the Actions run page.

Never merge `main`; push only to `arena/3b84c22f-lockpcb`.
