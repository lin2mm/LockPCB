# File Naming Rules — LockPCB

**Status:** project recommendation, based on the accessible Drive methodology and file-tree records; the referenced J00 master workbook was not located in Drive search and was not read. Do not present this as a verbatim transcription of that missing workbook.

## What the accessible indexes/rules say

- `00_MTH-J01_NamingStorageRules_CN_v2.md` gives the general pattern:

  `NN_<ProductCode>-<CategoryLetter><Seq>_<DocType>_<Subject>_<Scope>_<Lang>_vX[_Status].ext`

  `NN` is a short ordering prefix; the product/category/sequence identifies the workstream; the remaining fields state artifact type, subject, scope, language, version, and optional status.
- Its verified **A–K** categories are GTM/business-specific: A product/claims; B visuals/assets/marketing; C market/legal; D ICP/orders; E data sources/lists; F scoring/validation; G supply-chain/ecosystem research; H outreach/waves; I results/retrospective; J methodology/index/scripts; K cost operations. These do not provide a suitable mechanical, PCB, or electrical-CAD category map.
- The same v2 note says to group files by module/category, keep root-level indexes/method summaries/handoffs only, prefix generated files with a sequence/class, preserve backups and source documents, and use recoverable Drive Trash—not permanent deletion—for authorized cleanup.
- `00_MTH-J01_Index_FileTree_NamingRules_CN_v3.md` is a tree snapshot, not a complete prose rule. It points to `00_MTH-J00_Index_DualMethodology_FileRules_CN_v3.xlsx` and a J02 audit/handoff. The J00 workbook and same-name Markdown were not found as standalone Drive files in this audit. The tree includes older versions, rename logs, and a pre-rename backup; those listings are inventory/history, not LockPCB requirements.
- `00_MTH-J07_Agent3_Start_Summary_Plan_CN_v2.md` independently repeats the compact form `NN_<Code>-<Cat><Seq>_<Type>_<Subject>_<Scope>_<Lang>_vX`.
- `123_SOP-ONE_GTM_Lean_Rules_2026-09-22.md` states that detailed naming remains owned by the relevant category method; it recommends readable fields, preserving original source names and identity, and a broad generated-file pattern `project_category_subject_sku-or-scene_version_date_status.ext`. This is not a CAD-specific standard and does not supersede a project-specific engineering rule.
- Broad indexes such as `session1-gtm-INDEX.md`, `133_Session10_Index_Tree_2026-09-23.md`, workspace inventories and the two `INDEX_TREE` snapshots are principally cross-project file inventories. They are not a LockPCB CAD rulebook. Large inventory extractions were truncated, so this review does not claim to have exhaustively audited every unrelated file title/content.

## Recommended LockPCB convention

Adopt the general structured pattern but create an explicit **project-local** category namespace:

`NN_LPCB-<Domain><Seq>_<ArtifactType>_<Subject>_<Scope>_<Lang>_vX[_Status].ext`

Suggested domain letters:

- `J` — index, source register, decision log, handoff/method.
- `M` — mechanical and CAD-source interpretation.
- `P` — PCB layout, board geometry and fabrication engineering.
- `E` — schematic, electrical architecture and component decisions.
- `T` — test, validation and review evidence.

These are LockPCB extensions, **not** the unrelated GTM A–K taxonomy. Keep the field values short, ASCII, stable, and searchable. Use ISO dates only when a date is useful; do not encode mutable dimensions or inferred SKU in a canonical filename. Put version and workflow status in the file name only where useful, and keep the content's provenance/status explicit too.

Examples for new reports (illustrative, not a renaming mandate):

- `00_LPCB-J01_Index_SourceRegister_Project_EN_v1.md`
- `01_LPCB-M01_Source_DWG_PCBOutline_FactorySample_CN_v1.md`
- `02_LPCB-M02_Source_STEP_EnclosureAssembly_FactorySample_CN_v1.md`
- `03_LPCB-P01_Design_PCBMechanicalOutline_Prototype_EN_v1_review.md`
- `04_LPCB-E01_Decision_BatterySKU_Selection_EN_v1_TBD.md`
- `05_LPCB-T01_Report_ClearanceReview_EnclosureFit_EN_v1.md`

## Apply without breaking CAD and provenance

- **Do not rename designer originals** inside source archives. Record their exact original filenames, Drive location, revision/date and checksum in a source register.
- Preserve native CAD/KiCad interoperability names: `pcb/LockPCB.kicad_pro`, `LockPCB.kicad_pcb`, and `LockPCB.kicad_sch`. Do not force a sequence prefix onto a KiCad project basename or generated files that tools expect to match.
- Keep code and source-of-truth files in the repository's existing `pcb/`, `docs/`, `decisions/`, and `ci/` directories. Use the structured prefix for new standalone reports, evidence packages and handoffs, not for every code file.
- Every engineering summary should label each claim as designer/source-confirmed, directly measured/parsed, Agent-derived, or TBD. A filename or directory position never upgrades evidence status.
