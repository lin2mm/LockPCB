# LockPCB — Session Handoff

**Start here:** [`README.md`](README.md), then [`PROJECT_STATE.md`](PROJECT_STATE.md), [`docs/MECHANICAL_SOURCE_BASELINE.md`](docs/MECHANICAL_SOURCE_BASELINE.md), and [`docs/FILE_NAMING_RULES.md`](docs/FILE_NAMING_RULES.md). These are the current entry points; do not use older CAD-summary narratives as project truth.

## Repository and validation

- Repository: private `lin2mm/LockPCB`; fixed working branch `arena/3b84c22f-lockpcb`; do not switch branches, push elsewhere, or merge `main`.
- KiCad source: `pcb/LockPCB.kicad_pro`, `.kicad_sch`, `.kicad_pcb`.
- The current board outline is derived from the designer-confirmed 14 × 50 mm PCB drawing. Hole circles remain graphics, not actual drill/pad definitions. The electrical design is incomplete and mechanical fit is unverified.
- [CI run 38900003033](https://github.com/lin2mm/LockPCB/actions/runs/38900003033) passed on cleanup baseline commit `0d5895dbd61aa7f1c864f90f2ba510dbf238ac89`. CI success is not fit, electrical safety, or fabrication approval.
- No firmware, purchasing, fabrication, or real hardware testing is in scope.

## Next step

Continue from the current source baseline. Reconcile the sampled cell identity (18500 vs 18650), map the selected confirmed CAD revision to the assembled enclosure, validate the contour against native-mm source, then resolve contact/drill and motor/shaft interfaces before implementing real pads, schematic pins, or routing. Keep unknowns TBD and do not claim fit or fabrication readiness.
