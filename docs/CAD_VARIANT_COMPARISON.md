# Comparison of the Two Enclosure CAD Folders

**Purpose:** distinguish a confirmed PCB/enclosure source package from a possible second product-size series. This is an evidence comparison, not a fit report.

## Folder A — `锁-PCB-外壳设计稿-260729`

- Contains a full assembly STEP, `sxs-zp-4_asm(1).stp`, the PCB DWG, PCB-related JPGs, and the factory function TXT.
- The designer PCB drawing evidence gives a 14 × 50 mm board plan, a 1.20 mm thickness callout, and two Ø3.10 mm end-hole features with approximately Ø5 mm concentric rings. The factory function TXT says the two fixing holes also provide positive and negative battery contacts; exact contact construction/polarity/plating still needs confirmation.
- The full assembly contains a battery-like node called `DC-18650-SX` whose previously parsed mesh envelope is approximately 18 × 18 × 50 mm. The same factory function TXT explicitly says 18500. The model name therefore conflicts with its size and the TXT.
- The shell component `SX-DB-4` in this assembly has a previously parsed mesh envelope of about 39.8 × 22.5 × 90.5 mm. This is an outer part envelope, not usable cavity or proof of battery fit.

## Folder B — `CAD-贴锁-外壳设计-stl`

- This is not a single assembled STL. Its root contains `5个零件说明.png` and material-organized folders; the supplied models are individual `.stp` parts.
- The visible parts list describes black-plastic parts, internal plastic parts, an aluminum CNC shell, and a stainless-steel bent part. The image has no readable overall dimensions.
- Separate STEP exports include `sx-db-4.stp`, `sx-dcg-jcp.stp`, `sx-dc-ddk.stp`, `sx-dc-gai-4.stp`, and `sx-azb-18650(2).stp`.
- Those component identifiers also occur inside Folder A's full `sxs-zp-4_asm(1).stp` assembly. In particular, both folders contain the `SX-DB-4` shell part and `SX-AZB-18650` part identifier. The part exports are dated 2025-12, whereas the assembly file is dated 2026-07; file dates and matching names alone do not prove revision identity or a longer enclosure variant.

## Comparison conclusion

- The user's hypothesis that Folder B may describe a longer 18650 product is plausible, but **the files reviewed do not establish it**. Folder B supplies component-level models and a parts illustration, not a dimensioned, assembled enclosure drawing or a clearly identified long-size assembly.
- The repeated part IDs make Folder B look like exports from the same part family/assembly as Folder A, or a related revision, rather than clear evidence of an independent longer-size series. This is a working inference only; geometry/revision identity is not yet verified.
- The `18650` substring in `SX-AZB-18650` is a part name, not a measured battery envelope. Conversely, Folder A's `DC-18650-SX` name is paired with ~18 × 50 mm geometry and a TXT specifying 18500. Do not use either filename alone to assign the cell size.
- The current V1 PCB remains user-directed to target 1S 18650, with a provisional 19 × 70 mm battery planning envelope. That target is not evidence that either CAD folder fits it. The board outline is 14 × 50 mm; no battery or PCB fit is proven.

## Evidence needed to close the comparison

1. Ask the designer which exact assembly/revision is the short 18500 series and which is the longer 18650 series.
2. Obtain a full assembled STEP (or native CAD) for Folder B with its overall dimensions and explicit battery envelope; identify which component is the cell itself, not a holder/plate/contact.
3. Confirm the sample/variant using physical measurements and the cell label/BOM, including protected/unprotected maximum cell length and diameter.
4. Compare both variants in one datum system before making the PCB outline, battery contact locations, and keepout variant-specific.

Until then, keep the two folders as separate evidence sources and do not label Folder B as the confirmed 18650 enclosure.
