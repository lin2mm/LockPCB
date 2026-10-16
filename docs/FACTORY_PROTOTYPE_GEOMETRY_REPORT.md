# Factory Prototype DWG / STEP Geometry Review

Updated: 2026-10-16. Source package: designer-confirmed files in [`锁-PCB-外壳设计稿-260729`](https://drive.google.com/drive/folders/1IWp7LyViBp6CB88CaIeKXHRRBcGfmi9Z), already sent to the factory for prototype sampling. The user also confirms that designer-approved enclosure parts have been sampled and assembled. This review does not claim that the current Agent PCB has been fit-tested in that assembled enclosure.

## Executive result

- **PCB:** the converted DWG, dimension JPG, and STEP mesh agree on a **50.00 × 14.00 mm** board plan envelope. The DWG also calls out **1.20 mm** board thickness and **2 × Ø3.10 mm** end holes. The DWG geometry places those hole centers **37.00 mm** apart, **10.00 mm** from one board end and **3.00 mm** from the other, centered across the 14 mm width. This is consistent with the JPG when the board is oriented the same way.
- **The JPG's 28 mm callout is geometrically reconcilable:** it is not stored as a 28.00 dimension object in the converted DWG, but the DWG coordinates place a central round feature 28 mm from one end hole and 9 mm from the other. The 28 mm feature-to-hole distance matches the JPG in the corresponding orientation. The JPG's 5.00 callout and DWG's 5.50 callout appear to reference different/uncertain datums; do not call them a confirmed discrepancy or equivalent until the feature points are identified.
- **Battery:** the STEP instance named `DC-18650-SX` has a mesh envelope of **18.00 × 17.994 × 50.00 mm**. If this is the cell model, that is 18500-sized geometry, not 18650 length. Thus the TXT's **18500** is supported by this model geometry; the STEP node label `18650` is more likely stale/misleading than the TXT being a typo. This remains an engineering inference, not proof of the factory-installed cell SKU. Another part named `SX-AZB-18650` is 35.50 × 17.501 × 85.549 mm, and its assembly role cannot be established from its label alone.
- **Housing:** the STEP node named `SX-DB-4` measures **39.80 × 22.50 × 90.494 mm** by mesh bounds and agrees with the designer-confirmed standalone shell STEP (about 39.8 × 22.5 × 90.5 mm). A separate designer-confirmed FCStd assembly yields different overall bounds in its inherited handoff; this is a CAD assembly/placement/revision reconciliation item, not evidence that either designer CAD source is an agent test or invalid.
- **Source-authority correction:** the CAD/DWG/STEP files inside designer-provided ZIP packages are designer-confirmed drawings. The PCB layout/graphics inherited from the previous session were agent capability-test outputs, not designer-approved product geometry; they must not be used to set mechanical dimensions or treated as a competing design revision.
- **Agent PCB update:** the previous-session 17.5 × 60 mm test rectangle has been replaced in KiCad by the DWG-derived **14 × 50 mm notched Edge.Cuts** contour. `Dwgs.User` now shows the two Ø3.10 mm holes and Ø5 mm ring geometry as reference circles; these are not yet physical drill definitions or electrical pads. The Agent's other mechanical zone graphics remain proposals. The converter warning/unit-header inconsistency means the imported contour still needs cross-check against a clean native-mm export before fabrication.

## Source identification and method

| Source | Evidence used | Limits |
|---|---|---|
| [Factory DWG](https://drive.google.com/file/d/1_i8Ie_12as9PYupyOewx-VSl-qo5jiqW/view) | Converted to DXF with `dwg2dxf-converter` (embedded LibreDWG 0.13.4); parsed with `ezdxf` 1.4.4. Read dimension entities, circle centers, outline coordinates, and rendered orthographic/isometric views. | Conversion emitted `DWG_ERR_VALUEOUTOFBOUNDS`. The DXF header says `$INSUNITS=1` (inches) and `$MEASUREMENT=0`, while displayed dimensions, coordinates, the STEP header, and the 14 × 50 JPG depiction agree with millimetres. Treat the unit metadata as inconsistent; do not apply a 25.4 scale factor or use this DXF as a clean native-CAD validation. |
| [Factory STEP assembly](https://drive.google.com/file/d/10YUucD4Qwr9iPEB01nr7MfG6hYwjHakQ/view) | Parsed with `occt-import-js` 0.0.23 / OpenCascade WebAssembly, output units set to millimetres, linear deflection 0.05 mm and angular deflection 0.1. Bounds below are calculated from tessellated mesh vertices in assembly coordinates. | These are mesh AABBs, not analytic BREP measurements, tolerance limits, or proof of installed clearance. Assembly includes separate subassemblies/parts; the union is not automatically a product envelope. |
| [Dimension JPG](https://drive.google.com/file/d/1CrQXTpq_i5f4AAkHZWn990P0cuQEvZmb/view) | Visual cross-check of 14.00 × 50.00, 28.00 and 5.00 callouts and board orientation. | Raster and datum visibility are insufficient to replace the DWG/STEP. |
| [Functional TXT](https://drive.google.com/file/d/13GqUzUHtNP8PWyhGNM2isdlg7kBWRwnV/view) | Specifies one 18500 cell and states the two fixing holes also serve as battery positive/negative contacts. | Confirms what the file says, not a qualified battery part number or validated electrical/mechanical design. |

## DWG measurements and feature interpretation

### Dimensions present in the drawing

The 12 dimension objects extracted from the DXF contain these labels/values:

**50.00, 14.00, 12.30, 1.20, 22.00, 15.00, 2 × Ø3.10, 16.00, 5.50, 6.00, 2.80, and 3.00 mm.**

The 50.00 × 14.00 pair is the PCB outside plan envelope; 1.20 is the side-view thickness callout. The two Ø3.10 holes are at the board ends. The remaining numbers are local feature/datum dimensions in orthographic views and should not be reassigned to the battery, mounting-hole pitch, or edge clearance without confirming their extension points.

### KiCad transfer and hole/datum geometry

The parsed top-view board contour has been transferred to `pcb/LockPCB.kicad_pcb` as `Edge.Cuts`, with the following axis transform (units interpreted as millimetres and cross-checked to JPG/STEP):

- `KiCad X = DWG Y − 155.533`; `KiCad Y = −126.741 − DWG X`.
- The transformed bounds are X = 0…14 mm, Y = 0…50 mm. The shape retains the DWG's 0.5 mm rounded corners, 2 mm edge notch, and stepped edge feature; it is not a plain rectangle.
- This source contour replaces the previous Agent test outline. The visual ring/hole circles in `Dwgs.User` are reference graphics only. No drill, plating, pad numbers, or polarity nets have been created; do not treat them as manufacturable contact holes.

- Interpreting the parsed drawing coordinates as millimetres (consistent with the JPG and STEP), the two end-hole centers are approximately **(−173.741, 162.533)** and **(−136.741, 162.533)**, which map to KiCad reference coordinates **(7, 47)** and **(7, 10) mm**. Their center pitch is **37.000 mm**.
- The dimension chain **22.00 + 15.00 = 37.00 mm** independently describes that center pitch relative to the drawing datum.
- Against the 50 mm outline, the end-hole centers are **3.00 mm** and **10.00 mm** from the respective ends. The hole centers are at the 14 mm width midpoint (7.00 mm from each long edge).
- In the matching JPG orientation, the hole 10 mm from the end is at the top and the hole 3 mm from the opposite end is at the bottom. A central round feature lies 9 mm from the top hole and 28 mm from the bottom hole, which reconciles the JPG's visible **28.00 mm** callout. The converted DWG has no explicit 28.00 dimension entity, but the relevant feature coordinates produce that distance.
- The DWG's **5.50 mm** dimension is tied to a different point/datum in the lower orthographic view than can be identified confidently from the JPG's **5.00 mm** callout. It is not yet established that these are intended to measure the same feature spacing. Other local dimensions (12.30, 16.00, 6.00, 2.80 and 3.00) are retained as extracted values; feature intent remains to be confirmed.

## STEP mesh bounds

All dimensions in this table are **mesh-derived X × Y × Z bounds**, not part-name semantics:

| STEP product/node label | Mesh bounds (mm) | Interpretation and caveat |
|---|---:|---|
| `SX-PCB-5` | **14.00 × 5.70 × 50.00** | Board plan size agrees with DWG/JPG. The 5.70 mm value is the complete mesh envelope (board plus modeled component height), not bare laminate thickness; the DWG separately specifies 1.20 mm. |
| `DC-18650-SX` | **18.00 × 17.994 × 50.00** | Near-cylindrical nominal envelope consistent with an 18 × 50 mm (18500-size) cell. It is 50 mm long despite the `18650` label. It does not identify maker, chemistry, protection, terminal geometry, or SKU. |
| `SX-AZB-18650` | **35.50 × 17.501 × 85.549** | 18650-labelled battery-associated model, but too large to identify as a bare cell; role is not established from the available geometry/name alone. Do not treat it as independent proof of a 18650 cell. |
| `SX-DB-4` | **39.80 × 22.50 × 90.494** | Shell mesh envelope; agrees with the older standalone shell STEP's nominal external dimensions. Does not provide usable cavity or wall-thickness clearance by itself. |
| All imported meshes (union AABB) | **39.80 × 79.60 × 91.250** | Not a confirmed installed-device envelope. The STEP root contains several distinct components/subassemblies, including `SXS-DCG-ZP_ASM` and `SX-ST-ZP_ASM`; some parts extend outside the shell's AABB. Do not size the PCB or lock from this union. |

### Preliminary board-to-cell placement check

In the STEP assembly coordinate frame, `SX-PCB-5` spans X = 1.8…15.8 mm, Y = 15.8…21.5 mm, Z = 13…63 mm; `DC-18650-SX` spans X = −16.8…1.2 mm, Y = 1.303…19.297 mm, Z = 15.5…65.5 mm. Their axis-aligned boxes are separated by only **0.6 mm in X**, while overlapping in Y and Z. This is a coarse AABB observation—not a true surface-to-surface clearance or interference test—but it flags a very tight nominal side-by-side stack. Check the actual BREP surfaces, cell wrapper/holder, PCB components, contact hardware, assembly tolerances, and insulation before approving the fit.

## Battery assessment: file label versus modeled geometry versus fact

1. **Verified file text:** the factory functional TXT says 18500. The earlier product brief said 18650. The STEP names both `DC-18650-SX` and `SX-AZB-18650`.
2. **Verified parsed geometry:** the node `DC-18650-SX` is about 18 mm across and 50 mm long. That geometry supports an 18500-size model, not an 18650-length model. The other 18650-labelled node is not the size of a bare cell.
3. **Engineering inference:** the most consistent reading is that the TXT's 18500 is intentional for this factory prototype and the `DC-18650-SX` label is stale/incorrect. This is more likely than a TXT typo, but the parser cannot determine the installed production/prototype SKU or whether the STEP cell is merely illustrative.
4. **Still requiring owner/factory confirmation:** read the actual sampled cell label or BOM and confirm the full cell part number, chemistry, protected/unprotected configuration, dimensions including terminal/insulating sleeve, and contact/polarity arrangement. If 18650 is still the product requirement, replace/rebuild the 50 mm cell model with the actual 65 mm-class envelope and re-run the enclosure, PCB, contact and retention checks; do not solve this by renaming a part.

## Engineering recommendations

1. **Close the identity question from the physical sample/BOM.** Until that check, record the factory STEP geometry as 18 × 50 mm and keep the system-level SKU unresolved. Correct the stale CAD node/assembly labels and functional spec together after approval.
2. **Treat the two Ø3.10 mounting/contact holes as a coupled mechanical-electrical safety item.** Confirm positive/negative mapping, terminal material/plating, contact preload, resistance under vibration, screw/washer stack, polarity protection, exposed metal isolation, short-circuit protection and service/replacement procedure. No current or contact-force rating is established by the CAD.
3. **Check the motor against the entire 1S voltage range.** The TXT specifies a 3.3 V motor and a single lithium cell; verify motor winding/driver limits at the cell's maximum voltage (not only nominal voltage), startup/stall current, pulse duty and thermal conditions. Treat stall as a bounded detection event with a current/time limit and safe shutoff, not as the only protection.
4. **Continue the source-aligned KiCad design.** The DWG-derived notched outline and reference hole rings have been imported. Cross-check the origin/transform and every contour feature against a clean native-mm export, then implement Ø3.10 drills and electrical contact pads only after polarity/plating design approval. Keep motor/RF/service/metal zones clearly marked as Agent proposals until mapped from the selected, assembled designer housing CAD.
5. **Perform a true clearance/tolerance review.** Inspect the full STEP assembly in a CAD application, identify which cover/variant is used, verify battery-to-board/component clearances and enclosure wall/cover movement, and include cell wrapper, contacts, fasteners and manufacturing/assembly tolerances. The 0.6 mm AABB gap is a risk flag, not a pass/fail result.
6. **Preserve source distinctions.** The designer-confirmed package is authoritative for the submitted prototype revision, but a file label is not an independently verified SKU, a tessellated AABB is not a GD&T tolerance, and this review is not fabrication readiness. No KiCad, electrical, fit or safety validation is claimed here.
