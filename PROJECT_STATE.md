# LockPCB — 当前项目状态

Updated: 2026-10-16. Status: **PCB engineering skeleton / source-derived mechanical outline / electrical and fit validation open.**

## Source of truth and scope

- Private repository: `lin2mm/LockPCB`; work only on `arena/3b84c22f-lockpcb`; do not merge `main`.
- Checkout: `/home/user/LockPCB`. GitHub branch tree is the source of truth for the editable KiCad project. Designer-confirmed source CAD/DWG/STEP remains in Google Drive and original archives; preserve those inputs.
- This phase is PCB engineering only: no firmware flashing, purchasing, fabrication, or real hardware test.
- Read `docs/PRODUCT_VARIANTS.md` and `docs/MECHANICAL_SOURCE_BASELINE.md` before mechanical changes. They separate the V1 18650 design target from the supplied factory/sample geometry and record remaining validation items.

## Current KiCad source

- Files: `pcb/LockPCB.kicad_pro`, `pcb/LockPCB.kicad_sch`, `pcb/LockPCB.kicad_pcb`.
- PCB outline: source-derived notched 14 × 50 mm envelope in `Edge.Cuts`; visual references for two Ø3.10 mm holes and ~Ø5 mm concentric features are not drills/pads. DWG calls out 1.20 mm thickness. Native-mm/source datum verification remains open because the conversion emitted warnings and inconsistent unit metadata.
- The nine required mechanical labels exist as annotated layers. The `BATTERY_KEEP_OUT` drawing now shows a provisional 19 × 70 mm V1 18650 planning envelope only; it is not an enforced KiCad keepout and is not proof of clearance or fit. `NO_COMPONENT_ZONE` is also provisional.
- The PCB has no actual component footprints, electrical pads, nets, copper pours, or routed tracks. The A3 schematic is text-only architecture and signal intent, not pin-level connectivity.
- First PCB variant (V1) now targets one 1S 18650 form factor per user direction; exact cell MPN, protected-cell envelope, contacts and electrical limits remain TBD. A second product series with different dimensions may follow; do not force it into V1 geometry.

## Mechanical-source baseline

- The designer-confirmed package under Drive folder `锁-PCB-外壳设计稿-260729` contains eight factory prototype documents already sent for sampling; the user also confirms designer enclosure parts have been sampled and assembled. Use the physical assembled enclosure as the mechanical anchor.
- The DWG/JPG/STEP-derived PCB plan is 50 × 14 mm, with 1.20 mm DWG thickness callout and two Ø3.10 mm end holes. Full coordinate mapping and evidence limits are in the mechanical baseline.
- V1 PCB design target is 1S 18650. The factory functional TXT says 18500, while the STEP node `DC-18650-SX` measures about 18 × 18 × 50 mm. The supplied enclosure/sample package may therefore represent a 18500-like size; V1 fit to it is not confirmed. Exact 18650 SKU and protected-cell envelope remain TBD.
- Board-to-enclosure/cell/contact/motor fit, tolerances, and product-revision mapping have not been demonstrated. No fabrication readiness is claimed.

## Validation

- V1 18650 baseline commit: `5709a24fc6d6f4be7643af2b7ca46d9fbd778f87` on the session branch.
- [GitHub Actions run 38902175365](https://github.com/lin2mm/LockPCB/actions/runs/38902175365) passed KiCad 8 load/export, ERC/DRC, netlist export, structure/intent checks and SVG exports. This validates the checked files under CI, not physical fit, electrical completeness, or fabrication readiness.
- Local KiCad CLI/GUI is unavailable in this workspace.

## Next engineering gates

1. Establish whether the sampled enclosure/CAD variant can accept the V1 18650 target; maintain controlled datums and do not claim fit.
2. Recheck the DWG-derived contour/datums against clean native-mm source; approve hole/contact function, polarity and plating before creating real pads/holes.
3. Select an exact 18650 MPN and verify its maximum installed envelope, protection, sleeve and terminals.
4. Obtain motor/gearbox, shaft/coupler, current/torque and safe-stall requirements; map mechanical zones against the relevant enclosure variant.
5. Continue schematic, component and placement work for V1; defer a second differently-sized product series until its envelope is supplied. Keep unverified values TBD.
