# Mechanical Source Baseline — LockPCB

**State:** current engineering starting point. This is a compact record of designer-confirmed inputs and the Agent PCB's derived state; it is not a manufacturing release or fit report.

## Provenance and authority

- The user confirms that all eight files in Drive folder `锁-PCB-外壳设计稿-260729` are designer-confirmed facts/confirmation drawings already sent to the factory for sampling. CAD/DWG/STEP files inside designer-provided ZIPs are also designer-confirmed source documents.
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

- The earlier project brief specifies one vertical 18650 / 1S cell beside the long PCB; the factory functional TXT specifies 18500. STEP node `DC-18650-SX` is approximately 18 × 18 × 50 mm, which is 18500-size geometry despite its label. The actual cell SKU is **TBD** pending the sampled battery label/BOM and terminal/protection details. Do not silently choose either size.
- Factory STEP shell mesh `SX-DB-4` is approximately 39.8 × 22.5 × 90.494 mm. This is a tessellated part envelope, not the assembled cavity, internal clearance, or tolerance stack.
- Identify the exact designer CAD variant/revision corresponding to the physical sampled assembly before using any alternate cover or internal-part model. The assembled physical enclosure is authoritative for follow-up fit checks; no Agent PCB fit has yet been proven.
- Do not infer cell clearance, fit, usable cavity, motor/shaft alignment, or wall thickness from a bounding box, filename, visual render, or separate-part model alone.

## Required KiCad mechanical labels

The following named regions/axes are required in the editable PCB source:

`BATTERY_KEEP_OUT`, `BATTERY_CONTACT_ZONE`, `PCB_MAX_OUTLINE`, `MOTOR_GEARBOX_ZONE`, `SHAFT_AXIS`, `NFC_ANTENNA_ZONE`, `METAL_LOCKBODY_ZONE`, `SERVICE_ACCESS_ZONE`, `NO_COMPONENT_ZONE`.

These are current planning annotations. Except for the actual `Edge.Cuts` outline, do not interpret them as validated clearances or final electrical keepouts. `NO_COMPONENT_ZONE` is provisional and must be rederived from confirmed mechanical dimensions.

## Engineering status and next gates

- The board has no components, pads, nets, copper pours, or routed tracks. The schematic remains text-only design intent; the structural/intent checks do not prove circuit connectivity or fit.
- Still open: match CAD revision to sample; native-mm datum check; cell SKU/protection and terminal configuration; contact polarity/plating/force/current; motor/gearbox, shaft and coupler interface; enclosure metal and antenna boundaries; assembly and manufacturing tolerances.
- Recommended order: (1) compare the source CAD against the physical assembly and establish datums; (2) verify the DWG contour and holes; (3) close cell/contact/motor geometry; (4) establish measured zones/clearances; (5) only then implement real KiCad drills/pads, placements, netlist, routing and fabrication checks.

No fit, electrical safety, hardware test, or fabrication readiness is claimed.
