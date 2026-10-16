# Mechanical Source Baseline — LockPCB

**State:** current engineering starting point. V1 PCB design is now directed to target one 1S 18650. This record separates that user-selected design target from the factory-source model, which appears 18500-like; it is not a manufacturing release or fit report.

## Provenance and authority

- The user confirms that all eight files in Drive folder `锁-PCB-外壳设计稿-260729` are designer-confirmed facts/confirmation drawings already sent to the factory for sampling. CAD/DWG/STEP files inside designer-provided ZIPs are also designer-confirmed source documents. A second folder, `CAD-贴锁-外壳设计-stl`, contains component STEP exports with part IDs overlapping the first assembly; its status as a longer 18650 product variant is unconfirmed. See [`CAD_VARIANT_COMPARISON.md`](CAD_VARIANT_COMPARISON.md).
- The designer enclosure parts have been sampled and assembled. Use the physical enclosure as the mechanical anchor. This does **not** establish that the Agent PCB, cell, contacts, or motor fit it.
- Preserve original CAD, DWG, STEP, drawing and archive filenames and contents. Treat Agent-created board graphics/zone placement as editable engineering work, never as designer-approved product geometry.
- The Google Drive CAD-summary Markdown from the older visual/cover workflow has been moved to recoverable Trash. Designer source drawings, CAD archives, and source folders were not trashed.

## PCB geometry from the confirmed factory package

- Designer DWG/JPG/STEP evidence agrees on a **50 × 14 mm** PCB plan envelope. The DWG calls out **1.20 mm** thickness and **2 × Ø3.10 mm** end holes.
- Parsed DWG perimeter coordinates: X `[-176.741, -126.741]`, Y `[155.533, 169.533]`. Applied mapping into the KiCad board: `KiCad X = DWG Y − 155.533`; `KiCad Y = −126.741 − DWG X`. This produces a 14 × 50 mm envelope and retains the notched/stepped contour.
- Hole centers map to KiCad `(7,10)` and `(7,47)` mm, 37 mm pitch. The DWG also depicts approximately Ø5 mm concentric features.
- The DWG-to-DXF conversion emitted `DWG_ERR_VALUEOUTOFBOUNDS`; its `$INSUNITS=1` inch header is inconsistent with the millimetre geometry cross-checked against the JPG and STEP. Do not apply a 25.4 scale factor blindly. Recheck the contour/datum against a clean native-mm source/export before making manufacturing data.
- Current `pcb/LockPCB.kicad_pcb` has the derived outline in `Edge.Cuts`. Hole/ring circles are `Dwgs.User` visual references only: there are no actual drills, plated holes, contact pads, pad numbers, or polarity nets yet.
- Factory STEP node `SX-PCB-5` has a tessellated mesh envelope of 14 × 5.7 × 50 mm; 5.7 mm is the modeled board-plus-components envelope, not bare laminate thickness.

## Cell and assembled enclosure

- **V1 design target:** one 1S 18650 beside the long PCB, per the user's latest direction. Exact MPN, chemistry, protection, terminals and installed envelope remain TBD. The factory functional TXT specifies 18500; STEP node `DC-18650-SX` is approximately 18 × 18 × 50 mm, which is 18500-size geometry despite its 18650-like label. Therefore, do not claim the supplied factory/sample enclosure fits the V1 target until checked. A second differently-sized product series may follow; its dimensions and cell format are not yet specified.
- Factory STEP shell mesh `SX-DB-4` is approximately 39.8 × 22.5 × 90.494 mm. This is a tessellated part envelope, not the assembled cavity, internal clearance, or tolerance stack.
- Identify the exact designer CAD variant/revision corresponding to the physical sampled assembly before using any alternate cover or internal-part model. The assembled physical enclosure is authoritative for follow-up fit checks; no Agent PCB fit has yet been proven.
- Do not infer cell clearance, fit, usable cavity, motor/shaft alignment, or wall thickness from a bounding box, filename, visual render, or separate-part model alone.

## Required KiCad mechanical labels

The following named regions/axes are required in the editable PCB source:

`BATTERY_KEEP_OUT`, `BATTERY_CONTACT_ZONE`, `PCB_MAX_OUTLINE`, `MOTOR_GEARBOX_ZONE`, `SHAFT_AXIS`, `NFC_ANTENNA_ZONE`, `METAL_LOCKBODY_ZONE`, `SERVICE_ACCESS_ZONE`, `NO_COMPONENT_ZONE`.

These are current planning annotations. The V1 battery graphic is a provisional 19 × 70 mm 18650 envelope, not an enforced KiCad keepout; revise it to the selected cell's maximum dimensions and tolerance allowance. Except for the actual `Edge.Cuts` outline, do not interpret annotations as validated clearances or final electrical keepouts. `NO_COMPONENT_ZONE` is provisional and must be rederived from confirmed mechanical dimensions.

## Engineering status and next gates

- The board has no components, pads, nets, copper pours, or routed tracks. The schematic remains text-only design intent; the structural/intent checks do not prove circuit connectivity or fit.
- Still open: match CAD revision to sample and determine whether the V1 18650 envelope fits; native-mm datum check; exact 18650 SKU/protection/terminals; contact polarity/plating/force/current; motor/gearbox, shaft and coupler interface; enclosure metal and antenna boundaries; assembly and manufacturing tolerances. The future size-series variant remains out of scope until dimensions arrive.
- Recommended order: (1) compare the source CAD against the physical assembly and establish datums; (2) verify the DWG contour and holes; (3) close cell/contact/motor geometry; (4) establish measured zones/clearances; (5) only then implement real KiCad drills/pads, placements, netlist, routing and fabrication checks.

No fit, electrical safety, hardware test, or fabrication readiness is claimed.
