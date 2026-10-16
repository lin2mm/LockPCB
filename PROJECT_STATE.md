# LockPCB — 当前项目状态

Updated: 2026-10-16. Status: **PCB engineering skeleton / source-derived mechanical outline / electrical and fit validation open.**

## Source of truth and scope

- Private repository: `lin2mm/LockPCB`; work only on `arena/3b84c22f-lockpcb`; do not merge `main`.
- Checkout: `/home/user/LockPCB`. GitHub branch tree is the source of truth for the editable KiCad project. Designer-confirmed source CAD/DWG/STEP remains in Google Drive and original archives; preserve those inputs.
- This phase is PCB engineering only: no firmware flashing, purchasing, fabrication, or real hardware test.
- Read `docs/MECHANICAL_SOURCE_BASELINE.md` before mechanical changes. It is the single current project summary for designer-source facts, derived board geometry, and open validation items.

## Current KiCad source

- Files: `pcb/LockPCB.kicad_pro`, `pcb/LockPCB.kicad_sch`, `pcb/LockPCB.kicad_pcb`.
- PCB outline: source-derived notched 14 × 50 mm envelope in `Edge.Cuts`; visual references for two Ø3.10 mm holes and ~Ø5 mm concentric features are not drills/pads. DWG calls out 1.20 mm thickness. Native-mm/source datum verification remains open because the conversion emitted warnings and inconsistent unit metadata.
- The nine required mechanical labels exist as annotated layers. They are not proof of clearance or fit; `NO_COMPONENT_ZONE` is a provisional keepout placeholder.
- The PCB has no actual component footprints, electrical pads, nets, copper pours, or routed tracks. The A3 schematic is text-only architecture and signal intent, not pin-level connectivity.
- Layer-count, parts, BOM MPNs, footprints, battery contact implementation, exact cell SKU, motor/gearbox interface, and antenna clearances remain TBD or provisional recommendations.

## Mechanical-source baseline

- The designer-confirmed package under Drive folder `锁-PCB-外壳设计稿-260729` contains eight factory prototype documents already sent for sampling; the user also confirms designer enclosure parts have been sampled and assembled. Use the physical assembled enclosure as the mechanical anchor.
- The DWG/JPG/STEP-derived PCB plan is 50 × 14 mm, with 1.20 mm DWG thickness callout and two Ø3.10 mm end holes. Full coordinate mapping and evidence limits are in the mechanical baseline.
- Cell identity remains unresolved: the brief says 18650/1S; factory TXT says 18500; a STEP node named `DC-18650-SX` measures about 18 × 18 × 50 mm. Confirm against sampled cell label/BOM; do not infer SKU from a node name or AABB.
- Board-to-enclosure/cell/contact/motor fit, tolerances, and product-revision mapping have not been demonstrated. No fabrication readiness is claimed.

## Validation

- Cleanup baseline commit: `0d5895dbd61aa7f1c864f90f2ba510dbf238ac89` on the session branch.
- [GitHub Actions run 38900003033](https://github.com/lin2mm/LockPCB/actions/runs/38900003033) passed KiCad 8 load/export, ERC/DRC, netlist export, structure/intent checks and SVG exports. This validates the checked files under CI, not physical fit, electrical completeness, or fabrication readiness.
- Local KiCad CLI/GUI is unavailable in this workspace.

## Next engineering gates

1. Match the selected designer-confirmed CAD variant/revision to the sampled, assembled enclosure; keep component-origin coordinate transforms in one controlled datum system.
2. Recheck the DWG-derived contour and datums against a clean native-mm drawing/export; approve drill, plating, polarity and contact design before creating real pads/holes.
3. Resolve cell SKU from the physical sample/BOM, including protection, sleeve, terminals and installed envelope.
4. Obtain motor/gearbox, shaft/coupler, current/torque and safe-stall requirements; map the required mechanical labels/zones from the confirmed assembly.
5. Then progress to actual schematic symbols/pins/nets, component selection and fit/tolerance review. Preserve all unverified values as TBD.
