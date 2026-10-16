# Google Drive index and CAD source reconciliation

Updated: 2026-10-16. This note records the Drive index sweep and CAD-related sources reviewed. It does **not** promote unconfirmed source dimensions or requirements into the current PCB baseline.

## Index review

- The project backup `smart-lock-pcb-pre-cad-2026-10-16.zip` contains the project-specific `docs/learning-index.md`. It is an engineering learning index spanning product/safety, mechanics, power, motor, interfaces, RF/NFC, schematic/PCB, manufacturing, compliance, and supply chain. It is not a CAD file index.
- The project Drive root's `03-mechanical` folder was empty when checked. Its dated backup ZIP has requirements and draft architecture, but no `.FCStd`, `.stp`, `.step`, `.kicad_pro`, `.kicad_sch`, or `.kicad_pcb` source files.
- A Drive-wide filename search surfaced general Arena/GTM/methodology indexes and website `index.html`/`index.js` files in other folders. Those are not part of the `matchbox-smart-lock-pcb` project tree and are not treated as PCB or mechanical design authority.

### Drive index sweep and copy comparison

The filename search found these index-like records, classified by scope:

| Index record | Finding |
|---|---|
| Project ZIP `docs/learning-index.md` | Project-specific engineering-learning index; points to topic areas and requirements, not native CAD. |
| [`INDEX_TREE-Arena记录下载20261003前.md` copy A](https://drive.google.com/file/d/1h9QHILm2h2PqYgtl-ykpsPxMazy2CJHg/view) and [copy B](https://drive.google.com/file/d/1m0giT64Df1xJn1c2bhdqdBmXePwpGoYp/view) | General 2026-10-03 download inventory, not a project index. Metadata differs: 57,491 bytes / MD5 `ba7b66d1f9ee3e0912084bc0dd7ee365` versus 57,393 bytes / MD5 `ced3321b1e5b5bed9f521288e7c9028f`. Local text comparison shows one inventory counts 800 files, the other 799; folder labels differ and one has an extra `INDEX_TREE.md` entry. The listed smart-lock CAD subtree is identical in both. Neither is a canonical PCB source. |
| `00_MTH-J01_Index_FileTree_NamingRules_CN_v3.md` | General Drive file-tree/naming methodology, not a LockPCB requirements source. |
| `session1-gtm-INDEX.md`, `133_Session10_Index_Tree_2026-09-23.md` | Broad session/GTM inventories; available extraction was truncated, but titles/index entries identify marketing, product/visual and website material. CAD records they mention are cross-project historical assets. |
| `00_EXP1-J00_Index_MethodologyExperiment_RunLog_CN_v1.xlsx` | Methodology experiment run log; extraction was partial and it is not design authority. |
| Drive `index.html` / `index.js` search hits | Application/web assets, not KiCad files. |
| `00_MTH-J08_EXP1_Baseline_Required_Source_Package_CN_v1.zip` | Archive listing contains methodology, supplier/channel and outreach material; no native CAD. |

The broad index trees reference smart-lock CAD records (including historical StartHere, shell/cover CAD reviews and the old CAD ZIP) but do not establish that those artifacts are the current LockPCB product/revision. Their references are treated as cross-project history until explicitly matched. The index also names `09_GTM_CAD_Video_Frozen_Discrepancy_Log`, `19_GTM_CAD_Dimension_And_Visual_Gate`, and `32_GTM_CAD_Shaded_Render_Audit`; exact-name Drive searches did not return those as separate readable files, so only their inventory references were inspected and no findings are attributed to their missing contents.

## Newly added PCB-related folder (2026-10-16)

Drive folder: [`锁-PCB-外壳设计稿-260729`](https://drive.google.com/drive/folders/1IWp7LyViBp6CB88CaIeKXHRRBcGfmi9Z), under `20261016-GTM-22-PCB相关`. It is outside the `matchbox-smart-lock-pcb` project folder, but is more directly PCB-related than the earlier general CAD history because its STEP assembly contains products named `SX-PCB-5` and `SX-DB-4`. The STEP's relationship/revision match to the earlier standalone `sx-db-4.stp` has not been reconciled.

Files present: one TXT functional note, one STEP assembly (`sxs-zp-4_asm(1).stp`), one DWG (`PCB板260729(1).dwg`), and five JPGs. There is no KiCad project/schematic/PCB source in this folder.

| File | Drive reference | Review status |
|---|---|---|
| `锁-PCB-功能说明-260729.txt` | [TXT](https://drive.google.com/file/d/13GqUzUHtNP8PWyhGNM2isdlg7kBWRwnV/view) | Text read. |
| `sxs-zp-4_asm(1).stp` | [STEP](https://drive.google.com/file/d/10YUucD4Qwr9iPEB01nr7MfG6hYwjHakQ/view) | Header and product labels inspected; no full CAD application fit/clearance validation. |
| `PCB板260729(1).dwg` | [DWG](https://drive.google.com/file/d/1_i8Ie_12as9PYupyOewx-VSl-qo5jiqW/view) | Binary file identified by its AC1032 signature; not parsed here. |
| `锁芯锁-PCB-尺寸图-260729.jpg` | [Dimension JPG](https://drive.google.com/file/d/1CrQXTpq_i5f4AAkHZWn990P0cuQEvZmb/view) | Visually reviewed; 14 × 50 mm callouts visible. |
| `锁芯锁-PCB-线框图-260729.jpg` | [Wireframe JPG](https://drive.google.com/file/d/1lnwIMNVc-9mXS2CX56u69IZMblFsCH0m/view) | Visually reviewed. |
| `锁芯锁-PCB板位置-260729.jpg` | [Board-location JPG](https://drive.google.com/file/d/1kn3G2QIjk7qyKhZQRZeI6SzfG-rKb3dl/view) | Visually reviewed; positional reference only. |
| `锁-外壳设计稿-带锁芯-260729.jpg` | [Enclosure JPG](https://drive.google.com/file/d/1hLZsR1ZJwSS3A44NaMYfBrszMVyXdVPl/view) | Product-render reference; not a dimension source. |
| `锁-外壳设计稿-棕色-260729.jpg` | [Brown enclosure JPG](https://drive.google.com/file/d/10GuPyWUWmobtuJj1yDZDFCcNFbC1DgWR/view) | Product-render reference; not a dimension source. |

### What the files say or depict

- The TXT note specifies a **single 18500 lithium cell**, **3.3 V motor**, right-hand door as default with a left/right selection procedure, button-operated lock/unlock, blue indicator LED and buzzer feedback, Bluetooth app plus Bluetooth keypad, and lock/unlock motor stall as a signal. It also says the two fixing holes double as positive/negative battery contacts. These are statements in the reference note—not newly user-confirmed requirements or an approved electrical design.
- This conflicts with the current user-confirmed **single 18650** product requirement. The same STEP assembly has product labels `SX-PCB-5`, `SX-AZB-18650`, and `DC-18650-SX`; the labels suggest 18650-related content but do not resolve the TXT conflict or independently identify a qualified battery.
- The PCB dimension JPG visibly calls out **14.00 mm × 50.00 mm**. It also shows 28.00 and 5.00 dimensions whose datums are not sufficiently clear in the JPG. The board-location view shows a long narrow board along the lock interior, with motor/gearing at one end. This 14 × 50 candidate is smaller than the current provisional 17.5 × 60 outline and lies within the 20 × 65 review envelope, but that comparison is not a fit validation or a reason to change the placeholder. Verify against the original DWG/CAD.
- The STEP header identifies `SXS-ZP-4_ASM`, Creo Parametric, 2026-07-29, with millimetre units. Its product labels include several cover variants (`SX-DC-GAI-4`, `SX-DC-DDK`, `SX-DCG-JCP`) as well as the PCB. Do not assume every named variant is installed simultaneously or is the released revision. The assembly's geometry and board-to-housing clearances have not been independently validated in a CAD application.
- The DWG has an AutoCAD `AC1032` file signature, but it was not parsed here; the image/JPG claims above should be checked against that drawing before use.

### Current treatment and recommendation

Treat this folder as a **high-value candidate source**, not yet as the accepted LockPCB design baseline. Preserve the confirmed 18650 requirement and current board-size placeholders until the user confirms the folder's product/revision and the cell-size discrepancy is reconciled. The two-hole battery-contact concept also needs electrical/mechanical review for polarity, contact force, current capacity, oxidation/fretting, retention, and short-circuit protection before it is adopted.

## Relevant CAD records located outside the project folder

| Record | Role recorded in its historical handoff | Current treatment |
|---|---|---|
| [`sx-db-4.stp`](https://drive.google.com/file/d/1kcUb22aSBNMmsP5p2J7B8XdltalI7R8l/view) | Original aluminum shell STEP. A 2026-09-19 handoff records a 39.800 × 22.500 × 90.500 mm envelope and says not to infer dimensions from renders. | Candidate source only; conflicts with a later FCStd-derived envelope (see below). Neither replaces current PCB `TBD` values until the discrepancy and product revision are resolved. |
| [`装配-DB-4-成功.FCStd`](https://drive.google.com/file/d/1a4h7m__cpRPNrWHB-sA8j9MZpQx_kVCL/view) | Main FreeCAD assembly, including links/placements for the shell and sliding battery cover. | Useful for controlled mechanical coordination, but the current PCB repo has no imported CAD or board-to-shell fit. |
| [`装配-db-4.FCStd`](https://drive.google.com/file/d/1qacexo-Whomb3wdFqXjxGQyXdBZgTpwS/view) | Historical handoff identifies this as the shell/body BREP child. | Reference only until opened against the selected assembly and product scope. |
| [`装配-DC-4.FCStd`](https://drive.google.com/file/d/1FyznpYkXJ3PU7L3EOQUYH_T277fETLQ2/view) | Historical handoff identifies this as the sliding cover BREP child. | Reference only; clearance, contact, and manufacturing status are not established for this PCB project. |
| [`CAD-贴锁-设计-stl.zip`](https://drive.google.com/file/d/1HlDJX0bcZY_ZbNKrUjoXj87Bp9M4inLN/view) | Older CAD package with multiple plastic variants, an aluminum shell, a stainless part, images, and a file named `sx-azb-18650(2).stp`. | Historical source package only. Its handoff explicitly rejects some old DDK/GAI/JCP variants and warns against inferring exterior features from old plastic STEP files. The 18650-named STEP is not a verified cell/holder model. |
| [`107_GTM_External_FCStd_Downloaded_And_BottomCover_Geometry_Read_2026-09-20.md`](https://drive.google.com/file/d/10jGjXhu7B6Omfj84Cbk-spfytkRhaxkm/view) and [`105_GTM_External_FCStd_And_BottomBatteryCover_Geometry_Verification_Plan_2026-09-20.md`](https://drive.google.com/file/d/1eOiBiAyqlhkCEDpmcjEjPEgguXJxXR8_/view) | Historical geometry-read and verification records for the FreeCAD assembly and cover. The read report contains BREP bounds/placements and an intersection diagnostic; it expressly says the common volume is not by itself a manufacturing defect and that the intended mating surfaces/clearance need engineering interpretation. | Useful historical measurements only. The reports do not establish PCB fit, current product identity, or a released enclosure. |
| [`00_S5_PRODUCT_START_HERE_CN_v4_2026-09-20.md`](https://drive.google.com/file/d/1RQVbxcRcD9HNACJzoqKb42YM9Zi7D20n/view) | Product/CAD handoff that describes a confirmed shell/cover/knob visual workstream and explicitly flags the mismatch between the STEP and FCStd shell envelopes as unresolved. | Critical discrepancy record; use it to block, not approve, a CAD dimension. |
| [`101_GTM_Drive_FCStd_Assembly_Verification_And_Render_Delete_QA_2026-09-20.md`](https://drive.google.com/file/d/1VUpnewuLlTiiwTEjFBdgys48jRlHkTn3/view) | Records the main assembly links, placements and active slider joint; at that review point child BREP geometry had not yet been independently verified. | Assembly metadata helps understand cover motion; not an engineering fit release. Later 107/111 records report child solid geometry and placements, but not a revision match, approved clearance or PCB fit. |
| [`111_GTM_Workspace_Refresh_Summary_2026-09-20.md`](https://drive.google.com/file/d/1pV8007Nz1O9QpbjdbrPiKxqyx5tq7JsX/view) | Later refresh summary reports that all three FCStd files were present; child shell and cover each contained a single BREP solid, and assembly placements/joint were read. It also records unresolved fit/clearance interpretation. | Stronger evidence the historic assembly geometry is readable, but it remains outside the PCB project and is not a fit/release approval. |
| [`102_GTM_ConfirmedCover_Knob_BatteryCover_From31_TwoImageGate_And_HistoricalCleanupPlan_2026-09-20.md`](https://drive.google.com/file/d/1vuNo74mOWWNg9xEormjg5sg1XJ6I0_40/view) | Visual/asset workflow for a cover, knob and bottom battery cover; says full child BREP and user approval gates remained pending in that workflow. | Visual decisions do not establish this PCB's geometry or its mechanical interface. |
| [`09_GTM_AI_CAD_Combination_Capability_Assessment_CN_v1.md`](https://drive.google.com/file/d/1qazu-EWL359lekGhzyY54BzzHrvZG_4B/view) | Records limits of image/video-to-CAD and notes filenames (including `18650`) do not prove product dimensions, internals, compatibility or battery specification. | Supports the evidence hierarchy used here: native CAD + verified dimensions first; images/video as secondary evidence only. |

The FreeCAD files were downloaded for archival inspection during this review. They are deliberately not copied into Git: Google Drive remains the reference/backup location for large native CAD, while this repository remains the KiCad/electrical source of truth.

## Critical unresolved envelope conflict

The historical CAD handoff reports two different outer-shell envelopes:

| Historical source | Reported envelope (mm) |
|---|---:|
| `sx-db-4.stp` shell STEP | 39.800 × 22.500 × 90.500 |
| `装配-db-4.FCStd` BREP placed in the main assembly (as reported in the 2026-09-20 QA note) | approximately 43.09 × 22.51 × 92.56 |

The historical QA note calculates the FCStd-derived bounds as about 3.286 mm larger on X and 2.057 mm larger on Z than the STEP envelope, and marks the cause unresolved. The [`107` geometry-read record](https://drive.google.com/file/d/10jGjXhu7B6Omfj84Cbk-spfytkRhaxkm/view) gives the shell-child local bounds as X = −21.543136…+21.543136 mm, Y = −0.503532…+22.003532 mm, Z = −21.541602…+71.015493 mm. Applying the main FCStd placement (−4.600000, −7.550001, −22.350000 mm; identity rotation) yields X = −26.143137…+16.943136, Y = −8.053532…+14.453531, Z = −43.891601…+48.665493 mm. The reason these BREP-derived bounds differ from the named STEP envelope is not established.

The same record reports the separate cover BREP at about 33.1025 × 6.4001 × 18.8945 mm, placed at the upper end of the assembly with +90° about X. It records a 15.180740 mm³ geometric common volume between the two placed solids, but explicitly cautions this alone is not proof of a manufacturing interference; mating surfaces and clearance intent are unknown. These geometry values are useful for future controlled reconciliation, not fit approval.

The records do not say which shell version should govern. These are conflicting historical CAD results, not an acceptable tolerance or a dimension to average. Until the source file/revision and coordinate transforms are reconciled by a CAD review, treat **both** as unapproved for PCB fit and keep the mechanical outline and internal clearance TBD.

The older product/CAD handoff also explicitly warns against recovering exterior geometry from old plastic variants or images. The native FCStd files and shell STEP were located in Drive outside the PCB project's own `03-mechanical` folder; cross-project/revision identity is still not confirmed.

## Reconciliation with the current PCB baseline

The current confirmed product requirements remain: compact indoor retrofit lock, no drilling/new wiring, one vertical 1S 18650 alongside a long PCB, and motor/gearing/coupler at the top. The historical shell CAD could be a valuable missing input if it belongs to this exact product/revision, but the two documented outer-envelope values conflict. It is **not yet confirmed as the PCB's usable internal envelope**; wall thickness, battery/contact space, cover travel, motor/gearbox, shaft datum, service access, metal and RF exclusions still consume volume.

Therefore:

1. Keep all mandatory named zones in `pcb/LockPCB.kicad_pcb`; do not replace `TBD` dimensions with the historical external envelope.
2. Keep the current 17.5 × 60 mm board rectangle and 20 × 65 mm review envelope as provisional discussion placeholders only, not a fit claim.
3. Do not reverse-engineer board placement from screenshots or old non-authoritative plastic STEP variants.
4. Before any geometry is frozen, confirm whether the new `SXS-ZP-4_ASM` folder is the current product/revision and resolve its 18500 note versus the confirmed 18650 requirement. Verify the 14 × 50 mm candidate outline against the original DWG and STEP, then check board placement, battery contacts, motor/gearbox, shaft axis, RF/NFC exclusions, cover travel, service access and tolerance stack in one CAD coordinate system.
5. Keep battery model, holder/contact, actual internal free volume, motor specifications, and board-to-shell fit as `TBD` until verified.

## Design lessons retained from the prior engineering records

The pre-CAD engineering archive and previous pin/net drafts support planning for battery-input protection, hardware-safe motor disable, motor fault/current feedback, lock/door sensing, tamper input, service/test access, and optional NFC/keypad/fingerprint interfaces. These are logical interface candidates only. They add no approved device, footprint, pin assignment, voltage/current rating, or firmware requirement. NFC, fingerprint, keypad, Wi-Fi and charging remain optional until selected; Wi-Fi and on-board USB-C charging stay outside the baseline by default.
