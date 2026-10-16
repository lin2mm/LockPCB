# Google Drive index and legacy CAD source reconciliation

Updated: 2026-10-16. This note records what was found while checking Drive indexes and earlier CAD-related records. It does **not** promote older CAD dimensions into the current PCB requirements.

## Index review

- The project backup `smart-lock-pcb-pre-cad-2026-10-16.zip` contains the project-specific `docs/learning-index.md`. It is an engineering learning index spanning product/safety, mechanics, power, motor, interfaces, RF/NFC, schematic/PCB, manufacturing, compliance, and supply chain. It is not a CAD file index.
- The project Drive root's `03-mechanical` folder was empty when checked. Its dated backup ZIP has requirements and draft architecture, but no `.FCStd`, `.stp`, `.step`, `.kicad_pro`, `.kicad_sch`, or `.kicad_pcb` source files.
- A Drive-wide filename search also surfaced general Arena/GTM/methodology indexes and website `index.html`/`index.js` files in other folders. Those are not part of the `matchbox-smart-lock-pcb` project tree and are not treated as PCB or mechanical design authority. A broad Arena index tree does reference other smart-lock product/CAD work; its references are treated as cross-project history until the user confirms they describe this exact product.

## Relevant CAD records located outside the project folder

| Record | Role recorded in its historical handoff | Current treatment |
|---|---|---|
| [`sx-db-4.stp`](https://drive.google.com/file/d/1kcUb22aSBNMmsP5p2J7B8XdltalI7R8l/view) | Original aluminum shell STEP. The 2026-09-19 CAD handoff records a shell envelope of 39.800 × 22.500 × 90.500 mm and says to take dimensions from this CAD source, not from renders. | Useful candidate shell reference; product identity and current revision still need confirmation before it can replace the current PCB `TBD` envelope. |
| [`装配-DB-4-成功.FCStd`](https://drive.google.com/file/d/1a4h7m__cpRPNrWHB-sA8j9MZpQx_kVCL/view) | Main FreeCAD assembly, including links/placements for the shell and sliding battery cover. | Useful for controlled mechanical coordination, but the current PCB repo has no imported CAD or board-to-shell fit. |
| [`装配-db-4.FCStd`](https://drive.google.com/file/d/1qacexo-Whomb3wdFqXjxGQyXdBZgTpwS/view) | Historical handoff identifies this as the shell/body BREP child. | Reference only until opened against the selected assembly and product scope. |
| [`装配-DC-4.FCStd`](https://drive.google.com/file/d/1FyznpYkXJ3PU7L3EOQUYH_T277fETLQ2/view) | Historical handoff identifies this as the sliding cover BREP child. | Reference only; clearance, contact, and manufacturing status are not established for this PCB project. |
| [`CAD-贴锁-设计-stl.zip`](https://drive.google.com/file/d/1HlDJX0bcZY_ZbNKrUjoXj87Bp9M4inLN/view) | Older CAD package with multiple plastic variants, an aluminum shell, a stainless part, images, and a file named `sx-azb-18650(2).stp`. | Historical source package only. Its handoff explicitly rejects some old DDK/GAI/JCP variants and warns against inferring exterior features from old plastic STEP files. The 18650-named STEP is not a verified cell/holder model. |
| [`107_GTM_External_FCStd_Downloaded_And_BottomCover_Geometry_Read_2026-09-20.md`](https://drive.google.com/file/d/10jGjXhu7B6Omfj84Cbk-spfytkRhaxkm/view) and [`105_GTM_External_FCStd_And_BottomBatteryCover_Geometry_Verification_Plan_2026-09-20.md`](https://drive.google.com/file/d/1eOiBiAyqlhkCEDpmcjEjPEgguXJxXR8_/view) | Historical geometry-read and verification records for the FreeCAD assembly and cover. The read report contains BREP bounds/placements and an intersection diagnostic; it expressly says the common volume is not by itself a manufacturing defect and that the intended mating surfaces/clearance need engineering interpretation. | Evidence that usable enclosure/cover CAD exists; not evidence of a PCB fit or released enclosure. |

The FreeCAD files were downloaded for archival inspection during this review. They are deliberately not copied into Git: Google Drive remains the reference/backup location for large native CAD, while this repository remains the KiCad/electrical source of truth.

## Reconciliation with the current PCB baseline

The current confirmed product requirements remain: compact indoor retrofit lock, no drilling/new wiring, one vertical 1S 18650 alongside a long PCB, and motor/gearing/coupler at the top. The historical shell envelope could be a valuable missing input if it belongs to this exact product/revision. It is **not yet confirmed as the PCB's usable internal envelope**; wall thickness, battery/contact space, cover travel, motor/gearbox, shaft datum, service access, metal and RF exclusions still consume volume.

Therefore:

1. Keep all mandatory named zones in `pcb/LockPCB.kicad_pcb`; do not replace `TBD` dimensions with the historical external envelope.
2. Keep the current 17.5 × 60 mm board rectangle and 20 × 65 mm review envelope as provisional discussion placeholders only, not a fit claim.
3. Do not reverse-engineer board placement from screenshots or old non-authoritative plastic STEP variants.
4. Before any geometry is frozen, confirm the product/revision match and obtain the current complete shell/assembly plus battery contact, motor/gearbox, shaft-axis and service-access geometry. Then check the board, RF/NFC exclusions, clearances, cover travel, and tolerance stack in the same CAD coordinate system.
5. Keep battery model, holder/contact, actual internal free volume, motor specifications, and board-to-shell fit as `TBD` until verified.

## Design lessons retained from the prior engineering records

The pre-CAD engineering archive and previous pin/net drafts support planning for battery-input protection, hardware-safe motor disable, motor fault/current feedback, lock/door sensing, tamper input, service/test access, and optional NFC/keypad/fingerprint interfaces. These are logical interface candidates only. They add no approved device, footprint, pin assignment, voltage/current rating, or firmware requirement. NFC, fingerprint, keypad, Wi-Fi and charging remain optional until selected; Wi-Fi and on-board USB-C charging stay outside the baseline by default.
