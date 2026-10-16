# LockPCB — Session Handoff

**Start here:** [`README.md`](README.md), then [`PROJECT_STATE.md`](PROJECT_STATE.md), [`docs/PRODUCT_VARIANTS.md`](docs/PRODUCT_VARIANTS.md), [`docs/CAD_VARIANT_COMPARISON.md`](docs/CAD_VARIANT_COMPARISON.md), [`docs/MECHANICAL_SOURCE_BASELINE.md`](docs/MECHANICAL_SOURCE_BASELINE.md), and [`docs/FILE_NAMING_RULES.md`](docs/FILE_NAMING_RULES.md). These are the current entry points; do not use older CAD-summary narratives as project truth.

## Repository and validation

- Repository: private `lin2mm/LockPCB`; fixed working branch `arena/3b84c22f-lockpcb`; do not switch branches, push elsewhere, or merge `main`.
- KiCad source: `pcb/LockPCB.kicad_pro`, `.kicad_sch`, `.kicad_pcb`.
- The current board outline is derived from the designer-confirmed 14 × 50 mm PCB drawing. Hole circles remain graphics, not actual drill/pad definitions. The electrical design is incomplete and mechanical fit is unverified.
- [CI run 38902175365](https://github.com/lin2mm/LockPCB/actions/runs/38902175365) passed on V1 18650 baseline commit `5709a24fc6d6f4be7643af2b7ca46d9fbd778f87`. CI success is not fit, electrical safety, or fabrication approval.
- No firmware, purchasing, fabrication, or real hardware testing is in scope.

## Next step

Continue V1 PCB design using 1S 18650 as the user-selected form-factor target. Do not reopen the form-factor choice; keep exact MPN/electrical limits TBD. The factory sample appears 18500-like, so verify whether a separate enclosure variant is needed before claiming fit. Continue non-cell-specific PCB work, check the contour against native-mm source, and resolve motor/shaft interfaces. The potential second size series is deferred. Do not claim fit or fabrication readiness.
